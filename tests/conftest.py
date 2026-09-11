import pytest_asyncio

from src.ble_client import BLEClient


@pytest_asyncio.fixture
async def ble_client():
    client = BLEClient()

    await client.connect()

    yield client

    await client.disconnect()