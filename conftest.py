import json
import pytest
from pathlib import Path
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session", autouse=True)
def config():
    config_file_path = Path(__file__).parent / "config.json"
    with open(config_file_path,'r') as f:
        data = json.load(f)
    return data

@pytest.fixture(scope="session")
def pw_instance():
    with sync_playwright() as pw:
        yield pw

@pytest.fixture(scope="session")
def browser(pw_instance, config):
    browser_type = config.get("browser","chromium")
    headless = config.get("headless",False)
    launch_args = {
        "headless": headless,        
        "args": ["--start-maximized"]
    }
    if browser_type == "chrome":
        browser = pw_instance.chromium.launch(channel="chrome", **launch_args)
    elif browser_type == "msedge":
        browser = pw_instance.chromium.launch(channel="msedge", **launch_args)
    elif browser_type == "firefox":
        browser = pw_instance.firefox.launch(**launch_args)
    else:
        raise ValueError(f"Unsupported browser type: {browser_type}")
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def context(browser):
    context = browser.new_context(no_viewport=True)
    yield context
    context.close()

@pytest.fixture(scope="function", autouse=True)
def page(context,config):
    page = context.new_page()
    page.goto(config["url"])
    yield page
    page.close()