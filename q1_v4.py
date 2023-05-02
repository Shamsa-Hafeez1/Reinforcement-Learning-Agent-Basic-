import turtle 
# import sys
# sys.path.append("c:\\users\\fizza\\appdata\\local\\programs\\python\\python310\\lib\\site-packages\\numpy")
import numpy as np

# import my_module
# from "c:\\users\\fizza\\appdata\\local\\programs\\python\\python310\\lib\\site-packages" import numpy as np
import math 
import random 


class Reinforcement_Learning: 
    def __init__(self): 
       
        self.MAX_STEPS = 20 
        self.alpha = 0.8
        self.T = 1 
        self.gamma = 0.8 # larger gamma, care more about long term reward 

        turtle.register_shape("square", ((-10,-10), (-10,10), (10,10), (10,-10), (-10,-10)))
        turtle.register_shape("left", ((-10,10),(0,0),(10,10),(0,2),(-10,10)))  
        turtle.register_shape("right", ((-10,-10),(0,0),(10,-10),(0,-2),(-10,-10)))
        turtle.register_shape("up", ((0, -10), (-10, 0), (0, 10), (-2, 0), (0, -10)))
        turtle.register_shape("down", ((0, 10), (10, 0), (0, -10), (8, 0), (0, 10)))

        self.t = turtle.Turtle(shape="square")
        
        self.t.speed(5)
        self.t.hideturtle()

        grid_option = input("Do you want a prebuilt grid? y - Yes, n - No: ")
        if grid_option == "y":
            self.grid = [
                "XXXXBXXXXX",
                "XXXXXXXXXB",
                "XXXXRRRRXR",
                "XBXXXXXXXX",
                "XBXXXXXXXX",
                "XBXXXXXXXX",
                "XXRXXXXXXX",
                "XXRRXXRRRX",
                "XXRXXXXXXX",
                "XXRRRRRRRG"
            ]
        #-------------------- You can use different grids to test the code 
        #         self.grid = [
        #     "XXXXXXXXXXXXG",
        #     "XBXXXXXXXXXXR",
        #     "XXXXXXXXXXXXX",
        #     "XXXXXXXXXXXXX",
        #     "XXXXXXXXXXXXX",
        #     "GGGGGRRRRRRRR"
        # ]
            # self.grid = [
            #     "XXXG",
            #     "XBXR",
            #     "XXXX",
            #     "XXXX"]
        else: 
            self.generate_random_grid() 
        

        self.t.penup()
      
        self.grid_vals = dict()
        for y in range(len(self.grid)):
                for x in range(len(self.grid[y])):

                    character=self.grid[y][x]
                    screen_x, screen_y = -288 + (x*24), 88 - (y*24)

                    if character == "X" :
                        self.t.fillcolor("white") 
                        self.grid_vals[(screen_x, screen_y)]  = random.random()

                    if character == "R" :
                        self.t.fillcolor("red")
                        self.grid_vals[(screen_x, screen_y)]  = -100
                        
                    if character == "G" : 
                        self.t.fillcolor("green")
                        self.grid_vals[(screen_x, screen_y)]  = 100 

                    if character == "B": 
                        self.t.fillcolor("black")
                        self.grid_vals[(screen_x, screen_y)]  = None 

                    self.t.goto(screen_x, screen_y)     
                    self.t.stamp()

        # The turtle now sets to get ready for its journey 
        
        self.t.shape("turtle")
        self.t.fillcolor("blue")
        self.start_node = next(iter(self.grid_vals))
        self.t.showturtle()
       

    def generate_random_grid(self): 
        n = int(input("Enter the value from a _ x _ grid: "))
        self.grid = [] 
        for i in range(n): 
            row = "" 
            for j in range(n): 
                if i == 0 and j == 0: 
                    row += "X"
                else:
                    row += random.choices(["X", "G", "R", "B"], weights=[0.85, 0.05, 0.05, 0.05])[0]
            self.grid.append(row)


    def Boltzmann_distribution(self, values, energies): 
        probabilities = [math.exp(energies[i]/self.T) for i in range(len(energies))]
        return values[np.random.choice(len(values), p = [i/sum(probabilities) for i in probabilities])]
        
    def show_directions(self): 
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if self.grid[y][x] != "G" and self.grid[y][x] != "B" and self.grid[y][x] != "R": 
                    neighbours = [ (-288 + ((x+1)*24), 88 - ((y)*24)), (-288 + ((x-1)*24), 88 - ((y)*24)), (-288 + ((x)*24), 88 - ((y-1)*24)), (-288 + ((x)*24), 88 - ((y+1)*24))]
                    d = [self.grid_vals[i] if i in self.grid_vals and self.grid_vals[i] != None else -10000 for i in neighbours]
    
                    v = d.index(max(d))
                    self.t.goto((-288 + (x*24), 88 - (y*24)))
                    if v == 0: 
                        self.t.shape("right")
                    if v == 1: 
                        self.t.shape("left")
                    if v == 2: 
                        self.t.shape("up")
                    if v == 3: 
                        self.t.shape("down")
                    
                    self.t.stamp()
    

    def episode(self): 

        end, current_node, steps_taken = False, self.start_node, 0 

        self.t.goto(self.start_node)
        self.t.shape("turtle")
        self.t.fillcolor("blue")

        visited = [current_node] 

        while  steps_taken != self.MAX_STEPS and not end: 
            self.t.showturtle() 
            steps_taken += 1 

            x, y = (current_node[0] + 288) // 24 , - (current_node[1] - 88) // 24 

            neighbours = [ (-288 + ((x+1)*24), 88 - ((y)*24)), (-288 + ((x-1)*24), 88 - ((y)*24)), (-288 + ((x)*24), 88 - ((y-1)*24)), (-288 + ((x)*24), 88 - ((y+1)*24))]
           
            values, energy = [], []
            for n in neighbours:
                if n in self.grid_vals and n not in visited and self.grid_vals[n] != None: 
                    values.append(n) 
                    energy.append(self.grid_vals[n])
          
            if len(energy) == 0: 
                break 
            
            next_node =  self.Boltzmann_distribution(values, energy)
            
            self.t.goto(next_node)

            # Was there any reward in next node? 
            xx, yy = (next_node[0] + 288) // 24, - (next_node[1] - 88) // 24 

            if self.grid[yy][xx] == "G": 
                reward, end = 100, True 
                self.t.hideturtle() 
                self.grid_vals[current_node] = self.grid_vals[current_node] + self.alpha * (reward + (self.gamma * self.grid_vals[next_node]) - self.grid_vals[current_node]) - steps_taken

            elif self.grid[yy][xx] == "R":
                reward, end = -100, True 
                self.t.hideturtle() 
                self.grid_vals[current_node] = self.grid_vals[current_node] + self.alpha * (reward + (self.gamma * self.grid_vals[next_node]) - self.grid_vals[current_node]) 
            
            else: 
                reward = 0  
                self.grid_vals[current_node] = self.grid_vals[current_node] + self.alpha * (reward + (self.gamma * self.grid_vals[next_node]) - self.grid_vals[current_node]) 
                self.t.shape("square")
                self.t.fillcolor('white')
                # self.t.fillcolor(1-(self.grid_vals[current_node] +100) / 200.0, (self.grid_vals[current_node] +100) / 200.0, 0)
                self.t.stamp()
                self.t.write(str(round(self.grid_vals[current_node], 2)),align="center", font=("Arial", 5, "normal")) 

              
            visited.append(next_node)
            current_node = next_node
            if self.T > 0.2:
                self.T -= 0.001

rl = Reinforcement_Learning() 
for i in range(50):
    rl.episode()
rl.show_directions()

turtle.update()
turtle.mainloop()
                        