# Python + Behave + Selenium Project

Based on the Gherkin language, here is a framework using Behave that is the
equivalent of Serenity BDD in Python. Here is used the POM (Page Object Model
Pattern).

---

## ✏️ How to Contribute

We welcome contributions! Please
see [docs/CONTRIBUTE-python.md](docs/CONTRIBUTE-python.md) for guidelines on how
to contribute to this project.

---

## 🧰 Tech Stack

- **Python 3**: The programming language used for this project.
- **[Poetry](https://python-poetry.org)**: Dependency manager for Python
  projects.
- Behave.
- Allure reports.

---

## ℹ️ Instructions

### Installation

To install the project, run the following commands:

```bash
poetry shell
poetry install
poetry run post-install
```

If your environment isn't set up yet, please refer
to [docs/INSTALLATION.md](docs/INSTALLATION.md) for detailed instructions.

### Execution

Before running the tests you need to start the environment:

```bash
poetry shell
```

To run the test, you need to run the following command:

```bash
poetry run test
```

To run the browser in headless mode:

```bash
poetry run test-ci
```

### Reporting

To run the report you need to run the following command after the tests:

```bash
poetry run report
```

The previous command gives you instructions on how to open the report.

### Development

For development instructions and contribution guidelines, please
see [docs/CONTRIBUTE-python.md](docs/CONTRIBUTE-python.md).

## 🔧 Troubleshooting

The following are the most common issues:

- Most of the issues can be addressed following the **Installation**
  instructions in this file.
- In the IDE you need to set your **Python Interpreter** to **Poetry**.
- If you, by error, create Virtual Environment for this project, delete the
  folder and re-clone it.

---

By following these guidelines, you should be able to get up and running with the
project quickly and easily. Happy coding!
