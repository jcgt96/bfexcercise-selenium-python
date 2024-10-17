import os
import shutil
import subprocess
import sys


def post_install():
    print("Running post-install actions...")
    subprocess.run("poetry run pre-commit install", shell=True, check=False)
    subprocess.run("npm install", shell=True, check=False)


def sonar():
    print("Running SonarQube...")
    sonar_url = "http://localhost:9000"
    subprocess.run(
        "poetry run pysonar-scanner -Dsonar.host.url=" + sonar_url,
        shell=True,
        check=False,
    )


def lint():
    print("Running linting actions...")
    result = subprocess.run(
        "poetry run pre-commit run --all-files", shell=True, check=False
    )
    sys.exit(result.returncode)


def test(headless=False):
    print("Running tests...")
    environment = "HEADLESS=" + str(headless)
    result = subprocess.run(environment + " poetry run behave", shell=True, check=False)
    sys.exit(result.returncode)


def report():
    print("Generating report...")
    main_dir = "./.run/reports"
    results_output_dir = main_dir + "/behave/results"
    reports_output_dir = main_dir + "/allure/report"
    history_name_dir = "/history"

    # Remove history folder
    if os.path.exists(results_output_dir + history_name_dir):
        shutil.rmtree(results_output_dir + history_name_dir)

    # Copy history folder
    if os.path.exists(reports_output_dir + history_name_dir):
        shutil.copytree(
            reports_output_dir + history_name_dir, results_output_dir + history_name_dir
        )

    result = subprocess.run(
        "npx allure generate "
        + results_output_dir
        + " --clean -o "
        + reports_output_dir,
        shell=True,
        check=False,
    )

    print("Report generated on: " + reports_output_dir + "/index.html")
    current_directory = subprocess.run(
        "pwd", capture_output=True, text=True, check=False
    )
    current_directory = current_directory.stdout.strip()
    print(
        'You can open the report with: open -a "Google Chrome" --args '
        '--allow-file-access-from-files "'
        + current_directory
        + reports_output_dir[1:]
        + '/index.html"'
    )
    sys.exit(result.returncode)


def test_ci():
    test(headless=True)  # Reuse test function with headless=True


if __name__ == "__main__":
    post_install()
