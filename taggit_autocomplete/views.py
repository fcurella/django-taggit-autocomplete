from django.http import HttpResponse
from taggit.models import Tag
try:
    from django.utils import simplejson as json
except ImportError:
    import json

from django.utils.datastructures import MultiValueDictKeyError

def list_tags(request):
	try:
		tags = Tag.objects.filter(name__istartswith=request.GET['q']).values_list('name', flat=True)
		data = [{'value': t, 'name': t} for t in tags]
	except MultiValueDictKeyError:
		data = []
	
	return HttpResponse(json.dumps(data), mimetype='application/json')
