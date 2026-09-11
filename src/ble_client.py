import asyncio
from bleak import BleakClient, BleakScanner
from utils.logger import get_logger


DEVICE_NAME = "ESP32-BLE-Test"


class BLEClient:

    logger = get_logger("BLEClient")

    def __init__(self, device_name=DEVICE_NAME):
        self.device_name = device_name
        self.device = None
        self.client = None

    async def discover(self):
        """Discover the ESP32 BLE device."""

        self.logger.info(
            "Scanning for BLE device: %s",
            self.device_name
        )

        devices = await BleakScanner.discover(timeout=10)

        for device in devices:

            self.logger.info(
                "Discovered device: %s",
                device.name
            )

            if device.name == self.device_name:
                self.device = device

                self.logger.info(
                    "Target device found: %s",
                    device.name
                )

                return device

        self.logger.error(
            "BLE device '%s' was not found",
            self.device_name
        )

        raise RuntimeError(
            f"BLE device '{self.device_name}' was not found"
        )

    async def connect(self):
        """Discover and connect to the ESP32."""

        if self.device is None:
            await self.discover()

        self.logger.info(
            "Connecting to %s",
            self.device.name
        )

        self.client = BleakClient(self.device)

        await self.client.connect()

        if not self.client.is_connected:
            self.logger.error(
                "Failed to connect to %s",
                self.device.name
            )

            raise RuntimeError(
                "Failed to connect to ESP32"
            )

        self.logger.info(
            "Successfully connected to %s",
            self.device.name
        )

        return True

    async def disconnect(self):
        """Disconnect from the ESP32."""

        if self.client and self.client.is_connected:

            self.logger.info(
                "Disconnecting from %s",
                self.device.name
            )

            await self.client.disconnect()

            self.logger.info(
                "Disconnected successfully"
            )

    async def get_services(self):
        """Return GATT services discovered by the device."""

        if not self.client or not self.client.is_connected:
            raise RuntimeError("BLE client is not connected")

        return self.client.services

    async def read_characteristic(self, characteristic_uuid):
        """Read a BLE characteristic."""

        if not self.client or not self.client.is_connected:
            self.logger.error(
                "Read attempted while BLE client is disconnected"
            )

            raise RuntimeError(
                "BLE client is not connected"
            )

        self.logger.info(
            "Reading characteristic: %s",
            characteristic_uuid
        )

        data = await self.client.read_gatt_char(
            characteristic_uuid
        )

        self.logger.info(
            "Read successful: %s",
            data
        )

        return data

    async def write_characteristic(
    self,
    characteristic_uuid,
    value
):
        """Write data to a BLE characteristic."""

        if not self.client or not self.client.is_connected:
            self.logger.error(
                "Write attempted while BLE client is disconnected"
            )

            raise RuntimeError(
                "BLE client is not connected"
            )

        self.logger.info(
            "Writing to characteristic %s: %s",
            characteristic_uuid,
            value
        )

        await self.client.write_gatt_char(
            characteristic_uuid,
            value
        )

        self.logger.info(
            "Write successful"
        )