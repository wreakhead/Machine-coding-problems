from models.parking_lot_model import *
from service.outputFormaters import *
from service.parkVehicle_driver import*
from service.displayMethod_driver import*
from service.unparkVehicle_driver import *
from service.__print import Print__, logTime,endLog



def startService():

    # create parking lot 
    method,id,no_floors,slots = input().strip().split()
    no_floors = int(no_floors)
    slots = int(slots)

    
    logTime()
    if method == 'create_parking_lot':
        new_parking_lot = parkingLot(id,no_floors,slots)
        Print__("Created parking lot with "+str(no_floors)+ " floors and "+str(slots)+ " slots per floor")

        inputStream = ""

        while inputStream != "exit":
            inputStream = input().strip()

            stream = inputStream.split()

            if stream[0] == "display":
                displayMethod_driver(stream,new_parking_lot)
            elif stream[0]== "park_vehicle":
                parkVehicle_driver(stream,new_parking_lot)
            elif stream[0] == "unpark_vehicle":
                unparkVehicle_driver(stream,new_parking_lot)
            elif inputStream == 'exit':
                break    
            else:
                Print__("Invalid method")  
        endLog()          
                
                
                    


    else:
        Print__("Invalid method")    


