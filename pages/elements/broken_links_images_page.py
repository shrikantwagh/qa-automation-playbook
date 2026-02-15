"""Page object for Broken Links - Images page."""
from pages.base_page import BasePage
from playwright.sync_api import Page, Response


class BrokenLinksImagesPage(BasePage):
    """Page object for DemoQA Broken Links - Images page."""
    
    # Page URL
    PAGE_URL = "/broken"
    
    # Locators
    VALID_IMAGE = "img[src='/images/Toolsqa.jpg']"
    BROKEN_IMAGE = "img[src='/images/Toolsqa_1.jpg']"
    VALID_LINK = "a:has-text('Click Here for Valid Link')"
    BROKEN_LINK = "a:has-text('Click Here for Broken Link')"
    
    def __init__(self, page: Page):
        super().__init__(page)
    
    def navigate_to_page(self):
        """Navigate to Broken Links - Images page."""
        self.navigate(self.PAGE_URL)
    
    def is_valid_image_displayed(self) -> bool:
        """Check if valid image is displayed."""
        return self.is_visible(self.VALID_IMAGE)
    
    def is_broken_image_displayed(self) -> bool:
        """Check if broken image element exists (will have broken src)."""
        return self.is_visible(self.BROKEN_IMAGE)
    
    def get_valid_image_src(self) -> str:
        """Get valid image source."""
        return self.get_attribute(self.VALID_IMAGE, "src") or ""
    
    def get_broken_image_src(self) -> str:
        """Get broken image source."""
        return self.get_attribute(self.BROKEN_IMAGE, "src") or ""
    
    def get_image_natural_width(self, selector: str) -> int:
        """Get natural width of image (0 if broken)."""
        script = f"""
            document.querySelector('{selector}').naturalWidth
        """
        return self.execute_script(script)
    
    def is_image_broken(self, selector: str) -> bool:
        """Check if image is broken by checking natural width."""
        try:
            width = self.get_image_natural_width(selector)
            return width == 0
        except Exception:
            return True
    
    def click_valid_link(self):
        """Click valid link."""
        self.logger.info("Clicking valid link")
        self.click(self.VALID_LINK)
    
    def click_broken_link(self):
        """Click broken link."""
        self.logger.info("Clicking broken link")
        self.click(self.BROKEN_LINK)
    
    def get_valid_link_href(self) -> str:
        """Get valid link href."""
        return self.get_attribute(self.VALID_LINK, "href") or ""
    
    def get_broken_link_href(self) -> str:
        """Get broken link href."""
        return self.get_attribute(self.BROKEN_LINK, "href") or ""
    
    def check_link_status(self, url: str) -> int:
        """Check HTTP status code of a URL."""
        self.logger.info(f"Checking status of URL: {url}")
        
        # Use page.request to check the URL status
        response = self.page.request.get(url)
        return response.status
    
    def is_valid_link_working(self) -> bool:
        """Check if valid link returns 200 status."""
        href = self.get_valid_link_href()
        if href:
            status = self.check_link_status(href)
            return status == 200
        return False
    
    def is_broken_link_broken(self) -> bool:
        """Check if broken link returns error status (not 200)."""
        href = self.get_broken_link_href()
        if href:
            status = self.check_link_status(href)
            return status != 200
        return False
