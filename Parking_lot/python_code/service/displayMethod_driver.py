
from service.outputFormaters import *
from service.__print import Print__

def displayMethod_driver(stream,parking_lot):

    if stream[1] == "free_count":
        for floor in parking_lot.floors_data:
            slotSize = parking_lot.slots
            free_slots=0
            if stream[2] == 'CAR':
                for i in range(3,slotSize):
                    if floor.slots_data[i] == None:
                        free_slots+=1

                output_free_count(floor.level,free_slots,stream[2])
                

            elif stream[2] == 'BIKE':

                for i in range(1,3):
                    if floor.slots_data[i] == None:
                        free_slots+=1

                output_free_count(floor.level,free_slots,stream[2])

            elif stream[2] == 'TRUCK':
                    if floor.slots_data[0] == None:
                        free_slots=1
                    
                    output_free_count(floor.level,free_slots,stream[2])
            else:
                Print__("Invalid vehicle")        

    elif stream[1] =="free_slots":

        for floor in parking_lot.floors_data:
            output_free_slots(stream[2],floor)


    elif stream[1] =="occupied_slots":
         for floor in parking_lot.floors_data:
            output_occupied_slots(stream[2],floor)

    else:
         Print__( "Invalid method")