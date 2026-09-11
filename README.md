# Bluetooth Test Automation Framework

A Python-based Bluetooth Low Energy (BLE) test automation framework using
`pytest` and `Bleak` to validate BLE device discovery, connectivity,
GATT services, characteristics, read/write operations, and negative test cases.

## Project Overview

This project automates functional and negative testing of an ESP32 BLE device.

The framework communicates with an ESP32-WROOM-32 configured as a BLE GATT
server and validates its behavior through automated Python tests.

## Technologies Used

- Python 3.11
- pytest
- pytest-asyncio
- Bleak
- Bluetooth Low Energy (BLE)
- ESP32-WROOM-32
- Git
- GitHub
- GitHub Actions
- Windows development environment

## Features

- BLE device discovery
- BLE connection and disconnection validation
- GATT service discovery
- GATT characteristic validation
- Characteristic read testing
- Characteristic write testing
- Write/read-back validation
- Negative testing
- Reusable pytest fixtures
- Asynchronous BLE communication
- Structured test logging
- Regression test execution with pytest

## Project Structure

```text
ble-test-framework/
│
├── src/
│   ├── __init__.py
│   └── ble_client.py
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_discovery.py
│   ├── test_connection.py
│   ├── test_services.py
│   ├── test_characteristics.py
│   ├── test_read.py
│   ├── test_write.py
│   └── test_negative.py
│
├── utils/
│   └── logger.py
│
├── scan_ble.py
├── requirements.txt
├── .gitignore
└── README.md