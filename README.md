# SPark

The goal of this project is to help people find and reserve a parking spot quickly and conveniently. In addition, apartment owners can earn money from their private parking spot when they are not at home. We believe the land utilization will also be increased by this solution.

## Features
* Developed a website which user can easier reserve a parking spot using their plate no.
* Deployed the web server in RESTful structure to provide the service including parking lot appointment. And using linear regression technique to adjust the price.
* Built the circuit with IoT hardware so that it can detect the incoming car and compare the actual plate number with the plate number received from the server. Then make different responses and interact with the server.

## Requirements
* Python
* Django
* Raspberry pi
* Scikit-learn

## How To run:

#### To run the SPark server you will have to run below command on your terminal at project folder
``` bash 
# run the server
python SPark-server/manage.py runserver
``` 

#### Website
The website will run in port 8080: <br/>
 localhost:8080/ <br/>
 **To make sure Google Map Run correctly, you have to use https instead of http, and enable location in your browser.** <br/>
 if you have published your website, you have to obtain certificate for your website.

## Files
The project contains three different part of codes:

1. RPI:car sensor

2. backend:define the database and AJAX API

3. frontend:webpage
**All webpages should located in the template/ under backend  directory**
