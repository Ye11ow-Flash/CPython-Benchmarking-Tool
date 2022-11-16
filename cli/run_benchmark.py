import typer
from rich import print

from . import app


@app.command(
    "run",
    context_settings={"allow_extra_args": True, "ignore_unknown_options": True},
)
def run_benchmark(ctx: typer.Context):
    print("Running benchmark. ", flush=True, end="")
    print("The following will be passed to pyperformance", ctx.args)
