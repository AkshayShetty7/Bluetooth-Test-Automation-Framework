import pytest

from src.ble_client import BLEClient


@pytest.mark.asyncio
async def test_client_initial_state():
    client = BLEClient()

    assert client.device is None
    assert client.client is None


@pytest.mark.asyncio
async def test_read_requires_connection():
    client = BLEClient()

    with pytest.raises(
        RuntimeError,
        match="BLE client is not connected",
    ):
        await client.read_characteristic(
            "12345678-1234-1234-1234-123456789002"
        )


@pytest.mark.asyncio
async def test_write_requires_connection():
    client = BLEClient()

    with pytest.raises(
        RuntimeError,
        match="BLE client is not connected",
    ):
        await client.write_characteristic(
            "12345678-1234-1234-1234-123456789002",
            b"test",
        )


@pytest.mark.asyncio
async def test_services_require_connection():
    client = BLEClient()

    with pytest.raises(
        RuntimeError,
        match="BLE client is not connected",
    ):
        await client.get_services()