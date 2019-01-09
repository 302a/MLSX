import random

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def test1(request):
    code1 = str(random.randint(0, 9))
    code2 = str(random.randint(0, 9))
    code3 = str(random.randint(0, 9))
    code4 = str(random.randint(0, 9))
    lastcode = code1 + code2 + code3 + code4
    request.session['code'] = lastcode
    print(request.session.get('code'))
    data = {
        'ttt': lastcode
    }
    return JsonResponse(data)

def test2(request):
    tttt = request.session.get('code')
    data = {
        'tttt': tttt
    }
    return JsonResponse(data)