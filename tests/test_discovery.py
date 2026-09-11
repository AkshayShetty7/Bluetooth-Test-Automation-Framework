import pytest
from bleak import BleakScanner


DEVICE_NAME = "ESP32-BLE-Test"

@pytest.mark.hardware
@pytest.mark.asyncio
async def test_esp32_is_discoverable():
    devices = await BleakScanner.discover(timeout=10)

    device_names = [device.name for device in devices]

    assert DEVICE_NAME in device_names, (
        f"{DEVICE_NAME} was not found. "
        f"Discovered devices: {device_names}"
    )