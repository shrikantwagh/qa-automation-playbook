"""Page object for Buttons page."""
from pages.base_page import BasePage
from playwright.sync_api import Page


class ButtonsPage(BasePage):
    """Page object for DemoQA Buttons page."""
    
    # Page URL
    PAGE_URL = "/buttons"
    
    # Locators
    DOUBLE_CLICK_BUTTON = "#doubleClickBtn"
    RIGHT_CLICK_BUTTON = "#rightClickBtn"
    DYNAMIC_CLICK_BUTTON = "button:has-text('Click Me')"
    
    # Message locators
    DOUBLE_CLICK_MESSAGE = "#doubleClickMessage"
    RIGHT_CLICK_MESSAGE = "#rightClickMessage"
    DYNAMIC_CLICK_MESSAGE = "#dynamicClickMessage"
    
    def __init__(self, page: Page):
        super().__init__(page)
    
    def navigate_to_page(self):
        """Navigate to Buttons page."""
        self.navigate(self.PAGE_URL)
    
    def double_click_button(self):
        """Perform double click on double click button."""
        self.logger.info("Double clicking on button")
        self.double_click(self.DOUBLE_CLICK_BUTTON)
    
    def right_click_button(self):
        """Perform right click on right click button."""
        self.logger.info("Right clicking on button")
        self.right_click(self.RIGHT_CLICK_BUTTON)
    
    def click_dynamic_button(self):
        """Click on dynamic click me button."""
        self.logger.info("Clicking on dynamic button")
        self.click(self.DYNAMIC_CLICK_BUTTON)
    
    def get_double_click_message(self) -> str:
        """Get double click message text."""
        if not self.is_visible(self.DOUBLE_CLICK_MESSAGE, timeout=2000):
            return ""
        return self.get_text(self.DOUBLE_CLICK_MESSAGE)
    
    def get_right_click_message(self) -> str:
        """Get right click message text."""
        if not self.is_visible(self.RIGHT_CLICK_MESSAGE, timeout=2000):
            return ""
        return self.get_text(self.RIGHT_CLICK_MESSAGE)
    
    def get_dynamic_click_message(self) -> str:
        """Get dynamic click message text."""
        if not self.is_visible(self.DYNAMIC_CLICK_MESSAGE, timeout=2000):
            return ""
        return self.get_text(self.DYNAMIC_CLICK_MESSAGE)
    
    def is_double_click_message_displayed(self) -> bool:
        """Check if double click message is displayed."""
        return self.is_visible(self.DOUBLE_CLICK_MESSAGE, timeout=2000)
    
    def is_right_click_message_displayed(self) -> bool:
        """Check if right click message is displayed."""
        return self.is_visible(self.RIGHT_CLICK_MESSAGE, timeout=2000)
    
    def is_dynamic_click_message_displayed(self) -> bool:
        """Check if dynamic click message is displayed."""
        return self.is_visible(self.DYNAMIC_CLICK_MESSAGE, timeout=2000)
