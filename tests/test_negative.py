import pytest

from src.ble_client import BLEClient


INVALID_CHARACTERISTIC_UUID = (
    "12345678-1234-1234-1234-999999999999"
)


@pytest.mark.asyncio
async def test_read_invalid_characteristic(
    ble_client: BLEClient
):

    with pytest.raises(Exception):
        await ble_client.read_characteristic(
            INVALID_CHARACTERISTIC_UUID
        )
        
@pytest.mark.asyncio
async def test_read_after_disconnect(
    ble_client: BLEClient
):

    await ble_client.disconnect()

    with pytest.raises(Exception):
        await ble_client.read_characteristic(
            "12345678-1234-1234-1234-123456789002"
        )