"""Root conftest file with shared fixtures."""
import pytest
import logging
import os
from pathlib import Path
from datetime import datetime
from playwright.sync_api import Page, BrowserContext
from config.base_config import get_config


# Configure logging
def setup_logging():
    """Setup logging configuration."""
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    
    log_file = log_dir / f"test_run_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )


setup_logging()


@pytest.fixture(scope="session")
def config():
    """Get test configuration."""
    return get_config()


@pytest.fixture(scope="session")
def browser_context_args(config):
    """Browser context arguments."""
    return {
        "viewport": {
            "width": config.VIEWPORT_WIDTH,
            "height": config.VIEWPORT_HEIGHT
        },
        "ignore_https_errors": True,
        "base_url": config.BASE_URL
    }


@pytest.fixture(scope="function")
def context(new_context, config):
    """Create a new browser context for each test via pytest-playwright wrapper."""
    # Create downloads directory
    download_dir = Path(config.DOWNLOAD_DIR)
    download_dir.mkdir(parents=True, exist_ok=True)
    
    # Use pytest-playwright's new_context fixture so trace/video/screenshot
    # recording hooks are attached to this context.
    context = new_context(accept_downloads=True)
    
    yield context
    context.close()


@pytest.fixture(scope="function")
def page(context: BrowserContext) -> Page:
    """Create a new page for each test."""
    page = context.new_page()
    
    # Set default timeout
    page.set_default_timeout(30000)
    page.set_default_navigation_timeout(30000)
    
    yield page
    page.close()


@pytest.fixture(scope="function")
def screenshot_on_failure(request, page: Page, config):
    """Take screenshot on test failure."""
    yield
    
    if request.node.rep_call.failed if hasattr(request.node, 'rep_call') else False:
        # Create screenshots directory
        screenshot_dir = Path(config.SCREENSHOT_DIR)
        screenshot_dir.mkdir(parents=True, exist_ok=True)
        
        # Generate screenshot filename
        test_name = request.node.name
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        screenshot_file = screenshot_dir / f"{test_name}_{timestamp}.png"
        
        # Take screenshot
        page.screenshot(path=str(screenshot_file), full_page=True)
        logging.info(f"Screenshot saved: {screenshot_file}")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook to make test results available to fixtures."""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)


# Markers for test organization
def pytest_configure(config):
    """Register custom markers."""
    config.addinivalue_line("markers", "smoke: Smoke tests")
    config.addinivalue_line("markers", "regression: Regression tests")
    config.addinivalue_line("markers", "elements: Elements module tests")
    config.addinivalue_line("markers", "text_box: Text Box tests")
    config.addinivalue_line("markers", "check_box: Check Box tests")
    config.addinivalue_line("markers", "radio_button: Radio Button tests")
    config.addinivalue_line("markers", "web_tables: Web Tables tests")
    config.addinivalue_line("markers", "buttons: Buttons tests")
    config.addinivalue_line("markers", "links: Links tests")
    config.addinivalue_line("markers", "broken_links: Broken Links tests")
    config.addinivalue_line("markers", "upload_download: Upload Download tests")
    config.addinivalue_line("markers", "dynamic_properties: Dynamic Properties tests")
