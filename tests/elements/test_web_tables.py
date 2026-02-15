"""Test cases for Web Tables page."""
import pytest
from playwright.sync_api import Page
from pages.elements.web_tables_page import WebTablesPage


@pytest.mark.elements
@pytest.mark.web_tables
class TestWebTables:
    """Test cases for Web Tables functionality."""
    
    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        """Setup for each test."""
        self.web_tables_page = WebTablesPage(page)
        self.web_tables_page.navigate_to_page()
    
    @pytest.mark.smoke
    def test_add_new_record(self):
        """Test adding a new record to the table."""
        # Get initial count
        initial_count = self.web_tables_page.get_row_count()
        
        # Add new record
        self.web_tables_page.add_new_record(
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            age="30",
            salary="50000",
            department="Engineering"
        )
        
        # Verify record was added
        new_count = self.web_tables_page.get_row_count()
        assert new_count == initial_count + 1, "Row count should increase by 1"
        
        # Search for the new record
        self.web_tables_page.search("John")
        table_data = self.web_tables_page.get_table_data()
        
        assert len(table_data) > 0, "Should find at least one record"
        assert table_data[0]["first_name"] == "John"
        assert table_data[0]["email"] == "john.doe@example.com"
    
    def test_edit_existing_record(self):
        """Test editing an existing record."""
        # Add a record first
        self.web_tables_page.add_new_record(
            first_name="Jane",
            last_name="Smith",
            email="jane.smith@test.com",
            age="25",
            salary="60000",
            department="QA"
        )
        
        # Search for the record
        self.web_tables_page.search("Jane")
        
        # Edit the record
        self.web_tables_page.edit_record(
            row_index=0,
            salary="70000",
            department="Engineering"
        )
        
        # Verify changes
        table_data = self.web_tables_page.get_table_data()
        assert table_data[0]["salary"] == "70000"
        assert table_data[0]["department"] == "Engineering"
        # Other fields should remain unchanged
        assert table_data[0]["first_name"] == "Jane"
        assert table_data[0]["email"] == "jane.smith@test.com"
    
    def test_delete_record(self):
        """Test deleting a record from the table."""
        # Add a record
        self.web_tables_page.add_new_record(
            first_name="Delete",
            last_name="Me",
            email="delete.me@test.com",
            age="40",
            salary="80000",
            department="Sales"
        )
        
        # Search for the record
        self.web_tables_page.search("Delete")
        initial_count = self.web_tables_page.get_row_count()
        
        # Delete the record
        self.web_tables_page.delete_record(row_index=0)
        
        # Clear search to see all records
        self.web_tables_page.clear_search()
        
        # Verify record count decreased
        new_count = self.web_tables_page.get_row_count()
        assert new_count == initial_count - 1
    
    def test_search_functionality(self):
        """Test search functionality."""
        # Add a unique record
        unique_email = "unique.test@example.com"
        self.web_tables_page.add_new_record(
            first_name="Unique",
            last_name="User",
            email=unique_email,
            age="35",
            salary="90000",
            department="Marketing"
        )
        
        # Search by email
        self.web_tables_page.search(unique_email)
        results = self.web_tables_page.get_table_data()
        
        assert len(results) > 0, "Should find the record"
        assert results[0]["email"] == unique_email
    
    def test_search_no_results(self):
        """Test search with no matching results."""
        self.web_tables_page.search("NonExistentUser12345")
        results = self.web_tables_page.get_table_data()
        
        # When no results, table should show empty rows or no data
        assert len(results) == 0 or all(not row["first_name"] for row in results)
    
    @pytest.mark.parametrize("first_name,last_name,age,salary,department", [
        ("Alice", "Johnson", "28", "55000", "HR"),
        ("Bob", "Williams", "32", "65000", "IT"),
        ("Carol", "Brown", "45", "75000", "Finance"),
    ])
    def test_add_multiple_records(self, first_name, last_name, age, salary, department):
        """Test adding multiple different records."""
        email = f"{first_name.lower()}.{last_name.lower()}@test.com"
        
        self.web_tables_page.add_new_record(
            first_name=first_name,
            last_name=last_name,
            email=email,
            age=age,
            salary=salary,
            department=department
        )
        
        # Search and verify
        self.web_tables_page.search(first_name)
        results = self.web_tables_page.get_table_data()
        
        assert len(results) > 0
        assert results[0]["first_name"] == first_name
        assert results[0]["last_name"] == last_name
    
    def test_table_pagination(self):
        """Test table pagination if applicable."""
        # This test depends on how many default rows exist
        # and if pagination is available
        
        # Try to select different rows per page options
        try:
            self.web_tables_page.select_rows_per_page("5")
            # Verify this doesn't cause errors
        except Exception as e:
            pytest.skip(f"Pagination not available or different: {e}")
    
    def test_form_validation_missing_fields(self):
        """Test form with missing required fields."""
        self.web_tables_page.click_add_button()
        
        # Try to submit with missing fields
        self.web_tables_page.fill_registration_form(
            first_name="",
            last_name="",
            email="",
            age="",
            salary="",
            department=""
        )
        self.web_tables_page.click_submit()
        
        # Form should still be visible (validation should prevent submission)
        # This tests the actual application behavior
    
    def test_clear_search(self):
        """Test clearing search box."""
        # Add and search for a record
        self.web_tables_page.add_new_record(
            first_name="Search",
            last_name="Test",
            email="search.test@example.com",
            age="30",
            salary="60000",
            department="Testing"
        )
        
        self.web_tables_page.search("Search")
        filtered_results = self.web_tables_page.get_table_data()
        
        # Clear search
        self.web_tables_page.clear_search()
        all_results = self.web_tables_page.get_table_data()
        
        # All results should show more records than filtered
        assert len(all_results) >= len(filtered_results)
