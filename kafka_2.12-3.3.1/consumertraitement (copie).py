import json
from kafka import KafkaConsumer
import matplotlib.pyplot as plt
import pickle
from kafka import KafkaProducer
import time
stations = {}
Listargument = []
filename = 'finalized_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))
consumer = KafkaConsumer("diabete", bootstrap_servers='localhost:9092', group_id="consumertraitement")
for message in consumer:
    arguments = json.loads(message.value.decode())
    Listargument.append(arguments)
    # define input
    new_input = [[float(arguments[0]),float(arguments[1]),float(arguments[2]),float(arguments[3]),float(arguments[4]),float(arguments[5]),float(arguments[6]),float(arguments[7])]]
    # get prediction for new input
    new_output = loaded_model.predict(new_input)
    # summarize input and output
    print("##################################################################")
    if new_output[0]==1.0 :
       print("tested_positive")
    else :
        print("tested_negative")
    Listargument=[]

#/////////////////////////////////////////////////:
producer = KafkaProducer(bootstrap_servers="localhost:9092")
while True:
    producer.send("diabete", json.dumps(ListArgument).encode())
#    # print("{} Produced {} station records".format(time.time(), len(stations)))
    print("{} Produced  ".format(time.time()))
    ListArgument =[]
    time.sleep(2)
  
    



   
