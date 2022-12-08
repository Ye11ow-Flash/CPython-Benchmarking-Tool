import typer
from rich import print

from . import app


@app.command(
    "status",
    context_settings={"allow_extra_args": True, "ignore_unknown_options": True},
)
def check_benchmark(ctx: typer.Context):
    print("benchmark in progress")
