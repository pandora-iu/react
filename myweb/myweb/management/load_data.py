from csv import DictReader
from datetime import datetime

from django.core.management import BaseCommand

from 
from pytz import UTC

DATETIME_FORMAT = '%m/%d/%y %H:%H'


POINTS = [
    'product_name',
    'description',
    'cost',
]