import asyncio
from bleak import BleakScanner


async def main():
    print("Scanning for BLE devices...")
    print("Please wait 10 seconds...\n")

    devices = await BleakScanner.discover(timeout=10)

    print("\nDiscovered devices:")
    print("-" * 50)

    for device in devices:
        print(f"Name    : {device.name}")
        print(f"Address : {device.address}")
        print("-" * 50)


if __name__ == "__main__":
    asyncio.run(main())