"""Sidebar navigation component for DemoQA."""
from pages.base_page import BasePage
from playwright.sync_api import Page


class SidebarNavigation(BasePage):
    """Component for sidebar navigation menu."""
    
    # Main menu items
    ELEMENTS_MENU = "div.header-text:has-text('Elements')"
    FORMS_MENU = "div.header-text:has-text('Forms')"
    ALERTS_MENU = "div.header-text:has-text('Alerts, Frame & Windows')"
    WIDGETS_MENU = "div.header-text:has-text('Widgets')"
    INTERACTIONS_MENU = "div.header-text:has-text('Interactions')"
    BOOK_STORE_MENU = "div.header-text:has-text('Book Store Application')"
    
    # Elements submenu
    TEXT_BOX_ITEM = "span.text:has-text('Text Box')"
    CHECK_BOX_ITEM = "span.text:has-text('Check Box')"
    RADIO_BUTTON_ITEM = "span.text:has-text('Radio Button')"
    WEB_TABLES_ITEM = "span.text:has-text('Web Tables')"
    BUTTONS_ITEM = "span.text:has-text('Buttons')"
    LINKS_ITEM = "span.text:has-text('Links')"
    BROKEN_LINKS_ITEM = "span.text:has-text('Broken Links - Images')"
    UPLOAD_DOWNLOAD_ITEM = "span.text:has-text('Upload and Download')"
    DYNAMIC_PROPERTIES_ITEM = "span.text:has-text('Dynamic Properties')"
    
    def __init__(self, page: Page):
        super().__init__(page)
    
    def expand_elements_menu(self):
        """Expand Elements menu."""
        self.logger.info("Expanding Elements menu")
        if not self.is_menu_expanded(self.ELEMENTS_MENU):
            self.click(self.ELEMENTS_MENU)
    
    def is_menu_expanded(self, menu_selector: str) -> bool:
        """Check if menu is expanded."""
        # Check if the menu has 'show' class or is visible
        return "show" in (self.get_attribute(menu_selector, "class") or "")
    
    def navigate_to_text_box(self):
        """Navigate to Text Box page."""
        self.expand_elements_menu()
        self.click(self.TEXT_BOX_ITEM)
    
    def navigate_to_check_box(self):
        """Navigate to Check Box page."""
        self.expand_elements_menu()
        self.click(self.CHECK_BOX_ITEM)
    
    def navigate_to_radio_button(self):
        """Navigate to Radio Button page."""
        self.expand_elements_menu()
        self.click(self.RADIO_BUTTON_ITEM)
    
    def navigate_to_web_tables(self):
        """Navigate to Web Tables page."""
        self.expand_elements_menu()
        self.click(self.WEB_TABLES_ITEM)
    
    def navigate_to_buttons(self):
        """Navigate to Buttons page."""
        self.expand_elements_menu()
        self.click(self.BUTTONS_ITEM)
    
    def navigate_to_links(self):
        """Navigate to Links page."""
        self.expand_elements_menu()
        self.click(self.LINKS_ITEM)
    
    def navigate_to_broken_links(self):
        """Navigate to Broken Links - Images page."""
        self.expand_elements_menu()
        self.click(self.BROKEN_LINKS_ITEM)
    
    def navigate_to_upload_download(self):
        """Navigate to Upload and Download page."""
        self.expand_elements_menu()
        self.click(self.UPLOAD_DOWNLOAD_ITEM)
    
    def navigate_to_dynamic_properties(self):
        """Navigate to Dynamic Properties page."""
        self.expand_elements_menu()
        self.click(self.DYNAMIC_PROPERTIES_ITEM)
