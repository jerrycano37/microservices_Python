import click

from module.fastapi.main import start_fastapi
from module.flask.main import start_flask


@click.group()
def click_service():
    pass


@click_service.command("flask")
def start_api_rest():
    start_flask()


@click_service.command("fastapi")
def start_api_rest():
    start_fastapi()
