"""Base configuration for DemoQA test automation."""
import os
from dataclasses import dataclass
from typing import Optional


@dataclass
class BaseConfig:
    """Base configuration class."""
    
    # Application URLs
    BASE_URL: str = "https://demoqa.com"
    
    # Element URLs
    TEXT_BOX_URL: str = f"{BASE_URL}/text-box"
    CHECK_BOX_URL: str = f"{BASE_URL}/checkbox"
    RADIO_BUTTON_URL: str = f"{BASE_URL}/radio-button"
    WEB_TABLES_URL: str = f"{BASE_URL}/webtables"
    BUTTONS_URL: str = f"{BASE_URL}/buttons"
    LINKS_URL: str = f"{BASE_URL}/links"
    BROKEN_LINKS_URL: str = f"{BASE_URL}/broken"
    UPLOAD_DOWNLOAD_URL: str = f"{BASE_URL}/upload-download"
    DYNAMIC_PROPERTIES_URL: str = f"{BASE_URL}/dynamic-properties"
    
    # Timeouts
    DEFAULT_TIMEOUT: int = 30000
    NAVIGATION_TIMEOUT: int = 30000
    ELEMENT_TIMEOUT: int = 10000
    
    # Browser settings
    HEADLESS: bool = os.getenv("HEADLESS", "False").lower() == "true"
    BROWSER: str = os.getenv("BROWSER", "chromium")
    VIEWPORT_WIDTH: int = 1920
    VIEWPORT_HEIGHT: int = 1080
    
    # Test data paths
    TEST_DATA_DIR: str = os.path.join(os.path.dirname(__file__), "..", "test_data")
    UPLOAD_FILES_DIR: str = os.path.join(TEST_DATA_DIR, "files")
    DOWNLOAD_DIR: str = os.path.join(os.path.dirname(__file__), "..", "downloads")
    
    # Logging
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    LOG_DIR: str = os.path.join(os.path.dirname(__file__), "..", "logs")
    
    # Screenshots
    SCREENSHOT_ON_FAILURE: bool = True
    SCREENSHOT_DIR: str = os.path.join(os.path.dirname(__file__), "..", "reports", "screenshots")


def get_config() -> BaseConfig:
    """Get configuration instance."""
    return BaseConfig()
