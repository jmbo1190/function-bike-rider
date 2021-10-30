#!/usr/bin/env python
import click
from hello import marco
import sys

@click.command()
@click.option('--name')
def callmarco(name):
    """ CLI call to function marco() \n
        usage: \n
           hellocli.py --name "Marco"\n
           hellocli.py --help
    """
    result = marco(name)
    if result != "Polo":
        click.echo(click.style(f'{result}', bg='red'))
        sys.exit(1)  # Exit with status 1 - can be displayed in Linux with 'echo $?'
        # return True
    #click.echo(result)
    click.echo(click.style(f'{result}', bg='green')) 
    # return True
    # normal exit with status 0

if __name__ == '__main__':
    #pylint: disable=no-value-for-parameter
    callmarco()

