## High Level QA Automation Framework with Python & Playwright

### Create Virtual Environment
```bash
    python -m venv venv
    venv\Scripts\activate               # Windows
    source venv/bin/activate            # Linux/Mac
```

### Install packages
```bash
    pip install -r requirements.txt
```

### Install playwright browsers (chromium, firefox, webkit)
```bash
    playwright install
```

### Run tests
```bash
    pytest
```

### Generate Allure report
```bash
    allure serve reports/allure-results
```