# Python + Behave + Selenium Project

This project leverages the Gherkin language to create a behavior-driven
development (BDD) framework using **Behave** in Python, analogous to the *
*Serenity BDD** framework. It follows the **Page Object Model (POM) Pattern** to
organize the automation codebase effectively.

---

## ✏️ Contributing

We welcome and appreciate contributions! Please refer to
our [Contribution Guidelines](docs/CONTRIBUTE-python.md) for detailed
instructions on how to contribute to this project.

---

## 🧰 Tech Stack

- **Python 3**: The core programming language used in this project.
- **[Poetry](https://python-poetry.org)**: A Python dependency management and
  packaging tool.
- **Behave**: A BDD framework for Python.
- **Allure Reports**: For generating detailed test execution reports.

---

## ℹ️ Getting Started

### Installation

To set up the project, run the following commands:

```bash
poetry shell
poetry install
poetry run post-install
```

If you haven't set up your environment yet, please follow the instructions in
the [Installation Guide](docs/INSTALLATION.md).

### Running Tests

Before running tests, ensure you activate the virtual environment:

```bash
poetry shell
```

To execute the tests, run:

```bash
poetry run test
```

For running tests in **headless mode**, use:

```bash
poetry run test-ci
```

### Reporting

After running tests, both the Playwright HTML report and the Allure report
should be generated automatically.

#### Opening Allure Report

Option 1: Open local reports:

```bash
npm run test:report:open
```

Option 2: Open online reports:

https://jcgt96.github.io/bfexcercise-selenium-python

Option 3: Download GitHub Actions artifact:

1. Navigate to your GitHub repository.
2. Go to `Actions > [Latest Action] > Artifacts >  github-pages`.
3. Extract the `github-pages.zip` file, then open `index.html` using Chrome:

    ```bash
    open -a "Google Chrome" --args --allow-file-access-from-files "$(pwd)/.run/reports/allure/index.html"
    ```

---

### Development

For detailed development guidelines and best practices, please refer to
the [Contribution Guidelines](docs/CONTRIBUTE-python.md).

---

## 🔧 Troubleshooting

Here are some common issues and how to address them:

- **Installation Issues**: Make sure to follow
  the [Installation Instructions](#installation) properly.
- **Python Interpreter Issues**: Ensure your IDE is configured to use the *
  *Poetry** Python interpreter.
- **Virtual Environment Issues**: If a virtual environment is mistakenly
  created, delete the folder and re-clone the repository.

---

Following these guidelines should help you get started quickly and efficiently.
Happy coding!
