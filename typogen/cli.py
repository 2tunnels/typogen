import click

import typogen


@click.command()
@click.argument('text')
@click.option('--skip-letter', is_flag=True)
@click.option('--double-letter', is_flag=True)
@click.option('--reverse-letters', is_flag=True)
@click.option('--skip-spaces', is_flag=True)
@click.option('--missed-key', is_flag=True)
@click.option('--inserted-key', is_flag=True)
def main(text, **kwargs):
    all_typos = not kwargs['skip_letter'] and \
                not kwargs['double_letter'] and \
                not kwargs['reverse_letters'] and \
                not kwargs['skip_spaces'] and \
                not kwargs['missed_key'] and \
                not kwargs['inserted_key']

    if all_typos or kwargs['skip_letter']:
        for typo in typogen.skip_letter(text):
            click.echo(typo)

    if all_typos or kwargs['double_letter']:
        for typo in typogen.double_letter(text):
            click.echo(typo)

    if all_typos or kwargs['reverse_letters']:
        for typo in typogen.reverse_letters(text):
            click.echo(typo)

    if all_typos or kwargs['skip_spaces']:
        for typo in typogen.skip_spaces(text):
            click.echo(typo)

    if all_typos or kwargs['missed_key']:
        for typo in typogen.missed_key(text):
            click.echo(typo)

    if all_typos or kwargs['inserted_key']:
        for typo in typogen.inserted_key(text):
            click.echo(typo)
