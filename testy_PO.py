from random import randint

def rand_input(no_moves) :
    directions = ['f','b','r','l']
    table = []
    output = "{\""
    for i in range(no_moves) :
        index = randint(0,4)
        if index < 4 :
            output += directions[index]
            table.append(directions[index])
        else :
            ch = chr(randint(97,122))   
            output += ch
            if ch in directions :
                table.append(ch)
        output += "\", \""


    index = randint(0,4)
    if index < 4 : 
        output += directions[index]
        table.append(directions[index])
    else : 
        ch = chr(randint(97,122))
        output += ch
        if ch in directions :
            table.append(ch)
    output += "\"}"
    return output,table
    


def randomTest(test_ind = "first", no_animals = 2, no_moves = 10, map_width = 5, map_height = 5) :
    output = "  @Test\n"
    output += "  public void " + test_ind + "Test() {\n"
    args = rand_input(no_moves)
    output += "        String[] input = " + args[0] + ";\n"
    output += "        List<MoveDirection> directions = OptionsParser.parse(input);\n"
    output += "        List<Vector2d> positions = List.of("
    positions = []
    for _ in range(no_animals - 1) :
        y = randint(0,map_width-1)
        x = randint(0,map_height-1)
        while (x,y) in positions :
            y = randint(0,map_width-1)
            x = randint(0,map_height-1)
        positions.append((x,y))
        output += "new Vector2d(" + str(x) + "," + str(y) + "), "
    y = randint(0,map_width-1)
    x = randint(0,map_height-1)
    while (x,y) in positions :
        y = randint(0,map_width-1)
        x = randint(0,map_height-1)
    positions.append([x,y])
    output += "new Vector2d(" + str(x) + "," + str(y) + "));\n"
    output += "        Simulation simulation = new Simulation(directions, positions,new RectangularMap(" + str(map_width) + "," + str(map_height) + "));\n"
    output += "        List<String> result = simulation.run();\n"
    
    
    animals = []
    for i in range(len(positions)) :
        animals.append([positions[i],'^'])
    
    moves = args[1]
    moves_history = []
    
    def occupied(location) :
        for animal in animals :
            if animal[0] == location :
                return True
        return False
    
    def inMap(location) :
        if ((location[0] < map_width) and (location[0] >= 0) and (location[1] < map_height) and (location[1] >= 0)) :
            return True
        return False
    
    def next(orientation) :
        if orientation == '^' : return '>'
        if orientation == '>' : return 'v'
        if orientation == 'v' : return '<'
        if orientation == '<' : return '^'
        
    def previous(orientation) :
        if orientation == '^' : return '<'
        if orientation == '<' : return 'v'
        if orientation == 'v' : return '>'
        if orientation == '>' : return '^'
    
    for i in range(len(moves)) :
        animal_ind = i%no_animals
        move = moves[i]
        o = animals[animal_ind][1]
        a = animals[animal_ind][0][0]
        b = animals[animal_ind][0][1]
        location = animals[animal_ind][0]
        orientation = animals[animal_ind][1]
        if move =='f' :
            if orientation == "^" :
                new_location = [animals[animal_ind][0][0],animals[animal_ind][0][1] + 1]
                if inMap(new_location) and not occupied(new_location) :
                    animals[animal_ind][0] = new_location
                    o,a,b = orientation,new_location[0],new_location[1]
            if orientation == ">" :
                new_location = [animals[animal_ind][0][0] + 1,animals[animal_ind][0][1]]
                if inMap(new_location) and not occupied(new_location) :
                    animals[animal_ind][0] = new_location
                    o,a,b = orientation,new_location[0],new_location[1]
            if orientation == "v" :
                new_location = [animals[animal_ind][0][0],animals[animal_ind][0][1] - 1]
                if inMap(new_location) and not occupied(new_location) :
                    animals[animal_ind][0] = new_location
                    o,a,b = orientation,new_location[0],new_location[1]
            if orientation == "<" :
                new_location = [animals[animal_ind][0][0] - 1,animals[animal_ind][0][1]]
                if inMap(new_location) and not occupied(new_location) :
                    animals[animal_ind][0] = new_location
                    o,a,b = orientation,new_location[0],new_location[1]
        if move =='b' :
            if orientation == "^" :
                new_location = [animals[animal_ind][0][0],animals[animal_ind][0][1] - 1]
                if inMap(new_location) and not occupied(new_location) :
                    animals[animal_ind][0] = new_location
                    o,a,b = orientation,new_location[0],new_location[1]
            if orientation == ">" :
                new_location = [animals[animal_ind][0][0] - 1,animals[animal_ind][0][1]]
                if inMap(new_location) and not occupied(new_location) :
                    animals[animal_ind][0] = new_location
                    o,a,b = orientation,new_location[0],new_location[1]
            if orientation == "v" :
                new_location = [animals[animal_ind][0][0],animals[animal_ind][0][1] + 1]
                if inMap(new_location) and not occupied(new_location) :
                    animals[animal_ind][0] = new_location
                    o,a,b = orientation,new_location[0],new_location[1]
            if orientation == "<" :
                new_location = [animals[animal_ind][0][0] + 1,animals[animal_ind][0][1]]
                if inMap(new_location) and not occupied(new_location) :
                    animals[animal_ind][0] = new_location
                    o,a,b = orientation,new_location[0],new_location[1]
        if move == 'r' :
            animals[animal_ind][1] = next(orientation)
            o,a,b = next(orientation),location[0],location[1]
        if move == 'l' :
            animals[animal_ind][1] = previous(orientation)
            o,a,b = previous(orientation),location[0],location[1]
        moves_history.append(str(o) + " (" + str(a) + "," + str(b) + ")")
    
    expected_result = ''
    for i in range(len(moves_history) - 1) :
        expected_result +=  '\"' + moves_history[i] + "\", "
    expected_result += '\"' + moves_history[-1] + "\""
    output += "        List<String> expectedResult = List.of(" + expected_result + ");\n"
    output += "        if (result.size() != expectedResult.size()) {\n"
    output += "            assertTrue(false);\n"
    output += "            return;\n"
    output += "        }\n"
    output += "        for (int i = 0; i < result.size(); i++) {\n"
    output += "            assertEquals(result.get(i),expectedResult.get(i));\n"
    output += "        }\n"
    output += "    }\n"
    
    return output
    
print(randomTest("first",2,10,7,6))
