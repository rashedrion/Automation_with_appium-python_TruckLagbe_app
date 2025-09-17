# TruckLagbe Automation (Improved with POM)

## Requirements
- Python 3.8+
- Appium Server
- Android SDK + Emulator or real device
- TruckLagbe APK (placed in project root as `trucklagbe.apk`)
- Install dependencies:
```bash
pip install -r requirements.txt
```

## Run Tests
Start Appium server first:
```bash
appium
```

Run pytest with HTML report:
```bash
pytest --html=reports/report.html --self-contained-html
```

## Config
Edit `config/config.yaml` for phone number, OTP, and trip details.

## Structure
```
TruckLagbe_Automation_Improved/
├── config/
│   └── config.yaml
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   └── trip_page.py
├── tests/
│   ├── conftest.py
│   └── test_trip.py
├── reports/
├── requirements.txt
├── README.md
└── trucklagbe.apk
```
