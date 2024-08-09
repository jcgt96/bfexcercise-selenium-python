#!/bin/sh

# Run pre-commit checks
poetry run pre-commit run --all-files
if [ $? -ne 0 ]; then
    echo "Pre-commit checks failed. Push aborted."
    exit 1
fi

# Run tests
poetry run behave
if [ $? -ne 0 ]; then
    echo "Tests failed. Push aborted."
    exit 1
fi

# Run SonarQube analysis (optional, if configured)
# poetry run sonar-scanner
# if [ $? -ne 0 ]; then
#     echo "SonarQube analysis failed. Push aborted."
#     exit 1
# fi

exit 0
