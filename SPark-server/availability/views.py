from django.http import HttpResponse
from django.http import JsonResponse

from .models import Spot
from .pricePrediction import pricePredictor


def update(request):
    '''sensor update the availability'''
    available = request.GET.get("available", True)
    carPlate = request.GET.get("car", False)
    spotID = request.GET.get("spotID", False)

    if spotID != False:
        try:
            s = Spot.objects.get(spotID=spotID)
        except:
            return HttpResponse("sensor is not registered")
        if s.isAvailableNow is not True and s.isBooked:
            s.isBooked=False
        s.isAvailableNow = True if available == '1' else False
        s.currentCar = carPlate.lower()
        s.save()

        return HttpResponse(s.isBooked)
    else:
        return HttpResponse("fail to update database")


def retrieve(request):
    '''user retrieve a spot to park'''

    request.GET.get("position", False)

    s = Spot.objects.filter(isAvailableNow=True, isBooked=False)

    num_available = len(s)
    num_total = Spot.objects.all().count()

    # get a spot
    response_data = {}
    if num_available != 0:
        pp = pricePredictor()
        utilization_rate = float(num_total - num_available) / float(num_total)
        response_data['position'] = s[0].position
        response_data['price'] = pp.get_price(utilization_rate)
        response_data['spotID'] = s[0].spotID
    else:
        response_data['position'] = '0'
        response_data['price'] = 0
        response_data['spotID'] = '0'

    return JsonResponse(response_data)


def register(request):
    '''if sensor is not in the database then register'''
    spotID = request.GET.get("spotID", False)

    if spotID == False:
        return HttpResponse('fail to register')
    try:
        s = Spot.objects.get(spotID=spotID)
    except:
        s = Spot(spotID=spotID)
        s.save()

    return HttpResponse("registered")


def confirm(request):
    # make reservation for a spot

    carPlate = request.GET.get("plate", False)
    spotID = request.GET.get("spotID", False)
    response_data = {}

    if spotID != False:

        try:
            s = Spot.objects.get(spotID=spotID)
            s.reservedCar = carPlate.lower()
            s.isBooked = True
            s.save()
            response_data['result'] = True
        except Exception as e:
            print(e)
            response_data['result'] = False
    else:
        response_data['result'] = False

    return JsonResponse(response_data);


def getCarPlate(request):
    # get reserved car plate

    spotID = request.GET.get("spotID", False)

    if spotID != False:
        try:
            s = Spot.objects.get(spotID=spotID)
        except:
            return HttpResponse("sensor is not registered")

        return HttpResponse(s.reservedCar)
    else:
        return HttpResponse("fail to update database")
