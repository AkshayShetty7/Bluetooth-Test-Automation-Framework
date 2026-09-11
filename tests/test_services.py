import pytest

from src.ble_client import BLEClient


SERVICE_UUID = "12345678-1234-1234-1234-123456789001"


@pytest.mark.asyncio
async def test_esp32_service_exists():

    client = BLEClient()

    try:
        await client.connect()

        services = await client.get_services()

        service_uuids = [
            service.uuid.lower()
            for service in services
        ]

        assert SERVICE_UUID.lower() in service_uuids

    finally:
        await client.disconnect()