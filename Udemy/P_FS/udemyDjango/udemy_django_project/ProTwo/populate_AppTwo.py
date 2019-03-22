#!/usr/bin/env python
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')

import django
django.setup()

# Fake pop script
import random
from AppTwo.models import Users
from faker import Faker

fakegen = Faker()
# topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']
#
# def add_topic():
#     t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
#     t.save()
#     return t

def populate(N=5):
    for entry in range(N):
        #create data
        fake_mail = fakegen.email()
        fake_fname = fakegen.first_name()
        fake_lname = fakegen.last_name()

        # create the web-page entry
        user = Users.objects.get_or_create(user_first_name = fake_fname, user_last_name = fake_lname, email = fake_mail)[0]


if __name__ == '__main__':
    print("populating scrip!")
    populate(20)
    print("populating complete")

