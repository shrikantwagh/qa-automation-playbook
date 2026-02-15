# Contributing to DemoQA Test Automation

Thank you for your interest in contributing to this project! This guide will help you get started.

## Code of Conduct

- Be respectful and inclusive
- Focus on constructive feedback
- Help others learn and grow

## Getting Started

### Prerequisites

- Python 3.9+
- Git
- Basic understanding of Python and Playwright
- Familiarity with Page Object Model pattern

### Setup Development Environment

1. Fork and clone the repository
```bash
git clone <your-fork-url>
cd demoqa-automation
```

2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
playwright install
```

## Project Structure Guidelines

### Adding New Page Objects

1. Create page object in appropriate directory under `pages/`
2. Inherit from `BasePage`
3. Follow naming convention: `<feature>_page.py`
4. Example:

```python
from pages.base_page import BasePage
from playwright.sync_api import Page

class NewFeaturePage(BasePage):
    # Constants for URL and locators at the top
    PAGE_URL = "/new-feature"
    ELEMENT_SELECTOR = "#element-id"
    
    def __init__(self, page: Page):
        super().__init__(page)
    
    def navigate_to_page(self):
        """Navigate to the page."""
        self.navigate(self.PAGE_URL)
    
    # Add methods for page interactions
```

### Adding New Tests

1. Create test file in appropriate directory under `tests/`
2. Use descriptive test names: `test_<scenario>.py`
3. Use appropriate markers
4. Example:

```python
import pytest
from playwright.sync_api import Page
from pages.elements.new_feature_page import NewFeaturePage

@pytest.mark.elements
@pytest.mark.new_feature
class TestNewFeature:
    
    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        self.feature_page = NewFeaturePage(page)
        self.feature_page.navigate_to_page()
    
    @pytest.mark.smoke
    def test_feature_works(self):
        # Test implementation
        pass
```

### Locator Strategy

Priority order for locators:
1. `data-testid` attributes (most reliable)
2. `id` attributes
3. Unique `class` names
4. Text content (for stable text)
5. CSS selectors (as last resort)

Example:
```python
# Good
SUBMIT_BUTTON = "[data-testid='submit-btn']"
EMAIL_INPUT = "#userEmail"

# Avoid if possible
BUTTON = "div > button:nth-child(3)"  # Fragile
```

### Test Data Management

1. Use `DataGenerator` for dynamic data:
```python
from utils.data_generator import data_generator

user_data = data_generator.generate_user_data()
```

2. Use JSON files for static test data:
```python
import json
with open('config/test_data/users.json') as f:
    data = json.load(f)
```

## Coding Standards

### Python Style Guide

- Follow PEP 8
- Use type hints where applicable
- Maximum line length: 100 characters
- Use docstrings for classes and methods

### Naming Conventions

- **Files**: `snake_case.py`
- **Classes**: `PascalCase`
- **Functions/Methods**: `snake_case()`
- **Constants**: `UPPER_SNAKE_CASE`
- **Variables**: `snake_case`

### Documentation

- Add docstrings to all public methods
- Include type hints
- Document complex logic with comments

Example:
```python
def fill_registration_form(
    self,
    first_name: str,
    last_name: str,
    email: str
) -> None:
    """
    Fill the registration form with provided data.
    
    Args:
        first_name: User's first name
        last_name: User's last name
        email: User's email address
    """
    self.fill(self.FIRST_NAME_INPUT, first_name)
    self.fill(self.LAST_NAME_INPUT, last_name)
    self.fill(self.EMAIL_INPUT, email)
```

## Testing Your Changes

### Run Tests Locally

```bash
# Run all tests
pytest

# Run specific tests
pytest tests/elements/test_text_box.py

# Run with markers
pytest -m smoke
```

### Check Code Quality

```bash
# Format code
black .

# Lint code
flake8 .

# Type checking
mypy pages/ tests/
```

## Commit Guidelines

### Commit Message Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `test`: Adding or updating tests
- `refactor`: Code refactoring
- `style`: Code style changes
- `chore`: Maintenance tasks

**Examples:**
```
feat(pages): Add upload download page object

Implemented page object for upload/download functionality
including methods for file uploads and downloads.

Closes #123
```

```
fix(tests): Fix flaky web tables test

Updated wait strategy to handle dynamic table loading.
```

## Pull Request Process

1. **Create a branch** from `main`
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** following the guidelines above

3. **Write/update tests** for your changes

4. **Ensure all tests pass**
   ```bash
   pytest
   ```

5. **Update documentation** if needed

6. **Commit your changes** with clear messages

7. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

8. **Create Pull Request**
   - Provide clear description of changes
   - Reference any related issues
   - Ensure CI checks pass

### PR Checklist

- [ ] Tests added/updated
- [ ] All tests passing
- [ ] Code follows style guidelines
- [ ] Documentation updated
- [ ] Commit messages are clear
- [ ] No merge conflicts

## Questions?

If you have questions:
- Check existing documentation
- Search existing issues
- Create a new issue with the `question` label

Thank you for contributing! 🎉
