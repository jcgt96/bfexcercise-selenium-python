# How to Contribute

Guidelines for contributing to this repository.

---

## 🏆 Developer Good Practices

Code is communication. We need to write code that is easy to read and
understand. Here are some best practices to follow:

1. **Small Commits**: Keep It So Simple (KISS).
   Read [“The Power of Small Commits.”](https://levelup.gitconnected.com/the-power-of-working-in-small-commits-8bae57ecfbda)
2. **Use GitMoji**: Use [GitMoji](https://gitmoji.dev/) to add emojis to your
   commit messages. It makes it easier to identify the purpose or intention of a
   commit.
3. **One Solution per PR**: Submit a PR with one solution at a time. If you need
   to refactor, do it in a separate PR.
4. **Unit Tests**: Unit tests are part of the Definition of Done in Agile
   practices. It doesn't matter if you write them first (TDD) or before the
   final commit.
5. **Run Linters**: Ensure your code passes all linting checks before making a
   PR.
6. **SonarQube Analysis**: Run a SonarQube analysis and address its
   recommendations before posting a PR.
7. **TDD for Bugs**: Write a unit test to reproduce the bug (red), modify it to
   reflect the expected behavior (green), then refactor the code to solve the
   bug (blue).

---

## 📝 Git Workflow

### Branches

⚠️ Never push directly to the `main` and `develop` branches. Always create a new
branch and submit a PR.

Branch naming conventions:

- `main`: Contains the latest release.
- `develop`: Contains the latest development version.
- `feature/xxx`: Contains a new feature.
- `bugfix/xxx`: Contains a bugfix.
- `hotfix/xxx`: Contains a hotfix.
- `docs/xxx`: Contains documentation changes.
- `refactor/xxx`: Contains refactoring changes.
- `test/xxx`: Contains test changes.
- `ci/xxx`: Contains CI changes.

### Commit Messages

- Use [GitMoji](https://gitmoji.dev/) to add emojis to your commit messages.
- Use the imperative, present tense:
    - "change" not "changed" nor "changes".
    - "fix" not "fixed" nor "fixes".
    - "add" not "added" nor "adds".
    - "remove" not "removed" nor "removes".

### Pull Requests

- Use the imperative, present tense for PR titles:
    - "change" not "changed" nor "changes".
    - "fix" not "fixed" nor "fixes".
    - "add" not "added" nor "adds".
    - "remove" not "removed" nor "removes".

---

## 👩‍💻 Development

### Run Code Style Linters

Keeping code clean and readable is essential. Remember:

> The ratio of time spent reading versus writing is well over 10 to 1. We are
> constantly reading old code as part of the effort to write new code. Making it
> easy to read makes it easier to write.
>
> _Robert C. Martin (a.k.a. Uncle Bob)_

To run the linter, execute the following command:

```bash
poetry run pre-commit
```

### Run Static Code Analysis

Running static code analysis helps detect potential bugs and code smells. Use
the following command to run the analysis:

```bash
poetry run pysonar-scanner
```

The report will be available at [http://localhost:9000](http://localhost:9000).

Ensure you have a SonarQube server running locally or in Docker. To run
SonarQube in Docker, execute:

```bash
docker compose -f scripts/docker-compose-sonar.yml up -d
```

For SonarQube initial setup, follow
the [instructions here](https://blankfactor.atlassian.net/wiki/spaces/Marqueta/pages/614793231/Developer+s+best+practices#%F0%9F%91%A8%E2%80%8D%F0%9F%92%BB-STATIC-CODE-ANALYSIS-WITH-SONARQUBE).

---

Following these guidelines ensures a smooth and efficient contribution process.
Happy coding!
