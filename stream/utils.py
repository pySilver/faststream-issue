import imghdr
import os
import time
from typing import Optional, Dict, Any, List, TYPE_CHECKING

from pydantic import FilePath
from tenacity import retry, stop_after_attempt, wait_exponential

from .types import FeedState, ProductImage, FeedProduct

if TYPE_CHECKING:
    from .handlers import FeedsKeyValue


@retry(stop=stop_after_attempt(5))
async def increment_feed_import_state_counter(
    feeds_kv: "FeedsKeyValue", feed_id: int, counter: str
):
    state_entry = await feeds_kv.get(f"feed_import_{feed_id}")
    state_value = FeedState.parse_raw(state_entry.value.decode())
    state_value.increment_counter(counter)
    state_value.is_completed()

    await feeds_kv.update(
        f"feed_import_{feed_id}",
        state_value.json().encode(),
        last=state_entry.revision,
    )


async def get_image_extension_from_bytes(image_bytes) -> Optional[str]:
    image_type = imghdr.what(None, h=image_bytes)
    return image_type


@retry(stop=stop_after_attempt(5), wait=wait_exponential(multiplier=1, min=4, max=10))
async def download_image(session, url):
    async with session.get(url) as response:
        return await response.read()


def discover_product_attributes(product: FeedProduct) -> Dict[str, Any]:
    # Imagine this function would be used to discover product attributes using ML inference
    time.sleep(10)

    return {
        "color": "blue",
        "material": "cotton",
    }


def discover_product_category(product: FeedProduct) -> str:
    # Imagine this function would be used to discover product category using ML inference
    time.sleep(10)

    return "women t-shirt"


def save_product_images(merchant_id: int, images: List[ProductImage]) -> List[FilePath]:
    # Create the directory if it doesn't exist
    directory = f"../data/product_images/{merchant_id}"
    os.makedirs(directory, exist_ok=True)

    image_paths = []
    for image in images:
        path = f"{directory}/{image.filename}.{image.extension}"

        with open(path, "wb") as f:
            f.write(image.source)

        image_paths.append(path)

    return image_paths
