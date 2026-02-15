# Quick Start Guide - DemoQA Test Automation

## ⚡ 5-Minute Setup

### Step 1: Prerequisites Check
```bash
python --version  # Should be 3.9+
pip --version
git --version
```

### Step 2: Clone and Setup
```bash
# Navigate to your workspace
cd ~/workspace

# Clone the repository (or extract the zip)
# If from zip:
unzip demoqa-automation.zip
cd demoqa-automation

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
# Install Python packages
pip install -r requirements.txt

# Install Playwright browsers (choose one or all)
playwright install chromium        # Recommended for start
# playwright install firefox
# playwright install webkit
```

### Step 4: Verify Installation
```bash
# Check if pytest is installed
pytest --version

# Check if playwright is installed
playwright --version
```

### Step 5: Run Your First Test
```bash
# Run smoke tests (fastest)
pytest -m smoke -v

# Or use the helper script
./run_tests.sh smoke
```

## 🎯 Common Commands

### Running Tests
```bash
# All tests
pytest

# Smoke tests only (fast)
pytest -m smoke

# Specific component
pytest -m text_box
pytest -m buttons
pytest -m web_tables

# Specific test file
pytest tests/elements/test_text_box.py

# With visible browser (headed mode)
pytest --headed

# Parallel execution (faster)
pytest -n auto
```

### Using the Helper Script
```bash
# Make it executable (first time only)
chmod +x run_tests.sh

# Run smoke tests
./run_tests.sh smoke

# Run all tests
./run_tests.sh all

# Run specific element tests
./run_tests.sh element text_box
./run_tests.sh element buttons

# Run in parallel
./run_tests.sh parallel 4

# Run with specific browser
./run_tests.sh browser firefox

# Run with visible browser
./run_tests.sh headed

# Generate HTML report
./run_tests.sh html
```

### Viewing Results
```bash
# HTML Report
# After running: ./run_tests.sh html
# Open: reports/report.html in browser

# Allure Report (if allure is installed)
./run_tests.sh allure
# This will automatically open the report
```

## 📝 Your First Test Run

Let's run a complete workflow:

```bash
# 1. Activate virtual environment
source venv/bin/activate  # or venv\Scripts\activate on Windows

# 2. Run smoke tests to verify everything works
pytest -m smoke -v

# 3. Run tests for Text Box component
pytest -m text_box -v

# 4. Run all Elements tests
pytest -m elements -v

# 5. Generate a report
pytest --html=reports/report.html --self-contained-html

# 6. Open the report
# Open reports/report.html in your browser
```

## 🔧 Configuration

### Environment Variables
Create a `.env` file (copy from `.env.example`):
```bash
cp .env.example .env
```

Edit `.env` to customize:
```env
BASE_URL=https://demoqa.com
HEADLESS=False              # Set to True for headless mode
BROWSER=chromium           # chromium, firefox, or webkit
VIEWPORT_WIDTH=1920
VIEWPORT_HEIGHT=1080
```

### Pytest Configuration
Edit `pytest.ini` to customize test execution:
- Default browser
- Screenshot settings
- Video recording
- Slow motion speed
- And more...

## 📊 Understanding Test Results

### Test Output
```
tests/elements/test_text_box.py::TestTextBox::test_fill_all_fields_and_submit PASSED [100%]

✓ PASSED - Test passed successfully
✗ FAILED - Test failed (see error details)
⊗ SKIPPED - Test was skipped
```

### Artifacts Location
- **Screenshots**: `reports/screenshots/`
- **Videos**: `test-results/`
- **Traces**: `test-results/`
- **Logs**: `logs/`

## 🐛 Troubleshooting

### Issue: "playwright: command not found"
```bash
# Reinstall playwright
pip install playwright
playwright install chromium
```

### Issue: "No module named 'playwright'"
```bash
# Ensure virtual environment is activated
source venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

### Issue: Tests are failing
```bash
# Run in headed mode to see what's happening
pytest --headed --slowmo 1000

# Check the logs
cat logs/test_run_*.log
```

### Issue: Browser not launching
```bash
# Reinstall browsers with dependencies
playwright install --with-deps chromium
```

## 📚 Next Steps

1. **Explore the tests**: Look at `tests/elements/` directory
2. **Study page objects**: Check `pages/elements/` directory
3. **Read the docs**: Open `README.md` for detailed information
4. **Write your first test**: Follow patterns in existing tests
5. **Check contributing guide**: Read `CONTRIBUTING.md`

## 🎓 Learning Resources

### Framework Components
- `pages/base_page.py` - Base page methods
- `tests/conftest.py` - Fixtures and setup
- `pytest.ini` - Test configuration
- `config/base_config.py` - Application configuration

### Example Tests
- `tests/elements/test_text_box.py` - Form testing
- `tests/elements/test_buttons.py` - Click interactions
- `tests/elements/test_web_tables.py` - Table operations

## 💡 Tips

1. **Start small**: Run smoke tests first
2. **Use headed mode**: While learning, use `--headed` to see what's happening
3. **Read error messages**: Pytest provides detailed error information
4. **Check screenshots**: Failed tests automatically capture screenshots
5. **Use markers**: Run specific test subsets with `-m marker_name`

## ✅ Verification Checklist

- [ ] Python 3.9+ installed
- [ ] Virtual environment created and activated
- [ ] Dependencies installed
- [ ] Playwright browsers installed
- [ ] Smoke tests passing
- [ ] Can run tests in headed mode
- [ ] Can generate HTML reports

## 🆘 Need Help?

1. Check `README.md` for detailed documentation
2. Review `CONTRIBUTING.md` for development guidelines
3. Read inline comments in code
4. Check error messages carefully
5. Review logs in `logs/` directory

## 🚀 Ready to Go!

You're all set! Start with:
```bash
./run_tests.sh smoke
```

Happy Testing! 🎉
