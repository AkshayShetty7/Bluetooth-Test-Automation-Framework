import pytest

from src.ble_client import BLEClient


@pytest.mark.hardware
@pytest.mark.asyncio
async def test_esp32_connection():
    client = BLEClient()

    try:
        connected = await client.connect()

        assert connected is True
        assert client.client.is_connected is True

    finally:
        await client.disconnect()