import click
import click_boilerplate.mysubgroup.main as mysubgroup
from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("click-boilerplate")
except PackageNotFoundError:
    __version__ = "0.0.0"  # fallback


@click.group()
@click.version_option(version=__version__, prog_name="click-boilerplate")
def root():
    """Main entry point for the CLI application."""


@root.command()
@click.option("--name", default="World", help="Name to greet.")
def hello(name):
    """Simple program that greets NAME for a given value."""
    click.echo(f"Hello {name}!")


@root.command()
def install_autocomplete():
    """Install autocomplete for the CLI."""
    click.echo("To enable autocomplete, generate the autocompletion script:")
    click.echo(
        "_CLICK_BOILERPLATE_COMPLETE=bash_source click-boilerplate >> ~/.click-boilerplate-completion"
    )
    click.echo("\nThen, add the following line to your .bashrc or .zshrc file:")
    click.echo("source ~/.click-boilerplate-completion")


# Add the subgroups to the root command
root.add_command(mysubgroup.mysubgroup)
