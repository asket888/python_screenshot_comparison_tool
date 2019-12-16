from invoke import task


@task
def run(context, env='USA'):
    """
    Create new project with several flights on chosen environment
    :param context: invoke context object
    :param env: run on specific environment (USA, LAT, RUS); default value = USA
    :keyword: '$ invoke run'
    :keyword: '$ invoke run --env=RUS'
    """
    invoke_cmd = f'python run.py {env}'
    context.run(invoke_cmd)
