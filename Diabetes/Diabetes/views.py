import json
import time
import urllib.request
import sys
from kafka import KafkaProducer
#Treat Argument Values as List
import argparse
import os
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
   # return HttpResponse("<h1>Bonjour ,bienvenue sur mon site</h1>")
   return render(request, "index.html")

def getprediction(request):
    if(request.POST):
        Listarguments = []
        login_data = request.POST.dict()
        print(login_data)
        Pregnancies = login_data.get("Pregnancies")
        Glucose = login_data.get("Glucose")
        BloodPressure = login_data.get("BloodPressure")
        SkinThickness = login_data.get("SkinThickness")
        Insulin = login_data.get("Insulin")
        BMI = login_data.get("BMI")
        DiabetesPedigreeFunction = login_data.get("DiabetesPedigreeFunction")
        Age = login_data.get("Age")
        #user_type = login_data.get("user_type")
        print(request)
        print(Pregnancies, Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age)
        Listarguments=[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]
        producer = KafkaProducer(bootstrap_servers="localhost:9093")
        producer.send("djangofastapi", json.dumps(Listarguments).encode())
        print("{} Produced  ".format(time.time()))
        time.sleep(4)
        resultat = "1"
        os
        fichier = open("/home/mahjoubi/Documents/kafka/Diabetes/Diabetes/static/data.txt")
        resultat = fichier.read()
        fichier.close()
        print("resultat : "+resultat)
        if resultat!="1":
            
            os.remove("/home/mahjoubi/Documents/kafka/Diabetes/Diabetes/static/data.txt")
            return render(request, "index.html",context={"resultat":resultat})
        else :
            os.remove("/home/mahjoubi/Documents/kafka/Diabetes/Diabetes/static/data.txt")
            return render(request, "resultat.html")
    else:
        return render(request, "index.html")
def resultat(request):
    return render(request, "resultat.html")