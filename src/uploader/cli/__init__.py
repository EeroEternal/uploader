"""Command line interface for uploader."""

import click


CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])


@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument("files", nargs=-1, type=click.Path(exists=True))
@click.version_option(version="0.0.1")
def cli(files):
    """uploader command line interface."""
    click.echo(files)
    # ('setup.py', 'setup.cfg', 'README.md')


__all__ = ["cli"]
