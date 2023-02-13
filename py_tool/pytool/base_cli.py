#!/usr/bin/python
# -*-coding:utf-8-*-

"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: base_cli.py
@time: 2023/2/13 0:00
"""
import click
from rich.console import Console


from pytool import db_cli, file_cli
from colorama import Fore

console = Console()
@click.group()
def cli():
    pass


@cli.command()
def c():
    print(f"{Fore.CYAN}颜色字符")
    console.print("Hello", "World!")
    console.print("Hello", "World!", style="bold red")
    console.print("Where there is a [bold cyan]Will[/bold cyan] there [u]is[/u] a [i]way[/i].")


@cli.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
def main(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo('Hello %s!' % name)


cli.add_command(cmd=db_cli.db)
cli.add_command(cmd=file_cli.file_cli)