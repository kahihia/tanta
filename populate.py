import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Tanta.settings')

import django
django.setup()

## FAKE POP SCRIPTS
import random
from home_page.models import AccessRecord,Webpage,Topic
from faker import Faker

fakegen=Faker()
topics=['Search','Social','Marketplace','News','Games']

def add_topic():
	t=Topic.objects.get_or_create(top_name=random.choice(topics))[0]
	t.save()
	return t

def populate(N=5):

	for entry in range(N):
		# Get topic
		top=add_topic()

		# Create data
		fake_url=fakegen.url()
		fake_date=fakegen.date()
		fake_name=fakegen.company()
		# Create the webpage entry
		webpg=Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

		 # Create fake access record for webpage
		acc_rec=AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]

if __name__ == '__main__':
	print("populating script!")
	populate(20)
	print("populating complete!")