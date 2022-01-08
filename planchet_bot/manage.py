import typer

from planchet_bot.bot import updater


app = typer.Typer()


@app.command()
def run():
    """
    Start bot
    """
    updater.start_polling()


@app.callback()
def callback():
    pass


def main():
    app()


if __name__ == '__main__':
    main()
