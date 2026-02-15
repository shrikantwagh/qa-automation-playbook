"""Test cases for Buttons page."""
import pytest
from playwright.sync_api import Page
from pages.elements.buttons_page import ButtonsPage


@pytest.mark.elements
@pytest.mark.buttons
class TestButtons:
    """Test cases for Buttons functionality."""
    
    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        """Setup for each test."""
        self.buttons_page = ButtonsPage(page)
        self.buttons_page.navigate_to_page()
    
    @pytest.mark.smoke
    def test_double_click_button(self):
        """Test double click button functionality."""
        self.buttons_page.double_click_button()
        
        assert self.buttons_page.is_double_click_message_displayed()
        message = self.buttons_page.get_double_click_message()
        assert "You have done a double click" in message
    
    @pytest.mark.smoke
    def test_right_click_button(self):
        """Test right click button functionality."""
        self.buttons_page.right_click_button()
        
        assert self.buttons_page.is_right_click_message_displayed()
        message = self.buttons_page.get_right_click_message()
        assert "You have done a right click" in message
    
    @pytest.mark.smoke
    def test_dynamic_click_button(self):
        """Test dynamic click button functionality."""
        self.buttons_page.click_dynamic_button()
        
        assert self.buttons_page.is_dynamic_click_message_displayed()
        message = self.buttons_page.get_dynamic_click_message()
        assert "You have done a dynamic click" in message
    
    def test_all_buttons_in_sequence(self):
        """Test clicking all buttons in sequence."""
        # Double click
        self.buttons_page.double_click_button()
        assert self.buttons_page.is_double_click_message_displayed()
        
        # Right click
        self.buttons_page.right_click_button()
        assert self.buttons_page.is_right_click_message_displayed()
        
        # Dynamic click
        self.buttons_page.click_dynamic_button()
        assert self.buttons_page.is_dynamic_click_message_displayed()
        
        # Verify all messages are still displayed
        assert "double click" in self.buttons_page.get_double_click_message()
        assert "right click" in self.buttons_page.get_right_click_message()
        assert "dynamic click" in self.buttons_page.get_dynamic_click_message()
    
    def test_multiple_double_clicks(self):
        """Test multiple double clicks on the same button."""
        # First double click
        self.buttons_page.double_click_button()
        assert self.buttons_page.is_double_click_message_displayed()
        
        # Second double click (verify message persists or updates)
        self.buttons_page.double_click_button()
        assert self.buttons_page.is_double_click_message_displayed()
    
    def test_multiple_right_clicks(self):
        """Test multiple right clicks on the same button."""
        self.buttons_page.right_click_button()
        assert self.buttons_page.is_right_click_message_displayed()
        
        self.buttons_page.right_click_button()
        assert self.buttons_page.is_right_click_message_displayed()
    
    def test_multiple_dynamic_clicks(self):
        """Test multiple clicks on dynamic button."""
        self.buttons_page.click_dynamic_button()
        assert self.buttons_page.is_dynamic_click_message_displayed()
        
        self.buttons_page.click_dynamic_button()
        assert self.buttons_page.is_dynamic_click_message_displayed()
