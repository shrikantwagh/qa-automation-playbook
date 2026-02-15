"""Page object for Text Box page."""
from pages.base_page import BasePage
from playwright.sync_api import Page


class TextBoxPage(BasePage):
    """Page object for DemoQA Text Box page."""
    
    # Page URL
    PAGE_URL = "/text-box"
    
    # Locators
    FULL_NAME_INPUT = "#userName"
    EMAIL_INPUT = "#userEmail"
    CURRENT_ADDRESS_TEXTAREA = "#currentAddress"
    PERMANENT_ADDRESS_TEXTAREA = "#permanentAddress"
    SUBMIT_BUTTON = "#submit"
    
    # Output locators
    OUTPUT_CONTAINER = "#output"
    OUTPUT_NAME = "#name"
    OUTPUT_EMAIL = "#email"
    OUTPUT_CURRENT_ADDRESS = "p#currentAddress"
    OUTPUT_PERMANENT_ADDRESS = "p#permanentAddress"
    
    def __init__(self, page: Page):
        super().__init__(page)
    
    def navigate_to_page(self):
        """Navigate to Text Box page."""
        self.navigate(self.PAGE_URL)
        self.scroll_to_element(self.FULL_NAME_INPUT)
    
    def fill_full_name(self, name: str):
        """Fill full name field."""
        self.logger.info(f"Filling full name: {name}")
        self.fill(self.FULL_NAME_INPUT, name)
    
    def fill_email(self, email: str):
        """Fill email field."""
        self.logger.info(f"Filling email: {email}")
        self.fill(self.EMAIL_INPUT, email)
    
    def fill_current_address(self, address: str):
        """Fill current address field."""
        self.logger.info(f"Filling current address: {address}")
        self.fill(self.CURRENT_ADDRESS_TEXTAREA, address)
    
    def fill_permanent_address(self, address: str):
        """Fill permanent address field."""
        self.logger.info(f"Filling permanent address: {address}")
        self.fill(self.PERMANENT_ADDRESS_TEXTAREA, address)
    
    def click_submit(self):
        """Click submit button."""
        self.logger.info("Clicking submit button")
        self.scroll_to_element(self.SUBMIT_BUTTON)
        self.click(self.SUBMIT_BUTTON)
    
    def submit_form(self, full_name: str, email: str, current_address: str, permanent_address: str):
        """Fill and submit the complete form."""
        self.fill_full_name(full_name)
        self.fill_email(email)
        self.fill_current_address(current_address)
        self.fill_permanent_address(permanent_address)
        self.click_submit()
    
    def is_output_displayed(self) -> bool:
        """Check if output container is displayed."""
        return self.is_visible(self.OUTPUT_CONTAINER)
    
    def get_output_name(self) -> str:
        """Get output name text."""
        return self.get_text(self.OUTPUT_NAME).replace("Name:", "").strip()
    
    def get_output_email(self) -> str:
        """Get output email text."""
        return self.get_text(self.OUTPUT_EMAIL).replace("Email:", "").strip()
    
    def get_output_current_address(self) -> str:
        """Get output current address text."""
        text = self.get_text(self.OUTPUT_CURRENT_ADDRESS)
        return text.replace("Current Address :", "").strip()
    
    def get_output_permanent_address(self) -> str:
        """Get output permanent address text."""
        text = self.get_text(self.OUTPUT_PERMANENT_ADDRESS)
        return text.replace("Permananet Address :", "").strip()
    
    def get_all_output_data(self) -> dict:
        """Get all output data as dictionary."""
        return {
            "name": self.get_output_name(),
            "email": self.get_output_email(),
            "current_address": self.get_output_current_address(),
            "permanent_address": self.get_output_permanent_address()
        }
    
    def clear_all_fields(self):
        """Clear all input fields."""
        self.page.locator(self.FULL_NAME_INPUT).clear()
        self.page.locator(self.EMAIL_INPUT).clear()
        self.page.locator(self.CURRENT_ADDRESS_TEXTAREA).clear()
        self.page.locator(self.PERMANENT_ADDRESS_TEXTAREA).clear()
