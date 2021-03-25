from invoke import task

@task
def test(ctx):
    ctx.run("pytest /home/karhelmi/Documents/Ohjelmistotekniikka/ot-harjoitustyo/laskarit/viikko2/maksukortti/src")


@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest /home/karhelmi/Documents/Ohjelmistotekniikka/ot-harjoitustyo/laskarit/viikko2/maksukortti/src")

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html")
