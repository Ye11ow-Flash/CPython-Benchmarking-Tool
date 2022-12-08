import os
import pathlib
import subprocess
import typing

import typer

__version__ = "0.1.0"


def version_callback(value: bool):
    if value:
        print(f"Benchmarks CLI Version: {__version__}")
        raise typer.Exit()
