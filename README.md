# Bluetooth Test Automation Framework

Python-based BLE test automation framework using **Pytest** and **Bleak** for validating an ESP32 BLE GATT server.

## Overview

The framework automates functional and negative testing for an **ESP32-WROOM-32** BLE device, covering discovery, connection, GATT validation, characteristic operations, and error handling.

## Tech Stack

* Python 3.11
* Pytest
* pytest-asyncio
* Bleak
* ESP32-WROOM-32
* Bluetooth Low Energy (BLE)
* Windows
* Git / GitHub

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
```

## BLE Device Configuration

| Configuration       | Value                                  |
| ------------------- | -------------------------------------- |
| Device Name         | `ESP32-BLE-Test`                       |
| Service UUID        | `12345678-1234-1234-1234-123456789001` |
| Characteristic UUID | `12345678-1234-1234-1234-123456789002` |
| Properties          | `READ`, `WRITE`                        |
| Initial Value       | `Hello from ESP32`                     |


## Test Coverage

The test suite currently contains **8 automated tests** covering:

* Device discovery
* BLE connection
* GATT service discovery
* Characteristic discovery
* Characteristic read
* Characteristic write and read-back
* Invalid characteristic handling
* Operations after disconnect


## Architecture

```text
Pytest Tests
     │
     ▼
 BLEClient
     │
     ▼
   Bleak
     │
     ▼
Windows Bluetooth
     │
     ▼
 ESP32 BLE
     │
     ▼
GATT Server
```

`BLEClient` provides the reusable BLE communication layer, while the `tests/` package contains the test cases.

## Negative Testing

The framework validates expected failure scenarios, including:

* Accessing an invalid characteristic UUID
* Performing characteristic operations after disconnect

These tests verify that invalid BLE operations are handled correctly.

## Logging

Structured logs are generated during test execution.


## Continuous Integration

Software-level tests can be executed through **GitHub Actions**.

Physical BLE testing requires Bluetooth hardware and access to the ESP32. For hardware-in-the-loop testing, a **self-hosted Linux runner with BLE hardware** can be used.




