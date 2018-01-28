import random
import turtle

lifespan    = 100               #This is how long each rocket will live
popSize     = 10                #This is how many rockets is there
speed       = 10                #This will be how fast the rocket will be, it can move in a 20 pix radius
screen      = turtle.Screen()   #Higher lifespan, speed, or popSize will make them slower,
turtle.tracer(0,0)              #This makes it so turtles will move at its fastest

def Update ():
    for i in range(lifespan):
        #For every tick in lifespan, a rocket will update its properties.
        for a in population:
            #This will iterate through each rocket instance
            #Updating vectors, its fitness, and its position.
            a.RandomVectors()
            a.UpdatePosition(i)
            a.UpdateFitness()
            #print(a.fitness)
    for a in population:
        a.turt.hideturtle()
        #After the turtle has done lived its lifespan, they will hide.
    
    chancePool = []
    #chancePool is a list of copies of rockets, higher fitness will put more of one copies in there
    for a in population:
        chance = round(a.fitness * 10000)
        copy = a
        for b in range(chance):
            chancePool.append(copy)

    #fakePop will make sure it wont effect the children
    fakePop = []
    for b in range(popSize):
        #This will make a child, randomly choosing from the chance pool.
        parA = chancePool[random.randint(0, len(chancePool))]
        parB = chancePool[random.randint(0, len(chancePool))]
        child = Rocket()
        child.RandomVectors()
        #This is so that the vector can be overridden.
        for c in range(lifespan):
            #This is the how vectors will be transferred
            #It will randomly select one of the parents and give it to the child.
            #there is also a 1 in a 101 chance of it being a random vector
            z = random.randint(0,101)
            if z <= 50:
                child.SetVector(parA.vectorList[c], c)
            elif z < 100 and z > 50:
                child.SetVector(parB.vectorList[c], c)
            elif z == 101:
                child.SetVector((random.randint(-speed, speed),(random.randint(-speed, speed))), c)
        
        fakePop.append(child)
    for i in range(popSize):
        population[i] = fakePop[i]
        
    Update()

class Rocket():
    #Every rocket will have properties of a turtle, vector, position, fitness, and vectorList
    #A vector is just a coord that the rocket will go to, in a radius of speed.
    #vectorList will act as the genes, every tick of lifespan, there will be a vector
    #Fitness will be how well the rocket is doing, measured by how far it is from the circle
    def __init__(self):
        self            = self
        self.vectorList = []
        self.position   = [0,0]
        self.turt       = turtle.Turtle()
        self.fitness    = 0
        self.won        = False
        self.turt.penup()
        self.turt.setpos(0, 0)
        self.turt.shape("turtle")
        self.turt.speed("fastest")
        #self.turt.pendown()
        
    def RandomVectors(self):
        #This will make a random vector for every tick in lifespan
        for i in range(lifespan):
            self.vectorList.append((random.randint(-speed,speed), random.randint(-speed,speed)))
    
    def SetVector(self, vector, vectorIndex):
        #If given a vector and its index, this will replace it.
        self.vectorList[vectorIndex] = vector
    
    def UpdatePosition(self, vectIndex):
        #Each vector will add on to the rockets position
        self.position[0]  = self.position[0] + self.vectorList[vectIndex][0]
        self.position[1]  = self.position[1] + self.vectorList[vectIndex][1]
        self.turt.setpos(self.position[0], self.position[1])
        turtle.update()
    
    def UpdateFitness(self):
        d = self.turt.distance(0, 200)
        #If the turtle is in a 20 pixel radius, it will be given a high fitness rating
        if (self.turt.pos()[0] >= 20 and self.turt.pos()[1] <= 20) and (self.turt.pos()[0] >= 180 and self.turt.pos()[1] <= 220):
            self.fitness = 3
            self.won = True
    
        if self.won == False:
            #This is how it calculates fitness
            self.fitness = 1/d+0.1
    
        
circ = turtle.Turtle()
circ.penup()
circ.setpos(0, 200)
circ.pendown()
circ.circle(10)
circ.hideturtle()

#This will create a new population starting the program
population = [Rocket() for i in range(popSize)]
Update()
input()