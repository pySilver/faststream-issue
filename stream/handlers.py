import asyncio
import random
import pandas as pd
import datetime

from faststream.nats.annotations import NatsBroker
from nats.js.kv import KeyValue as KV
from typing_extensions import Annotated
from faststream.nats import JStream, PullSub
from faststream import Logger, Context
from datetime import datetime


from . import FEEDS_COUNT, APP_NAME, PRODUCTS_PER_FEED_MIN, PRODUCTS_PER_FEED_MAX
from .routers import router
from .types import FeedState

FeedsKeyValue = Annotated[KV, Context("feeds_kv")]
NewProductsKeyValue = Annotated[KV, Context("new_products_kv")]

stream = JStream(
    name="product_feeds",
    subjects=["product_feeds", "product_feeds.>"],
    declare=False,
)

images_df = pd.read_csv("./data/images.csv")

pull_sub = PullSub(batch_size=10, timeout=2)


@router.subscriber(
    "product_feeds.feeds_update_requested",
    stream=stream,
    durable=APP_NAME,
    max_workers=1,
    pull_sub=pull_sub,
)
async def update_feeds(msg: str, broker: NatsBroker, logger: Logger):
    for i in range(1, FEEDS_COUNT + 1):
        logger.info(f"Updating feed; feed_id={i}")
        await broker.publish(
            message=i,
            stream=stream.name,
            subject="product_feeds.one_feed_update_requested",
        )


@router.subscriber(
    "product_feeds.one_feed_update_requested",
    stream=stream,
    durable=APP_NAME,
    max_workers=1,
    pull_sub=pull_sub,
)
async def update_feed(
    feed_id: int, feeds_kv: FeedsKeyValue, broker: NatsBroker, logger: Logger
):
    logger.info(f"Downloading feed; feed_id={feed_id}")

    # Imagine downloading the feed from a remote server
    await asyncio.sleep(10)

    # Clear any previous state
    await feeds_kv.delete(f"feed_import_{feed_id}")
    # TODO: Load feed configuration from a database to determine items in the XML feed

    items_count = 0
    for item_id in range(
        1, random.randint(PRODUCTS_PER_FEED_MIN, PRODUCTS_PER_FEED_MAX) + 1
    ):
        logger.info(f"Processing item; item_id={item_id} feed_id={feed_id}")
        raw_item = {
            "id": item_id,
            "title": f"Product {item_id}",
            "price": random.randint(-100, 500),
            "description": "This is a product",
            "images": images_df.sample(3)["image_link"].to_list(),
            "gender": random.choice(["male", "female"]),
            "age_group": random.choice(["adult", "children"]),
            "merchant_id": feed_id,
            "size": None,
        }
        await broker.publish(
            {"item": raw_item, "feed_id": feed_id},
            stream=stream.name,
            subject="product_feeds.raw_product_received",
        )
        items_count += 1

    # Update the feed state
    feed_state = FeedState(
        items_count=items_count,
        items_approved=0,
        items_rejected=0,
        started_at=datetime.datetime.now(),
    )
    await feeds_kv.put(f"feed_import_{feed_id}", feed_state.json().encode())
    logger.info(f"Scheduled {items_count} products within the feed; feed_id={feed_id}")
