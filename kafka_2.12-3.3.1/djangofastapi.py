import json
from kafka import KafkaConsumer
import matplotlib.pyplot as plt
import pickle
from kafka import KafkaProducer
import time
# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
stations = {}
Listargument = []
filename = 'finalized_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))
consumer = KafkaConsumer("djangofastapi", bootstrap_servers='localhost:9093', group_id="djangofastapi")
print(consumer)
for message in consumer:
    print("dddddddddddddddddddddddddddddddddddddddddddd")
    arguments = json.loads(message.value.decode())
    print("FFFFFFFFFFFFFFFFFFFFF")
    print(arguments)
    Listargument.append(arguments)
    # define input
    new_input = [[float(arguments[0]),float(arguments[1]),float(arguments[2]),float(arguments[3]),float(arguments[4]),float(arguments[5]),float(arguments[6]),float(arguments[7])]]
    # get prediction for new input
    new_output = loaded_model.predict(new_input)
    # summarize input and output
    print("##################################################################")
    if new_output[0]==1.0 :
       fichier = open("/home/mahjoubi/Documents/kafka/Diabetes/Diabetes/static/data.txt",'w')
       fichier.write("test_positive")
       fichier.close()
       print("tested_positive")
    else :
        fichier = open("/home/mahjoubi/Documents/kafka/Diabetes/Diabetes/static/data.txt",'w')
        fichier.write("test_negative")
        fichier.close()
        print("tested_negative")
    Listargument=[]

#/////////////////////////////////////////////////:
# producer = KafkaProducer(bootstrap_servers="localhost:9092")
# while True:
#     producer.send("diabete", json.dumps(ListArgument).encode())
# #    # print("{} Produced {} station records".format(time.time(), len(stations)))
#     print("{} Produced  ".format(time.time()))
#     ListArgument =[]
#     time.sleep(2)
  
    



   
