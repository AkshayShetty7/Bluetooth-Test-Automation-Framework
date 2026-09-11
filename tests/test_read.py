import pytest

from src.ble_client import BLEClient


CHARACTERISTIC_UUID = "12345678-1234-1234-1234-123456789002"


@pytest.mark.asyncio
async def test_characteristic_read(
    ble_client: BLEClient
):

    data = await ble_client.read_characteristic(
        CHARACTERISTIC_UUID
    )

    value = data.decode("utf-8")

    assert value == "Hello from ESP32"