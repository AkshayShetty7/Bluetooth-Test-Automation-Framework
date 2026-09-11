import pytest

from src.ble_client import BLEClient


SERVICE_UUID = "12345678-1234-1234-1234-123456789001"
CHARACTERISTIC_UUID = "12345678-1234-1234-1234-123456789002"

@pytest.mark.hardware
@pytest.mark.asyncio
async def test_esp32_characteristic_exists(
    ble_client: BLEClient
):

    service = ble_client.client.services.get_service(
        SERVICE_UUID
    )

    assert service is not None

    characteristic = service.get_characteristic(
        CHARACTERISTIC_UUID
    )

    assert characteristic is not None