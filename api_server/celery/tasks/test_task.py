from celery.decorators import task


@task()
def return_ok():
    """Simple task for dummy schedule"""
    return "OK"