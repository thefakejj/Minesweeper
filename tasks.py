from invoke import task


@task
def start(ctx):
    ctx.run("python3 src/index.py", pty=True)

#coverage stuff

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src", pty=True)

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html", pty=True)

#testing

@task
def test(ctx):
    ctx.run("pytest src", pty=True)