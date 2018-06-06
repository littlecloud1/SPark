import urllib.request


def updateSensorStats(spotID=1,available=1,carPlate='ABC'):
    href="http://stoneparse.com/availability/update/?"

    # parking lot name
    spotID=spotID

    # 1 means parking is available
    # 0 means not available
    available=available

    # current car in this parking lot
    carPlate=carPlate

    contents = urllib.request.urlopen(href+"available="+str(available)+"&car="+str(carPlate)+"&spotID="+str(spotID)).read()
    return contents

def registerSensor(spotID=1):
    '''Spot need to register before it starts to update the database'''

    href = "http://stoneparse.com/availability/register/?"
    contents = urllib.request.urlopen(href+"spotID=" + str(spotID)).read()
    return contents


if __name__ == "__main__":

    # Testing function
    print(updateSensorStats(spotID=1,available=1,carPlate='ABC'))

    print(registerSensor(spotID=1))