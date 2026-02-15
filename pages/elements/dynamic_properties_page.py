"""Page object for Dynamic Properties page."""
from pages.base_page import BasePage
from playwright.sync_api import Page


class DynamicPropertiesPage(BasePage):
    """Page object for DemoQA Dynamic Properties page."""
    
    # Page URL
    PAGE_URL = "/dynamic-properties"
    
    # Locators
    RANDOM_ID_TEXT = "p:has-text('This text has random Id')"
    ENABLE_AFTER_BUTTON = "#enableAfter"
    COLOR_CHANGE_BUTTON = "#colorChange"
    VISIBLE_AFTER_BUTTON = "#visibleAfter"
    
    def __init__(self, page: Page):
        super().__init__(page)
    
    def navigate_to_page(self):
        """Navigate to Dynamic Properties page."""
        self.navigate(self.PAGE_URL)
    
    def is_random_id_text_visible(self) -> bool:
        """Check if random ID text is visible."""
        return self.is_visible(self.RANDOM_ID_TEXT)
    
    def get_random_id_text(self) -> str:
        """Get random ID text content."""
        return self.get_text(self.RANDOM_ID_TEXT)
    
    def is_enable_after_button_enabled(self, timeout: int = 5000) -> bool:
        """Check if 'Enable After 5 Seconds' button is enabled."""
        try:
            self.page.locator(self.ENABLE_AFTER_BUTTON).wait_for(
                state="enabled", 
                timeout=timeout
            )
            return True
        except Exception:
            return False
    
    def click_enable_after_button(self):
        """Click 'Enable After 5 Seconds' button."""
        self.logger.info("Clicking Enable After button")
        # Wait for it to be enabled first
        self.page.locator(self.ENABLE_AFTER_BUTTON).wait_for(state="enabled", timeout=6000)
        self.click(self.ENABLE_AFTER_BUTTON)
    
    def get_color_change_button_color(self) -> str:
        """Get the color of the color change button."""
        return self.get_attribute(self.COLOR_CHANGE_BUTTON, "class") or ""
    
    def wait_for_color_change(self, timeout: int = 5000):
        """Wait for color change button to change color."""
        # The button changes to class containing 'text-danger'
        self.page.locator(f"{self.COLOR_CHANGE_BUTTON}.text-danger").wait_for(
            state="attached",
            timeout=timeout
        )
    
    def is_color_changed(self) -> bool:
        """Check if color has changed (contains text-danger class)."""
        color_class = self.get_color_change_button_color()
        return "text-danger" in color_class
    
    def is_visible_after_button_visible(self, timeout: int = 5000) -> bool:
        """Check if 'Visible After 5 Seconds' button is visible."""
        return self.is_visible(self.VISIBLE_AFTER_BUTTON, timeout=timeout)
    
    def wait_for_visible_after_button(self, timeout: int = 6000):
        """Wait for 'Visible After 5 Seconds' button to appear."""
        self.logger.info("Waiting for Visible After button")
        self.wait_for_element_visible(self.VISIBLE_AFTER_BUTTON, timeout=timeout)
    
    def click_visible_after_button(self):
        """Click 'Visible After 5 Seconds' button."""
        self.logger.info("Clicking Visible After button")
        self.wait_for_visible_after_button()
        self.click(self.VISIBLE_AFTER_BUTTON)
