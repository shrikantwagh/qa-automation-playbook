"""Page object for Web Tables page."""
from pages.base_page import BasePage
from playwright.sync_api import Page
from typing import List, Dict


class WebTablesPage(BasePage):
    """Page object for DemoQA Web Tables page."""
    
    # Page URL
    PAGE_URL = "/webtables"
    
    # Locators
    ADD_BUTTON = "#addNewRecordButton"
    SEARCH_BOX = "#searchBox"
    
    # Modal/Form locators
    REGISTRATION_FORM = ".modal-content"
    FIRST_NAME_INPUT = "#firstName"
    LAST_NAME_INPUT = "#lastName"
    EMAIL_INPUT = "#userEmail"
    AGE_INPUT = "#age"
    SALARY_INPUT = "#salary"
    DEPARTMENT_INPUT = "#department"
    SUBMIT_BUTTON = "#submit"
    CLOSE_BUTTON = ".close"
    
    # Table locators
    TABLE_ROWS = ".rt-tr-group"
    TABLE_HEADERS = ".rt-thead .rt-th"
    TABLE_CELLS = ".rt-td"
    
    # Action buttons in table
    EDIT_BUTTON = "span[title='Edit']"
    DELETE_BUTTON = "span[title='Delete']"
    
    # Pagination
    PREVIOUS_BUTTON = "button:has-text('Previous')"
    NEXT_BUTTON = "button:has-text('Next')"
    ROWS_SELECT = "select[aria-label='rows per page']"
    
    def __init__(self, page: Page):
        super().__init__(page)
    
    def navigate_to_page(self):
        """Navigate to Web Tables page."""
        self.navigate(self.PAGE_URL)
    
    def click_add_button(self):
        """Click Add button to open registration form."""
        self.logger.info("Clicking Add button")
        self.click(self.ADD_BUTTON)
        self.wait_for_element_visible(self.REGISTRATION_FORM)
    
    def fill_registration_form(self, first_name: str, last_name: str, email: str, 
                              age: str, salary: str, department: str):
        """Fill the registration form with provided data."""
        self.logger.info("Filling registration form")
        self.fill(self.FIRST_NAME_INPUT, first_name)
        self.fill(self.LAST_NAME_INPUT, last_name)
        self.fill(self.EMAIL_INPUT, email)
        self.fill(self.AGE_INPUT, age)
        self.fill(self.SALARY_INPUT, salary)
        self.fill(self.DEPARTMENT_INPUT, department)
    
    def click_submit(self):
        """Click submit button in form."""
        self.logger.info("Clicking submit button")
        self.click(self.SUBMIT_BUTTON)
    
    def add_new_record(self, first_name: str, last_name: str, email: str, 
                       age: str, salary: str, department: str):
        """Add a new record to the table."""
        self.click_add_button()
        self.fill_registration_form(first_name, last_name, email, age, salary, department)
        self.click_submit()
    
    def search(self, search_term: str):
        """Search in the table."""
        self.logger.info(f"Searching for: {search_term}")
        self.fill(self.SEARCH_BOX, search_term)
    
    def clear_search(self):
        """Clear search box."""
        self.page.locator(self.SEARCH_BOX).clear()
    
    def get_table_data(self) -> List[Dict[str, str]]:
        """Get all data from the table as list of dictionaries."""
        rows = []
        row_elements = self.page.locator(self.TABLE_ROWS).all()
        
        for row_element in row_elements:
            cells = row_element.locator(self.TABLE_CELLS).all()
            if len(cells) > 0 and cells[0].text_content().strip():
                row_data = {
                    "first_name": cells[0].text_content().strip(),
                    "last_name": cells[1].text_content().strip(),
                    "age": cells[2].text_content().strip(),
                    "email": cells[3].text_content().strip(),
                    "salary": cells[4].text_content().strip(),
                    "department": cells[5].text_content().strip()
                }
                rows.append(row_data)
        
        return rows
    
    def get_row_count(self) -> int:
        """Get count of rows in table."""
        data = self.get_table_data()
        return len(data)
    
    def click_edit_for_row(self, row_index: int):
        """Click edit button for specific row (0-based index)."""
        self.logger.info(f"Clicking edit for row {row_index}")
        edit_buttons = self.page.locator(self.EDIT_BUTTON).all()
        if row_index < len(edit_buttons):
            edit_buttons[row_index].click()
            self.wait_for_element_visible(self.REGISTRATION_FORM)
    
    def click_delete_for_row(self, row_index: int):
        """Click delete button for specific row (0-based index)."""
        self.logger.info(f"Clicking delete for row {row_index}")
        delete_buttons = self.page.locator(self.DELETE_BUTTON).all()
        if row_index < len(delete_buttons):
            delete_buttons[row_index].click()
    
    def edit_record(self, row_index: int, first_name: str = None, last_name: str = None, 
                   email: str = None, age: str = None, salary: str = None, department: str = None):
        """Edit an existing record."""
        self.click_edit_for_row(row_index)
        
        if first_name:
            self.clear_and_fill(self.FIRST_NAME_INPUT, first_name)
        if last_name:
            self.clear_and_fill(self.LAST_NAME_INPUT, last_name)
        if email:
            self.clear_and_fill(self.EMAIL_INPUT, email)
        if age:
            self.clear_and_fill(self.AGE_INPUT, age)
        if salary:
            self.clear_and_fill(self.SALARY_INPUT, salary)
        if department:
            self.clear_and_fill(self.DEPARTMENT_INPUT, department)
        
        self.click_submit()
    
    def delete_record(self, row_index: int):
        """Delete a record from the table."""
        self.click_delete_for_row(row_index)
    
    def select_rows_per_page(self, rows: str):
        """Select number of rows per page."""
        self.select_option(self.ROWS_SELECT, rows)
    
    def click_next_page(self):
        """Click next page button."""
        self.click(self.NEXT_BUTTON)
    
    def click_previous_page(self):
        """Click previous page button."""
        self.click(self.PREVIOUS_BUTTON)
