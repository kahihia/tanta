from django.conf import settings


def mixpanel(request):
	return {'mixpanel':settings.MIXPANEL_TOKEN}