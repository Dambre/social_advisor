from celery.decorators import periodic_task
from django.core import management
from celery.task.schedules import crontab
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)




@periodic_task(run_every=(crontab(minutes='*/5')), name='update_hash_scores', ingore_result=True)
def update_hash(): 
    logger.info("update_hash")
    management.call_command('update_hash')
