import urllib.request
import ssl


def updateSensorStats(spotID=1,available=1,carPlate='ABC'):
    href="http://stoneparse.com/availability/update/?"

    context = ssl._create_unverified_context()

    # parking lot name
    spotID=spotID

    # 1 means parking is available
    # 0 means not available
    available=available

    # current car in this parking lot
    carPlate=carPlate

    contents = urllib.request.urlopen(href+"available="+str(available)+"&car="+str(carPlate)+"&spotID="+str(spotID), context=context).read()
    return contents

def registerSensor(spotID=1):
    '''Spot need to register before it starts to update the database'''

    href = "http://stoneparse.com/availability/register/?"
    context = ssl._create_unverified_context()
    contents = urllib.request.urlopen(href+"spotID=" + str(spotID),context=context).read()
    return contents

def getCarPlate(spotID=1):
    ''' Send SpotID and get carPlate'''

    href = "http://stoneparse.com/availability/getplate/?"
    context = ssl._create_unverified_context()
    contents = urllib.request.urlopen(href+"spotID=" + str(spotID),context=context).read()
    return contents

if __name__ == "__main__":

    # Testing function
    print(updateSensorStats(spotID=1,available=1,carPlate='ABC'))
    print(getCarPlate(1))

    # print(registerSensor(spotID=1))