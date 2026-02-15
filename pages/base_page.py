"""Base page object with common methods for all pages."""
from playwright.sync_api import Page, expect, Locator
from typing import Optional, List
import logging


class BasePage:
    """Base page object containing common functionality."""
    
    def __init__(self, page: Page, base_url: str = "https://demoqa.com"):
        self.page = page
        self.base_url = base_url
        self.logger = logging.getLogger(self.__class__.__name__)
    
    def navigate(self, path: str = ""):
        """Navigate to a specific path."""
        url = f"{self.base_url}{path}" if path else self.base_url
        self.logger.info(f"Navigating to: {url}")
        self.page.goto(url, wait_until="domcontentloaded")
    
    def wait_for_page_load(self, timeout: int = 30000):
        """Wait for page to be fully loaded."""
        self.page.wait_for_load_state("networkidle", timeout=timeout)
    
    def click(self, selector: str, **kwargs):
        """Click on element with optional parameters."""
        self.logger.debug(f"Clicking element: {selector}")
        self.page.click(selector, **kwargs)
    
    def fill(self, selector: str, text: str, **kwargs):
        """Fill input field."""
        self.logger.debug(f"Filling {selector} with: {text}")
        self.page.fill(selector, text, **kwargs)
    
    def clear_and_fill(self, selector: str, text: str):
        """Clear field and fill with text."""
        self.page.locator(selector).clear()
        self.fill(selector, text)
    
    def get_text(self, selector: str) -> str:
        """Get text content of element."""
        return self.page.locator(selector).text_content() or ""
    
    def get_all_text(self, selector: str) -> List[str]:
        """Get text content from all matching elements."""
        return self.page.locator(selector).all_text_contents()
    
    def get_attribute(self, selector: str, attribute: str) -> Optional[str]:
        """Get attribute value from element."""
        return self.page.locator(selector).get_attribute(attribute)
    
    def is_visible(self, selector: str, timeout: int = 5000) -> bool:
        """Check if element is visible."""
        try:
            return self.page.locator(selector).is_visible(timeout=timeout)
        except Exception:
            return False
    
    def is_enabled(self, selector: str) -> bool:
        """Check if element is enabled."""
        return self.page.locator(selector).is_enabled()
    
    def is_checked(self, selector: str) -> bool:
        """Check if checkbox/radio is checked."""
        return self.page.locator(selector).is_checked()
    
    def wait_for_selector(self, selector: str, timeout: int = 30000):
        """Wait for selector to appear."""
        self.page.wait_for_selector(selector, timeout=timeout)
    
    def wait_for_element_visible(self, selector: str, timeout: int = 30000):
        """Wait for element to be visible."""
        self.page.locator(selector).wait_for(state="visible", timeout=timeout)
    
    def wait_for_element_hidden(self, selector: str, timeout: int = 30000):
        """Wait for element to be hidden."""
        self.page.locator(selector).wait_for(state="hidden", timeout=timeout)
    
    def scroll_to_element(self, selector: str):
        """Scroll element into view."""
        self.page.locator(selector).scroll_into_view_if_needed()
    
    def get_locator(self, selector: str) -> Locator:
        """Get Playwright locator object."""
        return self.page.locator(selector)
    
    def take_screenshot(self, filename: str):
        """Take screenshot of current page."""
        self.page.screenshot(path=filename, full_page=True)
        self.logger.info(f"Screenshot saved: {filename}")
    
    def get_page_title(self) -> str:
        """Get page title."""
        return self.page.title()
    
    def get_current_url(self) -> str:
        """Get current page URL."""
        return self.page.url
    
    def hover(self, selector: str):
        """Hover over element."""
        self.page.locator(selector).hover()
    
    def double_click(self, selector: str):
        """Double click on element."""
        self.page.locator(selector).dblclick()
    
    def right_click(self, selector: str):
        """Right click on element."""
        self.page.locator(selector).click(button="right")
    
    def select_option(self, selector: str, value: str):
        """Select option from dropdown."""
        self.page.locator(selector).select_option(value)
    
    def upload_file(self, selector: str, file_path: str):
        """Upload file to input element."""
        self.page.locator(selector).set_input_files(file_path)
    
    def press_key(self, key: str):
        """Press keyboard key."""
        self.page.keyboard.press(key)
    
    def execute_script(self, script: str):
        """Execute JavaScript."""
        return self.page.evaluate(script)
    
    def remove_element(self, selector: str):
        """Remove element using JavaScript."""
        self.page.evaluate(f'document.querySelector("{selector}").remove()')
