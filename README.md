# UI Test Automation with Playwright

This project demonstrates a simple UI test automation framework using Playwright. It includes tests for basic navigation and content checks on a sample website. The project is integrated with GitHub Actions for continuous integration and testing.

## Features
- Playwright-based UI test automation
- Automated testing with GitHub Actions CI/CD
- Tests for sample website workflows
- Scalable and maintainable test structure

## Setup Instructions

### Prerequisites
- Python 3.8+
- Node.js
- GitHub account

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/playwright-ui-tests.git
    cd playwright-ui-tests
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate     # Windows
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    playwright install
    ```

### Running Tests

To execute tests locally:

```bash
pytest
```

To run tests on GitHub Actions, simply push your changes to the main branch. The tests will be executed automatically.

### Project Structure
- `tests/test_example.py`: Contains basic Playwright UI tests.
- `.github/workflows/ci.yml`: GitHub Actions workflow for running tests on every push.

### CI/CD Integration
This project is integrated with GitHub Actions for continuous testing on push and pull requests. The workflow is defined in `.github/workflows/ci.yml`.

### Screenshots
Test execution generates screenshots saved in the screenshots/ directory for debugging purposes.

### Contributing
Contributions are welcome! Please open an issue or submit a pull request for any suggestions or improvements.