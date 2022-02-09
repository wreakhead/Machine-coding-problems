from service.__print import Print__

def output_free_count(level,slot,type):
    Print__("No. of free slots for "+str(type) +" on Floor "+ str(level)+":"+ str(slot))


def output_free_slots(type,floor):
    output="Free slots for "+type+" on Floor "+ str(floor.level)+": "
    empty_slots = ""
    if type == 'CAR':
        for i in range(3,len(floor.slots_data)):
            if floor.slots_data[i] == None:
                empty_slots +=","+str(i+1)


    elif type == 'BIKE':
        for i in range(1,3):
            if floor.slots_data[i] == None:
                empty_slots +=","+str(i+1)

    elif type == 'TRUCK':
        if floor.slots_data[0] == None:
            empty_slots +=","+str(1)

    Print__(output+empty_slots[1:])
    

def output_occupied_slots(type,floor):
    output="Occupied slots for "+type+" on Floor "+ str(floor.level)+": "
    occupied_slots = ""
    if type == 'CAR':
        for i in range(3,len(floor.slots_data)):
            if floor.slots_data[i] != None:
                occupied_slots +=","+str(i+1)


    elif type == 'BIKE':
        for i in range(1,3):
            if floor.slots_data[i] != None:
                occupied_slots +=","+str(i+1)

    elif type == 'TRUCK':
        if floor.slots_data[0] != None:
            occupied_slots +=","+str(1)

    Print__(output+occupied_slots[1:])


def output_parked(ticket):
    Print__("Parked vehicle. Ticket ID: "+ticket)

def output_unparked(details):
    Print__("Unparked vehicle with Registration Number:" +str(details.register_no)+" and Color: "+details.color)    
