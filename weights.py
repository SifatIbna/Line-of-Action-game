def weigths():
    
    weigths8 = list()
    weights6 = list()
    
    
    file_weight8 = open("weights8x8.txt", "r")
    file_weight6 = open("weights6.txt","r")
    
    lines8 = file_weight8.readlines()
    lines6 = file_weight6.readlines()
    
    for line in lines8:

        line = line.split()
        weigths8.append( [int(line[i]) for i in range(len(line))] )
        
    
    for line in lines6:

        line = line.split()
        weights6.append( [int(line[i]) for i in range(len(line))] )
        
    
    print(weights6)
    print(weigths8)
    
    return weigths8,weights6

weigths()