from faststream import FastStream
from faststream.nats.annotations import ContextRepo
from faststream.nats import NatsBroker
from stream.routers import router
import importlib


# Automatically import files with handlers (across all modules)
importlib.import_module("stream.handlers")

broker = NatsBroker("nats://localhost:4222")
broker.include_router(router)
app = FastStream(broker)


@app.on_startup
async def setup_broker(context: ContextRepo):
    await broker.connect()

    new_products_kv = await broker.stream.create_key_value(
        bucket="new_products",
        description="Bucket for newly discovered products",
        ttl=3600 * 24 * 7,
    )
    feeds_kv = await broker.stream.create_key_value(
        bucket="feeds",
        description="Bucket used to store feed update state",
        ttl=3600 * 24 * 7,
    )
    context.set_global("new_products_kv", new_products_kv)
    context.set_global("feeds_kv", feeds_kv)
