import json
import time
import urllib.request
import sys
from kafka import KafkaProducer
#Treat Argument Values as List
import argparse

# addargument = False
ListArgument = []
# try:
#     parser = argparse.ArgumentParser(description='A test program.')

#     parser.add_argument("-p", "--print_string", help="Prints the supplied argument.", nargs='*')

#     argv = parser.parse_args()
#     addargument = argv
   
# except:
#     print("no arguments")




producer = KafkaProducer(bootstrap_servers="localhost:9092")
while True:
    Pregnancies = input("enter Pregnancies : ")
    ListArgument.append(Pregnancies)
    print(Pregnancies)
    Glucose = input("enter Glucose : ")
    ListArgument.append(Glucose)
    print(Glucose)
    BloodPressure = input("enter BloodPressure : ")
    ListArgument.append(BloodPressure)
    print(BloodPressure)
    SkinThickness = input("enter SkinThickness : ")
    ListArgument.append(SkinThickness)
    print(SkinThickness)
    Insulin = input("enter Insulin : ")
    ListArgument.append(Insulin)
    print(Insulin)
    Bmi = input("enter BMI : ")
    ListArgument.append(Bmi)
    print(Bmi)
    DiabetesPedigreeFunction = input("enter DiabetesPedigreeFunction : ")
    ListArgument.append(DiabetesPedigreeFunction)
    print(DiabetesPedigreeFunction)
    Age = input("enter Age : ")
    ListArgument.append(Age)
    print(Age)
#     for arg in ListArgument:
#         producer.send("diabete", json.dumps(arg).encode())
#    # print("{} Produced {} station records".format(time.time(), len(stations)))
#     print("{} Produced  ".format(time.time()))
    producer.send("diabete", json.dumps(ListArgument).encode())
#    # print("{} Produced {} station records".format(time.time(), len(stations)))
    print("{} Produced  ".format(time.time()))
    ListArgument =[]
    time.sleep(2)
    
def input():
    Pregnancies = input("enter Pregnancies : ")
    ListArgument.append(Pregnancies)
    print(Pregnancies)
    Glucose = input("enter Glucose : ")
    ListArgument.append(Glucose)
    print(Glucose)
    BloodPressure = input("enter BloodPressure : ")
    ListArgument.append(BloodPressure)
    print(BloodPressure)
    SkinThickness = input("enter SkinThickness : ")
    ListArgument.append(SkinThickness)
    print(SkinThickness)
    Insulin = input("enter Insulin : ")
    ListArgument.append(Insulin)
    print(Insulin)
    Bmi = input("enter BMI : ")
    ListArgument.append(Bmi)
    print(Bmi)
    DiabetesPedigreeFunction = input("enter DiabetesPedigreeFunction : ")
    ListArgument.append(DiabetesPedigreeFunction)
    print(DiabetesPedigreeFunction)
    Age = input("enter Age : ")
    ListArgument.append(Age)
    print(Age)
    

# else:
#     print(ListArgument.print_string)
#     Pregnancies = ListArgument.print_string[0]
#     Glucose = ListArgument.print_string[1]
#     BloodPressure = ListArgument.print_string[2]
#     SkinThickness = ListArgument.print_string[3]
#     Insulin = ListArgument.print_string[4]
#     Bmi = ListArgument.print_string[5]
#     DiabetesPedigreeFunction = ListArgument.print_string[6]
#     Age = ListArgument.print_string[7]

#//////////////////////////////////////////////////
# API_KEY = "d5c3fb4036213e83c0a60fd2325abad61910f268" # FIXME Set your own API key here
# url = "https://api.jcdecaux.com/vls/v1/stations?apiKey={}".format(API_KEY)

# producer = KafkaProducer(bootstrap_servers="localhost:9092")

# while True:
#    # response = urllib.request.urlopen(url)
#    # stations = json.loads(response.read().decode())
#     for station in range(1,10):
#         producer.send("diabete", json.dumps(station).encode())
#         time.sleep(1)
#    # print("{} Produced {} station records".format(time.time(), len(stations)))
#     print("{} Produced  ".format(time.time()))
#     time.sleep(2)
