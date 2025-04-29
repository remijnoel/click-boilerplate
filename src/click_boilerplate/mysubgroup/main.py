import click


@click.group()
def mysubgroup():
    """A group of commands for mysubcommand."""


@mysubgroup.command()
def subcommand():
    """A subcommand that does something."""
    click.echo("This is a subcommand.")
