import os
from dotenv import load_dotenv

load_dotenv()

CELERY = {
    'BROKER': os.environ.get('CELERY_BROKER')
}
