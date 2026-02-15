# DemoQA Test Automation Framework

Comprehensive Playwright-based test automation framework for DemoQA website using Python and Page Object Model (POM) design pattern.

## 🎯 Features

- **Page Object Model (POM)** design pattern for maintainable test code
- **Playwright** for reliable cross-browser testing
- **Pytest** framework with custom fixtures and markers
- **Parallel execution** support with pytest-xdist
- **Comprehensive reporting** with HTML and Allure reports
- **Screenshot** capture on test failures
- **Organized test structure** by functionality
- **Logging** at multiple levels
- **CI/CD ready** with GitHub Actions

## 📁 Project Structure

```
demoqa-automation/
├── config/                  # Configuration files
├── pages/                   # Page Object Models
│   ├── base_page.py
│   └── elements/           # Elements section pages
├── components/             # Reusable component objects
├── tests/                  # Test cases
│   └── elements/          # Elements tests
├── utils/                  # Utility functions
├── fixtures/               # Custom fixtures
├── test_data/             # Test data files
├── logs/                   # Test execution logs
├── reports/               # Test reports
└── pytest.ini             # Pytest configuration
```

## 🚀 Getting Started

### Prerequisites

- Python 3.9 or higher
- pip (Python package installer)

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd demoqa-automation
```

2. Create a virtual environment:
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Install Playwright browsers:
```bash
playwright install chromium
# Or install all browsers
playwright install
```

## 🧪 Running Tests

### Run all tests:
```bash
pytest
```

### Run specific test file:
```bash
pytest tests/elements/test_text_box.py
```

### Run tests by marker:
```bash
# Run smoke tests only
pytest -m smoke

# Run all elements tests
pytest -m elements

# Run specific element tests
pytest -m text_box
pytest -m buttons
```

### Run tests in parallel:
```bash
# Auto detect CPU cores
pytest -n auto

# Specify number of workers
pytest -n 4
```

### Run with specific browser:
```bash
pytest --browser chromium
pytest --browser firefox
pytest --browser webkit
```

### Run in headed mode (see browser):
```bash
pytest --headed
```

### Run with slow motion:
```bash
pytest --headed --slowmo 1000
```

### Generate HTML report:
```bash
pytest --html=reports/report.html --self-contained-html
```

### Generate Allure report:
```bash
# Run tests with allure
pytest --alluredir=allure-results

# Generate and open report
allure serve allure-results
```

## 📝 Test Organization

### Markers

Tests are organized using pytest markers:

- `@pytest.mark.smoke` - Critical smoke tests
- `@pytest.mark.regression` - Full regression suite
- `@pytest.mark.elements` - All elements section tests
- `@pytest.mark.text_box` - Text Box specific tests
- `@pytest.mark.buttons` - Buttons specific tests
- `@pytest.mark.web_tables` - Web Tables specific tests
- And more...

### Test Naming Convention

- Test files: `test_<feature>.py`
- Test classes: `Test<Feature>`
- Test methods: `test_<scenario>`

Example:
```python
@pytest.mark.elements
@pytest.mark.text_box
class TestTextBox:
    def test_fill_all_fields_and_submit(self):
        # Test implementation
        pass
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the root directory:

```env
BASE_URL=https://demoqa.com
HEADLESS=False
BROWSER=chromium
VIEWPORT_WIDTH=1920
VIEWPORT_HEIGHT=1080
LOG_LEVEL=INFO
```

### pytest.ini

Key configurations in `pytest.ini`:
- Test discovery paths
- Default command-line options
- Marker definitions
- Logging configuration
- Timeout settings

## 📊 Page Objects

### Base Page

All page objects inherit from `BasePage` which provides common methods:

```python
from pages.base_page import BasePage

class TextBoxPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
    
    def navigate_to_page(self):
        self.navigate("/text-box")
```

### Available Page Objects

- `TextBoxPage` - Text input form
- `CheckBoxPage` - Checkbox tree
- `RadioButtonPage` - Radio button selection
- `WebTablesPage` - Editable data table
- `ButtonsPage` - Click, double-click, right-click
- `LinksPage` - Various link types
- `BrokenLinksImagesPage` - Broken links and images
- `UploadDownloadPage` - File operations
- `DynamicPropertiesPage` - Dynamic element properties

## 🛠 Writing New Tests

### Example Test

```python
import pytest
from playwright.sync_api import Page
from pages.elements.text_box_page import TextBoxPage

@pytest.mark.elements
@pytest.mark.text_box
class TestTextBox:
    
    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        self.text_box_page = TextBoxPage(page)
        self.text_box_page.navigate_to_page()
    
    @pytest.mark.smoke
    def test_submit_form(self):
        self.text_box_page.fill_full_name("John Doe")
        self.text_box_page.fill_email("john@example.com")
        self.text_box_page.click_submit()
        
        assert self.text_box_page.is_output_displayed()
```

## 📈 Continuous Integration

GitHub Actions workflow example:

```yaml
name: Playwright Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          playwright install --with-deps chromium
      - name: Run tests
        run: pytest --browser chromium
      - uses: actions/upload-artifact@v4
        if: always()
        with:
          name: test-results
          path: test-results/
```

## 🐛 Debugging

### Run with trace:
```bash
pytest --tracing on
```

### View traces:
```bash
playwright show-trace trace.zip
```

### Debug with headed browser:
```bash
pytest --headed --slowmo 1000
```

## 📚 Best Practices

1. **Keep page objects simple** - One page object per page
2. **Use descriptive selectors** - Prefer data-testid over CSS
3. **Wait for elements** - Use built-in waits instead of sleep
4. **Independent tests** - Each test should be able to run independently
5. **Clean test data** - Clean up after tests when needed
6. **Meaningful assertions** - Use descriptive assertion messages
7. **DRY principle** - Reuse common code through fixtures and utilities

## 🤝 Contributing

1. Create a feature branch
2. Make your changes
3. Write/update tests
4. Ensure all tests pass
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## 📞 Support

For questions or issues, please create an issue in the repository.

## 🔗 Resources

- [Playwright Documentation](https://playwright.dev/python/)
- [Pytest Documentation](https://docs.pytest.org/)
- [DemoQA Website](https://demoqa.com/)
