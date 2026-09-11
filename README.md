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

# BLE Test Framework

A Python-based automated testing framework for validating BLE communication with an ESP32 test device using **Pytest** and **Bleak**.

## BLE Device Configuration

The ESP32 test device advertises with the following configuration:

| Configuration             | Value                                  |
| ------------------------- | -------------------------------------- |
| Device Name               | `ESP32-BLE-Test`                       |
| Service UUID              | `12345678-1234-1234-1234-123456789001` |
| Characteristic UUID       | `12345678-1234-1234-1234-123456789002` |
| Characteristic Properties | `READ`, `WRITE`                        |
| Initial Value             | `Hello from ESP32`                     |

## Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
cd ble-test-framework
```

### 2. Create a Virtual Environment

On Windows:

```powershell
python -m venv .venv
```

Activate the virtual environment:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```powershell
pip install -r requirements.txt
```

## Running the Tests

Before running the tests, make sure that:

* The ESP32 is powered on.
* Bluetooth is enabled on the test machine.
* The ESP32 is advertising with the name `ESP32-BLE-Test`.

Run the complete test suite:

```powershell
python -m pytest -v
```

## Test Coverage

The current test suite contains **8 automated tests** covering:

* Device discovery
* BLE connection
* GATT service discovery
* Characteristic discovery
* Characteristic read
* Characteristic write and read-back
* Invalid characteristic handling
* BLE operation after disconnect

## Test Results

A successful test execution looks like:

```text
================ 8 passed in 100.60s ================
```

The exact execution time may vary depending on the operating system, Bluetooth adapter, and ESP32 response time.

## Logging

The framework generates structured logs during test execution.

### Log Format

```text
timestamp | level | logger | message
```

Example:

```text
2026-09-11 22:57:02,973 | INFO | BLEClient | Successfully connected to ESP32-BLE-Test
2026-09-11 22:57:03,003 | INFO | BLEClient | Read successful: bytearray(b'Hello from ESP32')
```

Generated logs are stored in:

```text
logs/
```

The `logs/` directory is excluded from Git using `.gitignore`.

## Architecture

The framework separates BLE communication logic from the test cases.

```text
pytest test cases
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
 GATT Service / Characteristic
```

### Components

* **Pytest** — Test execution and test organization
* **BLEClient** — Reusable BLE communication layer
* **Bleak** — Python BLE communication library
* **Windows Bluetooth** — Bluetooth interface on the test machine
* **ESP32** — Physical BLE test device

Separating the BLE communication layer from the test cases allows `BLEClient` to be reused across multiple test scenarios.

## Negative Testing

The framework also validates expected BLE failure scenarios rather than testing only successful operations.

Current negative tests include:

### Invalid Characteristic

Attempts to read from an invalid characteristic UUID and verifies that the operation fails as expected.

### Operation After Disconnect

Attempts a characteristic operation after the BLE device has been disconnected and verifies that the framework handles the failure correctly.

These tests help ensure that the framework handles invalid BLE operations reliably.

## Continuous Integration

GitHub Actions can be used to execute software-level tests automatically whenever code changes are pushed to the repository.

However, physical BLE hardware testing requires:

* A machine with Bluetooth hardware
* Access to the ESP32 device
* A suitable BLE environment

GitHub-hosted runners cannot directly access a user's physical ESP32 device.

For future hardware-in-the-loop (HIL) testing, a **Linux self-hosted runner with BLE hardware** can be used.

## Future Improvements

Potential improvements include:

* Parametrized BLE test cases
* More specific exception assertions
* Test result reporting
* HTML test reports
* GitHub Actions CI workflow
* Linux BLE test environment
* Hardware-in-the-loop testing
* Additional positive and negative test scenarios

## Project Structure

The expected repository structure is:

```text
ble-test-framework/
│
├── README.md
├── .gitignore
├── requirements.txt
├── scan_ble.py
│
├── src/
│   └── ...
│
├── tests/
│   └── ...
│
└── utils/
    └── ...
```

Generated/runtime files should not be committed to the repository:

```text
.venv/
logs/
__pycache__/
.pytest_cache/
```

## Git Status Verification

After setting up the project, run:

```powershell
git status
```

You should see the project files, such as:

```text
README.md
.gitignore
requirements.txt
scan_ble.py
src/
tests/
utils/
```

Importantly, the following should **not** appear in the Git status output:

```text
.venv/
logs/
__pycache__/
.pytest_cache/
```

This confirms that environment files, generated logs, Python cache files, and Pytest cache files are correctly excluded using `.gitignore`.

## Author

**Akshay**
