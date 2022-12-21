import settings
from datetime import datetime


def getTimestamp():
    timestamp = datetime.now()
    return timestamp.strftime(settings.TIMESTAMP_FORMAT_CODE)
