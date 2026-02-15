"""Page object for Radio Button page."""
from pages.base_page import BasePage
from playwright.sync_api import Page


class RadioButtonPage(BasePage):
    """Page object for DemoQA Radio Button page."""
    
    # Page URL
    PAGE_URL = "/radio-button"
    
    # Locators
    YES_RADIO = "label[for='yesRadio']"
    IMPRESSIVE_RADIO = "label[for='impressiveRadio']"
    NO_RADIO = "label[for='noRadio']"
    
    # Input elements (actual radio inputs)
    YES_RADIO_INPUT = "#yesRadio"
    IMPRESSIVE_RADIO_INPUT = "#impressiveRadio"
    NO_RADIO_INPUT = "#noRadio"
    
    # Result
    RESULT_TEXT = ".mt-3"
    SUCCESS_TEXT = ".text-success"
    
    def __init__(self, page: Page):
        super().__init__(page)
    
    def navigate_to_page(self):
        """Navigate to Radio Button page."""
        self.navigate(self.PAGE_URL)
    
    def select_yes(self):
        """Select Yes radio button."""
        self.logger.info("Selecting Yes radio button")
        self.click(self.YES_RADIO)
    
    def select_impressive(self):
        """Select Impressive radio button."""
        self.logger.info("Selecting Impressive radio button")
        self.click(self.IMPRESSIVE_RADIO)
    
    def select_no(self):
        """Select No radio button."""
        self.logger.info("Attempting to select No radio button")
        # Note: This button is disabled in the actual application
        if self.is_enabled(self.NO_RADIO_INPUT):
            self.click(self.NO_RADIO)
        else:
            self.logger.warning("No radio button is disabled")
    
    def is_yes_selected(self) -> bool:
        """Check if Yes radio is selected."""
        return self.is_checked(self.YES_RADIO_INPUT)
    
    def is_impressive_selected(self) -> bool:
        """Check if Impressive radio is selected."""
        return self.is_checked(self.IMPRESSIVE_RADIO_INPUT)
    
    def is_no_enabled(self) -> bool:
        """Check if No radio button is enabled."""
        return self.is_enabled(self.NO_RADIO_INPUT)
    
    def get_result_text(self) -> str:
        """Get the result text displayed."""
        if not self.is_visible(self.SUCCESS_TEXT, timeout=2000):
            return ""
        return self.get_text(self.SUCCESS_TEXT)
    
    def is_result_displayed(self) -> bool:
        """Check if result is displayed."""
        return self.is_visible(self.RESULT_TEXT)
