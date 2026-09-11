import pytest

from src.ble_client import BLEClient


CHARACTERISTIC_UUID = "12345678-1234-1234-1234-123456789002"

@pytest.mark.hardware
@pytest.mark.asyncio
async def test_characteristic_write_and_read_back(
    ble_client: BLEClient
):

    test_value = b"pytest BLE test"

    await ble_client.write_characteristic(
        CHARACTERISTIC_UUID,
        test_value
    )

    result = await ble_client.read_characteristic(
        CHARACTERISTIC_UUID
    )

    assert result == test_value