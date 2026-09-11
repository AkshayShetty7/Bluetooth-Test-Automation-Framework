from bleak import BleakClient, BleakScanner
from utils.logger import get_logger


DEVICE_NAME = "ESP32-BLE-Test"


class BLEClient:

    logger = get_logger("BLEClient")

    def __init__(self, device_name=DEVICE_NAME):
        self.device_name = device_name
        self.device = None
        self.client = None

    async def discover(self, retries=3, timeout=10):
        """Discover the target BLE device with retry support."""

        for attempt in range(1, retries + 1):
            self.logger.info(
                "BLE discovery attempt %d/%d for device: %s",
                attempt,
                retries,
                self.device_name,
            )

            devices = await BleakScanner.discover(timeout=timeout)

            for device in devices:
                self.logger.info(
                    "Discovered device: %s",
                    device.name,
                )

                if device.name == self.device_name:
                    self.device = device

                    self.logger.info(
                        "Target device found: %s",
                        device.name,
                    )

                    return device

            self.logger.warning(
                "BLE device '%s' was not found on attempt %d/%d",
                self.device_name,
                attempt,
                retries,
            )

        self.logger.error(
            "BLE device '%s' was not found after %d attempts",
            self.device_name,
            retries,
        )

        raise RuntimeError(
            f"BLE device '{self.device_name}' was not found "
            f"after {retries} attempts"
        )

    async def connect(self):
        """Discover and connect to the target BLE device."""

        if self.device is None:
            await self.discover()

        self.logger.info(
            "Connecting to %s",
            self.device.name,
        )

        self.client = BleakClient(self.device)

        await self.client.connect()

        if not self.client.is_connected:
            self.logger.error(
                "Failed to connect to %s",
                self.device.name,
            )

            raise RuntimeError(
                "Failed to connect to ESP32"
            )

        self.logger.info(
            "Successfully connected to %s",
            self.device.name,
        )

        return True

    async def disconnect(self):
        """Disconnect from the BLE device."""

        if self.client and self.client.is_connected:
            self.logger.info(
                "Disconnecting from %s",
                self.device.name,
            )

            await self.client.disconnect()

            self.logger.info(
                "Disconnected successfully"
            )

    async def get_services(self):
        """Return the discovered GATT services."""

        if not self.client or not self.client.is_connected:
            raise RuntimeError(
                "BLE client is not connected"
            )

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
            characteristic_uuid,
        )

        data = await self.client.read_gatt_char(
            characteristic_uuid
        )

        self.logger.info(
            "Read successful: %s",
            data,
        )

        return data

    async def write_characteristic(
        self,
        characteristic_uuid,
        value,
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
            value,
        )

        await self.client.write_gatt_char(
            characteristic_uuid,
            value,
        )

        self.logger.info(
            "Write successful",
        )