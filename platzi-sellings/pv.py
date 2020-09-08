import click

@click.group()
@click.pass_context
def clie(ctx):
    ctx.obj = {}
    