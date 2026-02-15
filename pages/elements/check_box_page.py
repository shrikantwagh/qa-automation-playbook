"""Page object for Check Box page."""
from pages.base_page import BasePage
from playwright.sync_api import Page
from typing import List


class CheckBoxPage(BasePage):
    """Page object for DemoQA Check Box page."""
    
    # Page URL
    PAGE_URL = "/checkbox"
    
    # Locators
    EXPAND_ALL_BUTTON = "button[title='Expand all']"
    COLLAPSE_ALL_BUTTON = "button[title='Collapse all']"
    HOME_CHECKBOX = "label[for='tree-node-home'] .rct-checkbox"
    DESKTOP_CHECKBOX = "label[for='tree-node-desktop'] .rct-checkbox"
    DOCUMENTS_CHECKBOX = "label[for='tree-node-documents'] .rct-checkbox"
    DOWNLOADS_CHECKBOX = "label[for='tree-node-downloads'] .rct-checkbox"
    
    # Toggle buttons
    HOME_TOGGLE = "button[title='Toggle']"
    
    # Result
    RESULT_TEXT = "#result .text-success"
    
    def __init__(self, page: Page):
        super().__init__(page)
    
    def navigate_to_page(self):
        """Navigate to Check Box page."""
        self.navigate(self.PAGE_URL)
    
    def click_expand_all(self):
        """Click Expand All button."""
        self.logger.info("Clicking Expand All button")
        self.click(self.EXPAND_ALL_BUTTON)
    
    def click_collapse_all(self):
        """Click Collapse All button."""
        self.logger.info("Clicking Collapse All button")
        self.click(self.COLLAPSE_ALL_BUTTON)
    
    def click_home_checkbox(self):
        """Click Home checkbox."""
        self.logger.info("Clicking Home checkbox")
        self.click(self.HOME_CHECKBOX)
    
    def click_checkbox_by_label(self, label: str):
        """Click checkbox by its label text."""
        self.logger.info(f"Clicking checkbox: {label}")
        checkbox_selector = f"label[for='tree-node-{label.lower()}'] .rct-checkbox"
        self.click(checkbox_selector)
    
    def expand_node(self, node: str):
        """Expand a tree node."""
        self.logger.info(f"Expanding node: {node}")
        # This would need more specific implementation based on the tree structure
        pass
    
    def get_selected_items(self) -> List[str]:
        """Get list of selected checkbox items."""
        if not self.is_visible(self.RESULT_TEXT, timeout=2000):
            return []
        
        results = self.get_all_text(self.RESULT_TEXT)
        return results
    
    def is_checkbox_checked(self, checkbox_label: str) -> bool:
        """Check if a specific checkbox is checked."""
        checkbox_selector = f"label[for='tree-node-{checkbox_label.lower()}'] input"
        return self.is_checked(checkbox_selector)
    
    def get_result_text(self) -> str:
        """Get the result text displayed."""
        if not self.is_visible(self.RESULT_TEXT, timeout=2000):
            return ""
        return self.get_text("#result")
