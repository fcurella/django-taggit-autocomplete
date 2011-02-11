from django.http import HttpResponse
from django.core import serializers
from taggit.models import Tag
import simplejson

def list_tags(request):
	try:
		tags = Tag.objects.filter(name__istartswith=request.GET['q']).values_list('name', flat=True)
		data = [{'value': t, 'name': t} for t in tags]
	except MultiValueDictKeyError:
		pass
	
	return HttpResponse(simplejson.dumps(data), mimetype='application/json')
