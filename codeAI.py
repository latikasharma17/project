pip install numpy

# Define the environment matrix
environment = np.array([
    ['P', 'B', '', ''],
    ['', '', 'W', ''],
    ['', 'G', '', ''],
    ['', '', '', ''],
])

# Define the knowledge matrix, initialized with all rooms unknown
knowledge = np.array([
    ['?', '?', '?', '?'],
    ['?', '?', '?', '?'],
    ['?', '?', '?', '?'],
    ['?', '?', '?', '?'],
])

# Define the current position of the agent
current_pos = (0, 0)

# Initialize the list of visited rooms
visited_rooms = []

# Define a function to update the knowledge matrix based on the environment matrix
def update_knowledge(current_pos, environment, knowledge):
    # Get the state of the current room from the environment matrix
    state = environment[current_pos]
    
    # Update the knowledge matrix with the state of the current room
    knowledge[current_pos] = state
    
    # If the current room contains a pit or a Wumpus, mark all adjacent rooms as unsafe
    if 'P' in state or 'W' in state:
        x, y = current_pos
        if x > 0:
            knowledge[x-1][y] = 'U'
        if x < 3:
            knowledge[x+1][y] = 'U'
        if y > 0:
            knowledge[x][y-1] = 'U'
        if y < 3:
            knowledge[x][y+1] = 'U'
    
    return knowledge

# Define a function to decide on the next room to be visited
def decide_next_room(current_pos, knowledge):
    # Get the state of the current room from the knowledge matrix
    state = knowledge[current_pos]
    
    # If the current room contains gold, return None to signal the end of the game
    if 'G' in state:
        return None
    
    # Check if all adjacent rooms are unsafe
    x, y = current_pos
    unsafe_count = 0
    if x > 0 and knowledge[x-1][y] == 'U':
        unsafe_count += 1
