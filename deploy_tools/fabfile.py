import random
from fabric.contrib.files import append, exists
from fabric.api import cd, env, local, run, sudo, settings, hide

env.use_ssh_config = True
CONFIG_PRODUCTION = "config.settings.production"

REPO_URL = "https://github.com/rattletat/covid-register.eu.git"
ENV_VARS = [
    f"DJANGO_SETTINGS_MODULE={CONFIG_PRODUCTION}",
    "DJANGO_READ_DOT_ENV_FILE=y",
]
POETRY = " ".join(ENV_VARS) + " python3 -m poetry "


def deploy(domain):
    site_folder = f"/home/{env.user}/sites/{domain}"
    run(f"mkdir -p {site_folder}")
    with cd(site_folder):
        _get_latest_source()
        _update_virtualenv(domain)
        _create_or_update_dotenv(domain)
        _update_static_files()
        _update_database()
        _restart_gunicorn(domain)
        _restart_nginx()


def _get_latest_source():
    if exists(".git"):
        run("git fetch")
    else:
        run(f"git clone {REPO_URL} .")
    current_commit = local("git log -n 1 --format=%H", capture=True)
    run(f"git reset --hard {current_commit}")


def _update_virtualenv(domain):
    with settings(hide("warnings", "running", "stdout", "stderr"), warn_only=True):
        poetry_failed = run("poetry check").failed

    if poetry_failed:
        run(
            "curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python"
        )
        run("source $HOME/.poetry/env")
    if not exists("pyproject.toml"):
        run(POETRY + f"new . -n --src --name {domain}")
    run(POETRY + "install")


def _create_or_update_dotenv(domain):
    run("set -a")
    run("source .env")
    run("set +a")


def _update_static_files():
    run(POETRY + "run python3.8 manage.py collectstatic --noinput")


def _update_database():
    run(POETRY + "run python3.8 manage.py makemigrations")
    run(POETRY + "run python3.8 manage.py migrate --noinput")


def _restart_gunicorn(domain):
    sudo(f"systemctl restart gunicorn-{domain}.service")


def _restart_nginx():
    sudo(f"systemctl restart nginx.service")
