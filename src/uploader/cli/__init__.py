"""Command line interface for uploader."""

import click

from ..storage import upload_images

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])


@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument("files", nargs=-1, type=click.Path(exists=True))
@click.option("-c", "--config", type=click.Path(exists=True), help="Config file.")
@click.version_option(version="0.0.1")
def cli(files, config):
    """uploader command line interface."""
    click.echo(files)
    # ('setup.py', 'setup.cfg', 'README.md')
    click.echo(config)

    upload_images(files, config)

    # Upload
    # Success:
    # http://remote-image-1.png
    # http://remote-image-2.png

__all__ = ["cli"]
