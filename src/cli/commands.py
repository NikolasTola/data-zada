"""
Comandos CLI do Data-Zada
"""

import click
from configs import PROJECT_NAME, PROJECT_VERSION


@click.group()
@click.version_option(version=PROJECT_VERSION, prog_name=PROJECT_NAME)
def cli():
    """Data-Zada - Data Infrastructure as Code"""
    pass


@cli.command()
def test():
    """Comando de teste"""
    click.echo("Está funcionando")