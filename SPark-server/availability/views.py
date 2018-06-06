from django.http import HttpResponse

from django.http import JsonResponse
from .models import Spot,AvailableTime
from .pricePrediction import pricePredictor

def update(request):
    '''sensor update the availability'''
    available=request.GET.get("available",True)
    carPlate=request.GET.get("car",False)
    spotID=request.GET.get("spotID",False)

    if spotID != False:
        try:
            s=Spot.objects.get(spotID=spotID)
        except:
            return HttpResponse("sensor is not registered")

        s.isAvailableNow= True if available =='1' else False
        s.currentCar=carPlate.lower()
        s.save()

        return HttpResponse(s.isAvailableNow)
    else:
        return HttpResponse("fail to update database")

def retrieve(request):
    '''user retrieve a spot to park'''

    request.GET.get("position", False)

    s=Spot.objects.filter(isAvailableNow=True)
    response_data = {}

    num_available = len(s)
    num_total=Spot.objects.all().count()

    utilization_rate=(num_total-num_available)/num_total

    pp=pricePredictor()

    # get a spot
    response_data = {}
    response_data['position'] = s[0].position
    response_data['price'] = float(pp.get_price(utilization_rate))
    response_data['spotID'] = '1'

    return JsonResponse(response_data)

def register(request):
    '''if sensor is not in the database then register'''
    spotID = request.GET.get("spotID", False)

    if spotID == False:
        return HttpResponse('fail to register')
    try:
        s=Spot.objects.get(spotID=spotID)
    except:
        s = Spot(spotID=spotID)
        s.save()

    return HttpResponse("registered")

def confirm(request):
    # get a spot

    response_data = {}

    response_data['result'] = True

    return JsonResponse(response_data);

def getCarPlate(request):
    # get a spot

    request.GET.get("spotID", False)

    return HttpResponse("123");