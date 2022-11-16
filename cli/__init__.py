from __future__ import annotations

from typing import Any, Optional

import typer

from .utils import version_callback

app = typer.Typer(rich_markup_mode="rich")
from . import check_benchmark, run_benchmark

session_state: dict[str, Any] = {}

# Note: Typer Docs 👉 https://typer.tiangolo.com/


@app.callback(invoke_without_command=True)
def main(
    ctx: typer.Context,
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-V",
        callback=version_callback,
        help="Used to show users the current version",
    ),
):
    """Allows users to run python benchmarks. This program is built on top of pyperformance"""
    if ctx.invoked_subcommand is None:
        print("pass --help for more")
