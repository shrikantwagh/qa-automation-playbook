source#!/bin/bash

# DemoQA Test Automation - Test Execution Script
# This script provides convenient commands to run tests in different configurations

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to print colored output
print_info() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

# Function to check if virtual environment is activated
check_venv() {
    if [[ -z "$VIRTUAL_ENV" ]]; then
        print_warning "Virtual environment not activated!"
        print_info "Run: source venv/bin/activate (Linux/Mac) or venv\\Scripts\\activate (Windows)"
        exit 1
    fi
}

# Function to install dependencies
install_deps() {
    print_info "Installing dependencies..."
    pip install -r requirements.txt
    playwright install chromium
    print_info "Dependencies installed successfully!"
}

# Function to run all tests
run_all_tests() {
    print_info "Running all tests..."
    pytest -v
}

# Function to run smoke tests
run_smoke_tests() {
    print_info "Running smoke tests..."
    pytest -m smoke -v
}

# Function to run tests for specific element
run_element_tests() {
    local element=$1
    print_info "Running tests for: $element"
    pytest -m "$element" -v
}

# Function to run tests in parallel
run_parallel_tests() {
    local workers=${1:-auto}
    print_info "Running tests in parallel with $workers workers..."
    pytest -n "$workers" -v
}

# Function to run tests with specific browser
run_browser_tests() {
    local browser=$1
    print_info "Running tests with $browser browser..."
    pytest --browser="$browser" -v
}

# Function to run tests in headed mode
run_headed_tests() {
    print_info "Running tests in headed mode..."
    pytest --headed --slowmo=500 -v
}

# Function to generate HTML report
generate_html_report() {
    print_info "Generating HTML report..."
    pytest --html=reports/report.html --self-contained-html
    print_info "Report generated at: reports/report.html"
}

# Function to generate Allure report
generate_allure_report() {
    print_info "Generating Allure report..."
    pytest --alluredir=allure-results
    allure serve allure-results
}

# Function to clean test artifacts
clean_artifacts() {
    print_info "Cleaning test artifacts..."
    rm -rf test-results/ playwright-report/ allure-results/ reports/ logs/
    find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
    find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
    print_info "Artifacts cleaned successfully!"
}

# Function to show help
show_help() {
    cat << EOF
DemoQA Test Automation - Test Execution Script

Usage: ./run_tests.sh [COMMAND] [OPTIONS]

Commands:
    install             Install all dependencies
    all                 Run all tests
    smoke              Run smoke tests only
    element <name>     Run tests for specific element (e.g., text_box, buttons)
    parallel [n]       Run tests in parallel (default: auto detect cores)
    browser <name>     Run tests with specific browser (chromium, firefox, webkit)
    headed             Run tests in headed mode with slow motion
    html               Generate HTML report
    allure             Generate Allure report
    clean              Clean all test artifacts
    help               Show this help message

Examples:
    ./run_tests.sh install
    ./run_tests.sh smoke
    ./run_tests.sh element text_box
    ./run_tests.sh parallel 4
    ./run_tests.sh browser firefox
    ./run_tests.sh headed
    ./run_tests.sh html

Element Markers:
    text_box, check_box, radio_button, web_tables, buttons,
    links, broken_links, upload_download, dynamic_properties

EOF
}

# Main script logic
main() {
    local command=${1:-help}
    
    case "$command" in
        install)
            install_deps
            ;;
        all)
            check_venv
            run_all_tests
            ;;
        smoke)
            check_venv
            run_smoke_tests
            ;;
        element)
            check_venv
            if [[ -z "$2" ]]; then
                print_error "Please specify element name"
                exit 1
            fi
            run_element_tests "$2"
            ;;
        parallel)
            check_venv
            run_parallel_tests "${2:-auto}"
            ;;
        browser)
            check_venv
            if [[ -z "$2" ]]; then
                print_error "Please specify browser name (chromium, firefox, webkit)"
                exit 1
            fi
            run_browser_tests "$2"
            ;;
        headed)
            check_venv
            run_headed_tests
            ;;
        html)
            check_venv
            generate_html_report
            ;;
        allure)
            check_venv
            generate_allure_report
            ;;
        clean)
            clean_artifacts
            ;;
        help|--help|-h)
            show_help
            ;;
        *)
            print_error "Unknown command: $command"
            show_help
            exit 1
            ;;
    esac
}

# Run main function
main "$@"
