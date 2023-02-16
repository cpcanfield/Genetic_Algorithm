'''
Graph Miner
Theresa Rumoro, Caroline Canfield, Emily Walden

SUMMARY -----------------------------------------------------------------------------------------------------------------------
'''

# Import needed libraries
from cgi import test
from turtle import color
import igraph as graph
import matplotlib.pyplot as plot
import math
import random
#how do we take care of the space?
# Line not visible in 1-5 because 1-5, 2-5, 1-5
# https://appdividend.com/2021/06/21/how-to-read-file-into-list-in-python/#:~:text=To%20read%20a%20file%20into,text%20file%20into%20a%20list.

#FIX FILE, ADD TWO LINES

test_nodes = []
node_graph = graph.Graph()
nodes = []
user_nodes = []
population = []
generation_counter = 0


def parse_graph():
    #open the file
    open_file = open("graph_data.txt", "r")
    #holds all the nodes once file is read
    global nodes
    nodes = []
    #keeps track while traversing in the loop
    tracker = 0
    #begin traversing
    while True:
        #holds each node at each line
        node_index = []
        #open the file
        line = open_file.readline()
        #if the line is empty
        if(line == ''):
            break
        #if the first vertex is a single digit number
        if(line[1] == ' ' ):
            #if the second vertex on the line is a single digit number
            if(line[3] == ' '):
                #create the nodes out of the first correct indexes
                node1 = line[0]
                node2 = line[2]
                node_1 = int(node1)
                node_2 = int(node2)
                node_index.append(node_1)
                node_index.append(node_2)
            else: #if the second vertex on the line is a double digit number
                node1 = line[0]
                node2 = line[2] + line[3]
                node_1 = int(node1)
                node_2 = int(node2)
                node_index.append(node_1)
                node_index.append(node_2)
        #if the first number is double digit and the second number is single
        elif(line[4] == ''):
            node1 = line[0] + line [1]
            node2 = line[3]
            node_1 = int(node1)
            node_2 = int(node2)
            node_index.append(node_1)
            node_index.append(node_2)
        else: #if the first number is double digit and the second number is double too
            node1 = line[0] + line [1]
            node2 = line[3] + line[4]
            node_1 = int(node1)
            node_2 = int(node2)
            node_index.append(node_1)
            node_index.append(node_2)
        #append to the array
        nodes.append(node_index)
        tracker += 1
        if not line:
            break
    #close file
    open_file.close()
    # return length



'''
create_graph creates the graph with the vertices and edges and highlights paths.
'''
def create_graph(path_nodes):
    # Call global nodes and node_graph
    global nodes
    global node_graph
    global generation_counter
    # Set counter equal to 0
    counter = 0
    # Create an empty list called test_nodes
    test_nodes = []
    # While counter is less than path_nodes, append the counter index path_nodes to test_nodes and increment counter
    while (counter < len(path_nodes)):
        test_nodes.append(path_nodes[counter])
        counter += 1
    # Find the length of the nodes list
    length = len(nodes)
    # Divide the length by 2 because we are only focused on the lines and not the amount of data
    length /= 2
    # Round down for the length
    length = math.floor(length)
    # Create the edges using the global nodes, which includes the pathways between the nodes
    edges = nodes
    # Create a graph using igraph with the length and edges as parameters
    node_graph = graph.Graph(length, edges)
    # Set empty list called name to label the nodes
    name = []
    # Set counter equal to zero
    counter = 0
    # While the counter is less than or equal to the length, append the counter value to name and increment counter
    while (counter <= len(nodes)):
        # Append the counter
        name.append(counter)
        #Increment the counter
        counter += 1
    # Using the vertex sequence property, name each node using the name list
    node_graph.vs["Node Labels"] = name
    # Create the variable path to be an empty list
    path = []
    # Set node counter equal to 0
    node_counter = 0
    # While loop that confirms that the node_counter is less than or equal to the length of the nodes list
    while (node_counter <= len(nodes)):
        # If the length of the test_nodes is 0
        if (len(test_nodes) == 0):
            # While the node_counter is less than or equal to the length of the name list
            while (node_counter <= len(name)):
                # Append 0 and increment node_counter
                path.append(0)
                node_counter += 1
        # If the test_nodes at index 0 equals 1
        elif (test_nodes[0] == 1):
            # Append the nodes value to path, pop the first value from test_nodes and increment node_counter
            path.append(nodes[node_counter])
            test_nodes.pop(0)
            node_counter += 1
        # If the test_nodes at index 0 equals 0
        elif (test_nodes[0] == 0):
            # Append the nodes value to path, pop the first value from test_nodes and increment node_counter
            path.append(0)
            test_nodes.pop(0)
            node_counter += 1
        # Else, append 0 and add to node_counter
        else:
            path.append(0)
            node_counter += 1
    # Using the edge sequence property, assign the value of the edge using the path list
    node_graph.es["Edge Color"] = path
    # Sort the user_nodes list
    user_nodes.sort()
    # Copy the user_nodes list to wanted_nodes
    wanted_nodes = user_nodes.copy()
    # Create the variable user_node_path to be an empty list
    user_node_path = []
    # Set node_counter equal to 0
    node_counter = 0
    # Set the test_counter equal to 0
    test_counter = 0
    # While loop that confirms that the node_counter is less than or equal to the length of the nodes list
    while (node_counter <= len(nodes)):
        # If length of wanted_nodes is 0
        if (len(wanted_nodes) == 0):
            # While the node_counter is less than or equal to the length of the name list
            while (node_counter <= len(name)):
                # Append 0 and increment node_counter
                user_node_path.append(0)
                node_counter += 1
        # If the value in the name node_counter index equals the value in the wanted_nodes test_counter index
        elif (name[node_counter] == wanted_nodes[test_counter]):
            # Append 1 to the user_node_path, pop the first value from wanted_nodes, and increment node_counter
            user_node_path.append(1)
            wanted_nodes.pop(0)
            node_counter += 1
        # If the value in the name node_counter index is not equal to the value in the wanted_nodes test_counter index
        elif (name[node_counter] != wanted_nodes[test_counter]):
            # Appen 0 to the user_node_path and increment node_counter
            user_node_path.append(0)
            node_counter += 1
        # Else, append 0 to user_node_path and increment node_counter
        else:
            user_node_path.append(0)
            node_counter += 1
    # Using the vertex sequence property, assign the value of the vertex using the user_node_path list
    node_graph.vs["Vertex Color"] = user_node_path
    # Use the matplotlib library to create the graph and set the size of the new window to 8 by 8
    graph_visual, size = plot.subplots(figsize=(8,8))
    # Use matplotlib library to make the graph unique
    graph.plot(
        # Call node_graph
        node_graph,
        # Set the target to size, which shows where the graph should be drawn
        target = size,
        # Make the vertex size equal to 0.2
        vertex_size = 0.2,
        # Create the color of the vertex to be purple or yellow if it is one of the user's nodes
        vertex_color = ["#C576F6" if user_node_path == 0 else "#FDDA0D" for user_node_path in node_graph.vs["Vertex Color"]],
        # Create the outline of the vertex to be purple or yellow if it is one of the user's nodes
        vertex_frame_color = ["#C576F6" if user_node_path == 0 else "#FDDA0D" for user_node_path in node_graph.vs["Vertex Color"]],
        # Label each node
        vertex_label = node_graph.vs["Node Labels"],
        # Create the size of the label to be 13
        vertex_label_size = 13.0,
        # Create the edge color to be purple or yellow if it is one of the connections to create the path
        edge_color = ["#C576F6" if path == 0 else "#FDDA0D" for path in node_graph.es["Edge Color"]]
    )
    # Print the graph for the user
    plot.show()
    # Save the graph as a pdf with each labeled generation
    generation_counter = str(generation_counter)
    graph_visual.savefig("Generation_" + generation_counter + ".pdf")



 #creates all possible solutions initially
def initial_population():
     global population
     tracker = 0
     #generates 1000 individuals
     while(tracker < 500):
         #create array to store new individual
         individual = []
         tracker_2 = 0
         #iterate through individual and assigns 0 or 1 to each index
         #want individual to be the same size of nodes because it represents
         #if edges are present in the solution
         while(tracker_2 < len(nodes)):
             #for each index of individual assign 0 or 1 by calling coin_toss
             individual.append(coin_toss())
             tracker_2+=1
         #once inidvidual has been iterated through the proper amount
         #append that list to the proper index of population
         population.append(individual)
         tracker+=1
     return population



#randomly generates a 0 or a 1 and returns the value
def coin_toss():
     coin = random.randint(0,1)
     return coin


# #checks if the individual path contains an edge that connects to any of the users input nodes
def node_included(individual):
    score=0

    for i in range(len(individual)):
         if individual[i]==1:
             #if the edge contains 1 of the nodes the user input
             if (nodes[i][0] in user_nodes)or(nodes[i][1] in user_nodes):
                 #if the edge connects 2 of the notes the user input
                 if (nodes[i][0] in user_nodes)and(nodes[i][1] in user_nodes):
                     score+=20000
                 else:
                     score+=10000
    return score






# #checks if the individual path contains a lone edge that does not connect to user input nodes or any other edges
def lone_edge(individual):
     score=0
     edges_list=[]
     for i in range(len(individual)):
         if individual[i]==1:
             #add nodes in edge to edges list for check_edges condition
             edges_list.append(nodes[i][0])
             edges_list.append(nodes[i][1])
     i=0
     while (i < len(individual)):
         if(individual[i]==1):
              check_nodes= False   # 1. check if the edge does not connect 2 of the nodes,
              check_edges= False   # 2. check if the edge does not connect to other edges in this individuals list
              #check if the edge connects at least 1 node
              if (nodes[i][0] in user_nodes)or(nodes[i][1] in user_nodes):
                  check_nodes=True #true- connects to a node
              #count how many times the current node appears in the list. if its more than 1, the node connects at least 2 surrounding edges
              if(edges_list.count(nodes[i][0])>1)or(edges_list.count(nodes[i][0])>1):
                  check_edges=True #true- not a lone edge              #if both conditions are still false this is a lone edge
              if check_edges==False and check_nodes==False:
                  score=-10000
         i+=1

     #NOTE= need to add while loop to see if we can keep connecting edges
     return score

#uses a bubble sort to get top performers
def getTopPerformers():
    population_scores = fitness()
    #bubble sort population_scores and population
    for i in range(len(population_scores)):
        for j in range(0,len(population_scores)-i-1):
            if population_scores[j]>population_scores[j+1]:
                population_scores[j],population_scores[j+1]=population_scores[j+1],population_scores[j]
                population[j],population[j+1]=population[j+1],population[j]

    parentsSize= round(.2* len(population),0) #get the top 30%
    parents=population[:int(parentsSize)] #create next generation parent list only containing top 30% from this generation
    return parents

def getTopParent():
    global node_graph
    # print( node_graph)
    parents= getTopPerformers()
    topParent=parents[0]
    return topParent


#takes 2 parent individuals and generates a new individual
def crossover(ind1,ind2):
    crosspoint= int(round(random.random()*len(ind1),0))#randomly select a crossover point using parent 1's length
    ind1= ind1[:crosspoint]#first half of new individual child
    ind2= ind2[crosspoint:]#second half of new individual child
    child=ind1+ind2
    return child

#takes the top 30% individuals and creates the next geration by cross mixing between 2 individuals
def mutate():
    #call gettopperformers func to get next generation parents
    parents=getTopPerformers()
    #call cross over function until we have 1000 new child individuals for our new population
    nextGen=[]
    while len(nextGen) <=500:
        #NOTE-may want to edit this in favor of higher scoring parents
        nextGen.append(crossover(random.choice(parents),random.choice(parents)))

    return nextGen


def num_of_edges(individual):
    #count the number of 1s (edges)
    #a slolution that connects all nodes would have at least n-1 edges, where n= number of nodes,
    #so we would want a higher score for those that have at least n-1 edges
     if individual.count(1)>=len(user_nodes):
         score=1000
     else:
         score=0
     return score





'''
prompt_user prompts the user for a list of nodes and takes into account any user error.
The user must enter d or D to represeent done to start the graphing.
'''
def prompt_user():
    global user_nodes
    # Prompt user for node input
    user_input = input("Please enter one node and click enter (enter 'd' or 'D' when done): ")
    # If the user put in a letter and the letter is not d or D
    if (user_input.isdigit() == False and user_input != "d" and user_input != "D"):
        # Prompt the user to input a valid number and prompt the user again
        print("Please enter a valid number.")
        return True
    # If the user enters a 'd' or 'D'
    elif (user_input == "d" or user_input == "D"):
        # If the length of the user_nodes is 1
        if (len(user_nodes) == 1):
            # Prompt the user to input at least 2 values and prompt the user again
            print("Please enter at least 2 values.")
            return True
        # Else return the values
        else:
            print("Confirm ending?")
            return False
    # Else, the user entered a value
    else:
        # Turn the user input into an int
        user_input = int(user_input)
        # Find the length of the nodes and divide by 2 to find the node length
        length = (len(nodes)/2)
        # Round down to find the length of the nodes
        length = math.floor(length)
        # If the user_input is greater than the length of the node list options
        if (user_input > length):
            # Prompt the user to enter a value in range and prompt the user again
            print("Please enter a value in range of 0 to ", (length))
            return True
        # If the length of the user_nodes is 0
        elif (len(user_nodes) == 0):
            # Append the input to the user_nodes list and prompt user again
            user_nodes.append(user_input)
            return True
        # If the length of the user_nodes is not 0
        elif (len(user_nodes) != 0):
            # Set counter to 0
            counter = 0
            # Use while loop to iterate through the user_nodes list
            while (counter < len(user_nodes)):
                # If the user_input is the same as an input before
                if user_nodes[counter] == user_input:
                    # Prompt the user to input a different value
                    print("Please input a different value.")
                    # Increment counter and prompt user
                    counter += 1
                    return True
                # Else, the value is not the same
                else:
                    # Increment counter
                    counter += 1
            # Append the user input to the user_nodes
            user_nodes.append(user_input)
            # Sort user_nodes
            user_nodes.sort()
            # Prompt the user for more nodes
            return True


'''
fitness function calculates a score based upon how many adjacent edges the individual 
has of those of the user nodes list 
'''
def neighbor_edges(individual):
    # print(individual)
    #get the adjacent edges to the one in the user node list
    adj_edges = adjacent_edges()
    score = 0
    tracker = 0
    #traverse through the individual checking to see if any of its
    #edges are in individual
    while(tracker < len(individual)):
        tracker_2 = 0
        #index through adj_edges comparing the current index of individual with
        #all edges in adj_edges
        while(tracker_2 < len(adj_edges)):
            #compare the current index of individual against the current index of adj_edges
            if(individual[tracker] == adj_edges[tracker_2]):
                #if yes increment the individuals score
                score += 1000
                tracker_2+= 1
            tracker_2+=1
        tracker += 1
    return score


'''
gets the list of adjacent edges to each node in the user nodes list. 
also checks to make sure no node is inserted more than once 
'''
def adjacent_edges():
    global node_graph
    global user_nodes
    tracker = 0
    adj_edges = []

    #traverse through user nodes to get the adjacent edges
    while(tracker < len(user_nodes)):
        # get the current node
        this_node = user_nodes[tracker]
        # get the index of that nodes
        this_index = user_nodes.index(this_node)
        # now find the nodes adjacent to that node
        # print(this_index)
        # print(this_node)
        # print(node_graph)

        neighbors = node_graph.vs[this_node].neighbors()

        #traverse through the neighbor list checking if any of those edges are already
        #in the adjacent edge list
        tracker_2 = 0
        while(tracker_2 < len(neighbors)):
            tracker_3 = 0
            #index through adjacent edges at each index of neighbors
            while(tracker < len(adj_edges)):
                # check to see if you are at the end of the adj edges
                if (tracker == len(adj_edges) - 1):
                    #check to see if you have made it through the list without the neighbor edge already existing
                    if (neighbors[tracker_2] != adj_edges[tracker_3]):
                        #add the neighbor to the adjacent edges list
                        adj_edges.append(neighbors[tracker_2])
                    else: #move to the next index of the neighbors
                        tracker_2+=1
                #check to see if the current neighbor index is the same as the adj edges index
                elif(neighbors[tracker_2] == adj_edges[tracker_3]):
                    #move to the next index of the neighbor list
                    tracker_2 += 1
                else:
                    tracker_2 += 1
            tracker_2 += 1
        #move to the next index of the users nodes
        tracker+=1
    return adj_edges


#FITNESS: Includes edge that connects to wanted node, higher cost
#Ammount of edges in graph - start small
#If statements in while loop
def fitness():
    tracker = 0
    score = 0
    population_score = []
    while(tracker < len(population)):
        score += num_of_edges(population[tracker])
        score += lone_edge(population[tracker])
        score += node_included(population[tracker])
        score += neighbor_edges(population[tracker])
        population_score.append(score)

        tracker += 1
    return population_score







def main():
    global population
    global node_graph
    global generation_counter
    parse_graph()
    # print(length)
    # global user_nodes
    # user_nodes = input("What nodes?")


    while (prompt_user() != False):
        prompt_user()

    path = []
    create_graph(path)
    population=initial_population()

    # Set counter equal to 0
    counter = 0
    # While loop to create the amount of generations that we want
    while (counter < 10):
        # Mutation the information to create the population
        population = mutate()
        # Create graph to highlight path and send in the list from the getTopParent funciton
        create_graph(getTopParent())
        # Increment counter
        counter += 1
        generation_counter = int(generation_counter)
        # Increment generation_counter
        generation_counter += 1

    # #NOTE=NEED TO UPDATE MUTATION BELOW, JUST TESTING FUNCTIONS
    # # print(nodes)
    # population=initial_population()
    # create_graph(getTopParent())

    # print('TOP PARENT: ',getTopParent())

    # "\n\n 1st MUTATION"
    # population=mutate()

    # print('TOP PARENT: ',getTopParent())
    # create_graph(getTopParent())

    # "\n\n 2nd MUTATION"
    # population=mutate()

    # print('TOP PARENT: ',getTopParent())
    # create_graph(getTopParent())
    # return













if __name__ == '__main__':
    main()