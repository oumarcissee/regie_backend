# celery.py

from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Définissez le module de configuration Celery (utilisé pour la configuration Django)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

app = Celery('project')

# Chargez la configuration Celery depuis les paramètres Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Chargez les tâches de manière automatique depuis tous les modules "tasks.py" de votre projet
app.autodiscover_tasks()

# Nouvelle option pour activer la reconnexion au broker au démarrage
app.conf.broker_connection_retry_on_startup = True

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
