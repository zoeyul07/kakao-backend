import csv
import os
import django
import sys

os.chdir(".")
print("Current dir=", end=""), print(os.getcwd())

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print("BASE_DIR=", end=""), print(BASE_DIR)

sys.path.append(BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_1st.settings")
django.setup()

from product.models import *

CSV_PATH = './themes.csv'

with open(CSV_PATH, newline='') as csvfile:
    data_reader = csv.DictReader(csvfile)

    for row in data_reader:
        print(row)
        Theme.objects.create(
            name = row['name'],
            main_image_url = row['main_image_url'],
            detail_image_url = row['detail_image_url'],
            description = row['description']
        )

