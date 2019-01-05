from celery.schedules import crontab

CELERY_BEAT_SCHEDULE = {
    'dummy-schedule': {
        'task': 'api_server.celery.tasks.test_task.return_ok',
        'schedule': crontab(minute='*/15'),
    },
    'sync-exchange-rates': {
        'task': 'api_server.celery.tasks.exchange_rates. get_exchange_rates',
        'schedule': crontab(hour='*/24'),
    },