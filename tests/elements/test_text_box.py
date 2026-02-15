"""Test cases for Text Box page."""
import pytest
from playwright.sync_api import Page, expect
from pages.elements.text_box_page import TextBoxPage


@pytest.mark.elements
@pytest.mark.text_box
class TestTextBox:
    """Test cases for Text Box functionality."""
    
    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        """Setup for each test."""
        self.text_box_page = TextBoxPage(page)
        self.text_box_page.navigate_to_page()
    
    @pytest.mark.smoke
    def test_fill_all_fields_and_submit(self):
        """Test filling all fields and submitting form."""
        # Test data
        full_name = "John Doe"
        email = "john.doe@example.com"
        current_address = "123 Main St, New York, NY 10001"
        permanent_address = "456 Oak Ave, Boston, MA 02101"
        
        # Fill and submit form
        self.text_box_page.submit_form(
            full_name=full_name,
            email=email,
            current_address=current_address,
            permanent_address=permanent_address
        )
        
        # Verify output is displayed
        assert self.text_box_page.is_output_displayed(), "Output should be displayed"
        
        # Verify output data
        output_data = self.text_box_page.get_all_output_data()
        assert output_data["name"] == full_name, f"Expected name: {full_name}"
        assert output_data["email"] == email, f"Expected email: {email}"
        assert output_data["current_address"] == current_address
        assert output_data["permanent_address"] == permanent_address
    
    def test_submit_with_only_required_fields(self):
        """Test submitting with only name and email."""
        full_name = "Jane Smith"
        email = "jane.smith@test.com"
        
        self.text_box_page.fill_full_name(full_name)
        self.text_box_page.fill_email(email)
        self.text_box_page.click_submit()
        
        assert self.text_box_page.is_output_displayed()
        assert self.text_box_page.get_output_name() == full_name
        assert self.text_box_page.get_output_email() == email
    
    def test_submit_with_special_characters(self):
        """Test form with special characters in address."""
        full_name = "Test User"
        email = "test@domain.com"
        current_address = "123 Main St, Apt #4B, Floor 2nd"
        permanent_address = "Building-A, Street-5, Area/Zone: North"
        
        self.text_box_page.submit_form(
            full_name=full_name,
            email=email,
            current_address=current_address,
            permanent_address=permanent_address
        )
        
        assert self.text_box_page.is_output_displayed()
        output_data = self.text_box_page.get_all_output_data()
        assert current_address in output_data["current_address"]
        assert permanent_address in output_data["permanent_address"]
    
    def test_submit_with_long_text(self):
        """Test form with very long text."""
        full_name = "A" * 100
        email = "longtest@example.com"
        current_address = "Very long address " * 20
        permanent_address = "Another long address " * 20
        
        self.text_box_page.submit_form(
            full_name=full_name,
            email=email,
            current_address=current_address,
            permanent_address=permanent_address
        )
        
        assert self.text_box_page.is_output_displayed()
        assert len(self.text_box_page.get_output_name()) > 0
    
    @pytest.mark.parametrize("full_name,email,current_address,permanent_address", [
        ("Alice Brown", "alice@test.com", "100 Park Ave", "200 Lake Dr"),
        ("Bob Johnson", "bob@example.org", "300 Hill St", "400 Valley Rd"),
        ("Carol White", "carol@domain.net", "500 River Ln", "600 Forest Way"),
    ])
    def test_multiple_submissions(self, full_name, email, current_address, permanent_address):
        """Test multiple different data submissions."""
        self.text_box_page.submit_form(
            full_name=full_name,
            email=email,
            current_address=current_address,
            permanent_address=permanent_address
        )
        
        assert self.text_box_page.is_output_displayed()
        output_data = self.text_box_page.get_all_output_data()
        assert output_data["name"] == full_name
        assert output_data["email"] == email
    
    def test_email_field_validation(self):
        """Test email field with invalid email format."""
        # Note: DemoQA may or may not have client-side validation
        self.text_box_page.fill_full_name("Test User")
        self.text_box_page.fill_email("invalid-email")
        self.text_box_page.click_submit()
        
        # This test documents the actual behavior
        # If there's no validation, output will still appear
        # This can be adjusted based on actual application behavior
    
    def test_clear_and_refill_fields(self):
        """Test clearing fields and refilling them."""
        # First submission
        self.text_box_page.fill_full_name("First Name")
        self.text_box_page.fill_email("first@test.com")
        self.text_box_page.click_submit()
        
        # Clear and refill
        self.text_box_page.clear_all_fields()
        
        # Second submission
        full_name = "Second Name"
        email = "second@test.com"
        self.text_box_page.fill_full_name(full_name)
        self.text_box_page.fill_email(email)
        self.text_box_page.click_submit()
        
        assert self.text_box_page.get_output_name() == full_name
        assert self.text_box_page.get_output_email() == email
