#/bin/sh

poetry install
poetry shell
npm install
poetry run pre-commit install
cp scripts/pre-push.sh .git/hooks/pre-push
chmod +x .git/hooks/pre-push
