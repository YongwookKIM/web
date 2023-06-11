from django.http import HttpResponse


from django.shortcuts import render
from gangnam.models import Gangnam

def map(request):
    gangnam = Gangnam.objects.all()
    ctx = {'gangnam': gangnam}
    return render(request, 'kakaoapi/map.html', ctx)