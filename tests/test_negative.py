import pytest
from bleak.exc import BleakCharacteristicNotFoundError

from src.ble_client import BLEClient


INVALID_CHARACTERISTIC_UUIDS = [
    "12345678-1234-1234-1234-999999999999",
    "00000000-0000-0000-0000-000000000000",
    "12345678-1234-1234-1234-123456789003",
]

VALID_CHARACTERISTIC_UUID = (
    "12345678-1234-1234-1234-123456789002"
)

@pytest.mark.hardware
@pytest.mark.asyncio
@pytest.mark.parametrize(
    "characteristic_uuid",
    INVALID_CHARACTERISTIC_UUIDS,
)
async def test_read_invalid_characteristic(
    ble_client: BLEClient,
    characteristic_uuid: str,
):
    with pytest.raises(BleakCharacteristicNotFoundError):
        await ble_client.read_characteristic(characteristic_uuid)

@pytest.mark.hardware
@pytest.mark.asyncio
async def test_read_after_disconnect(ble_client: BLEClient):
    await ble_client.disconnect()

    with pytest.raises(RuntimeError, match="BLE client is not connected"):
        await ble_client.read_characteristic(
            VALID_CHARACTERISTIC_UUID
        )