import numpy as np

# Define the rooms and states
rooms = np.array(['A', 'B'])
states = np.array(['Clean', 'Dirty'])

def choose_room():
    return str(np.random.choice(rooms))

def choose_state():
    return str(np.random.choice(states))

def clean_rooms():
    room_states = {} 
    for room in rooms:
        room_states[str(room)] = choose_state()
    print(f'Initial Room States: {room_states}')    

    vaccum_pos = choose_room()
    print('Current Position:', vaccum_pos)
    print('========================')
    
    cost = 0
    
    for i in range(len(rooms)):
        if room_states[vaccum_pos] == 'Dirty':
            print(f'{vaccum_pos} is dirty.')
            print(f'Cleaning {vaccum_pos}')
            room_states[vaccum_pos] = 'Clean'
            print(f'{vaccum_pos} is cleaned.')
            print('========================')
            cost += 1
        else:
            print(f'{vaccum_pos} is clean.') 
            print('No operation') 
            print('========================')
        
        # Move to the other room
        another_room = list(set(rooms) - {vaccum_pos})
        vaccum_pos = str(another_room[0])
        
        # Increment cost for moving to the next room
        if i == 0:
            cost += 1
       
    print(f'Final States: {room_states}') 
    print('Both rooms are cleaned, stop')
    print(f'Cost: {cost}')
         
clean_rooms()
