# -*- coding:UTF-8 -*-

from django.http import HttpResponse
from django.utils import simplejson

def assignment_list(request):
    return HttpResponse(simplejson.dumps({'xxx':'yyy'}),mimetype='application/json')