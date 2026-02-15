"""Page object for Links page."""
from pages.base_page import BasePage
from playwright.sync_api import Page


class LinksPage(BasePage):
    """Page object for DemoQA Links page."""
    
    # Page URL
    PAGE_URL = "/links"
    
    # Locators - Simple Links
    HOME_LINK = "#simpleLink"
    DYNAMIC_HOME_LINK = "#dynamicLink"
    
    # Locators - API Call Links
    CREATED_LINK = "#created"
    NO_CONTENT_LINK = "#no-content"
    MOVED_LINK = "#moved"
    BAD_REQUEST_LINK = "#bad-request"
    UNAUTHORIZED_LINK = "#unauthorized"
    FORBIDDEN_LINK = "#forbidden"
    NOT_FOUND_LINK = "#invalid-url"
    
    # Response message
    LINK_RESPONSE = "#linkResponse"
    
    def __init__(self, page: Page):
        super().__init__(page)
    
    def navigate_to_page(self):
        """Navigate to Links page."""
        self.navigate(self.PAGE_URL)
    
    def click_home_link(self):
        """Click Home link (opens new tab)."""
        self.logger.info("Clicking Home link")
        self.click(self.HOME_LINK)
    
    def click_dynamic_home_link(self):
        """Click dynamic Home link (opens new tab)."""
        self.logger.info("Clicking Dynamic Home link")
        self.click(self.DYNAMIC_HOME_LINK)
    
    def click_created_link(self):
        """Click Created link (API call)."""
        self.logger.info("Clicking Created link")
        self.click(self.CREATED_LINK)
    
    def click_no_content_link(self):
        """Click No Content link (API call)."""
        self.logger.info("Clicking No Content link")
        self.click(self.NO_CONTENT_LINK)
    
    def click_moved_link(self):
        """Click Moved link (API call)."""
        self.logger.info("Clicking Moved link")
        self.click(self.MOVED_LINK)
    
    def click_bad_request_link(self):
        """Click Bad Request link (API call)."""
        self.logger.info("Clicking Bad Request link")
        self.click(self.BAD_REQUEST_LINK)
    
    def click_unauthorized_link(self):
        """Click Unauthorized link (API call)."""
        self.logger.info("Clicking Unauthorized link")
        self.click(self.UNAUTHORIZED_LINK)
    
    def click_forbidden_link(self):
        """Click Forbidden link (API call)."""
        self.logger.info("Clicking Forbidden link")
        self.click(self.FORBIDDEN_LINK)
    
    def click_not_found_link(self):
        """Click Not Found link (API call)."""
        self.logger.info("Clicking Not Found link")
        self.click(self.NOT_FOUND_LINK)
    
    def get_response_message(self) -> str:
        """Get API response message."""
        self.wait_for_element_visible(self.LINK_RESPONSE, timeout=5000)
        return self.get_text(self.LINK_RESPONSE)
    
    def is_response_displayed(self) -> bool:
        """Check if response message is displayed."""
        return self.is_visible(self.LINK_RESPONSE, timeout=5000)
    
    def get_link_href(self, selector: str) -> str:
        """Get href attribute of a link."""
        return self.get_attribute(selector, "href") or ""
