from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'kakaoapi/map.html')


def showattractions(request):
    with open('kakaoapi/testgong.json', encoding='utf-8') as json_file:
        attractions = json.load(json_file)['response']['body']['items']['item']

    attractiondict = []
    for attraction in attractions:
        if attraction.get('mapx'):
            content = {
                "title": attraction['국소명'],
                "mapx": str(attraction['lon']),
                "mapy": str(attraction['lat']),
                "addr1": str(attraction['주소']),
            }
            attractiondict.append(content)
    attractionJson = json.dumps(attractiondict, ensure_ascii=False)
    return render(request, 'map/map.html', {'attractionJson': attractionJson})
