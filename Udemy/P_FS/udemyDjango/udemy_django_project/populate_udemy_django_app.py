#!/usr/bin/env python
import os
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'udemy_django_project.settings')
#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'udemy_django_project.settings')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'udemy_django_project.settings')

import django
django.setup()

# Fake pop script
import random
from udemy_django_app.models import AccessRecord, Webpage, Topic
from faker import Faker

fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):

        # get the topic to the entry
        top = add_topic()

        #create data
        fake_url = fakegen.url()
        fake_data = fakegen.data()
        face_name = fakegen.company()

        # create the web-page entry
        webpage = Webpage.objects.get_or_create(topic = top, url = fake_url, name = face_name)[0]


        #create a fake access record
        acc_rec = AccessRecord.objects.get_or_create(name=webpage, data = fake_data)[0]

    if __name__ == '__main__':
        print("populating scrip!")
        populate(20)
        print("populating complete")

