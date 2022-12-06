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


"""
(?) Benchmark ->  EC2 -> (wait) -> venv-set-up -> (gather information) -> run-tests -> return file



configurations.config -> links to repo, all the details you need

Benchmark (python3 run benchmark.py -pyperf) -> 

AMI -> EC2




run-tests
queu: {id: int, pid: int, status: str}



(CP1) -> CP1.01 -> CP1.02
    \             /
     CP1.new_change

1. Shapshot of machine
2. Launch EC2
3. EC2 headless 
4. Credentials 

Sunday
Mondays
Thursday

9am - 6pm 
Tuesday 22nd <-> 
Wed <2pm - 6pm>
Friday <10am - 3pm>
Saturdays(Optional)


janshah@cs.stonybrook.edu

Ph:- +1 646-727(5749)
DA: 646-465-3446




"""
