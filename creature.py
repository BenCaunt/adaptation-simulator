import random

#creates an object class known as species

#skeleton 1 = exo, 2 = endo, 3 =none
class species:
    def __init__(self, name, skin, body_shape, segments, appendages, skeleton, size, movement, eye_count, eating, hunting, defense, reproduction, mating, babies, care, enviornment):

            self.name = name
            self.skin = skin
            self.body_shape = body_shape
            self.segments = segments
            self.appendages = appendages
            self.skeleton = skeleton
            self.size = size
            self.movement = movement
            self.eye_count = eye_count
            self.eating = eating
            self.hunting = hunting
            self.defense = defense
            self.reproduction = reproduction
            self.mating = mating
            self.babies = babies
            self.care = care
            self.enviornment = enviornment
            #********change to calculate from the information about skin, skelton, and defense
            #calculates a health mutliplier if the skin has scales
            if self.skin == 1 or self.skin == 2:
                health_temp_1 = 10
            else:
                health_temp_1 = 5

            health_temp_2 = self.size

            health_temp_3 = self.skeleton * 2 

            health_temp_4 = self.defense

            self.health = ((health_temp_1 + health_temp_2) * health_temp_3 + health_temp_4) * 10

            self.strength = random.randint(50,100)
            #rate of offspring production
            #####***********************change this to be involved with wether or not a species reproduces via eggs or live birth
            self.population = random.randint(100,1000)
'''
    def reproduce(self):
        parent_percentage = random.randint(1,10)
        parent_percentage = 1/parent_percentage

        self.population = self.population + (population.rate * parent_percentage)
        self.population = round(self.population)
'''

#our reproduce function that takes in the specific species as an objects
def reproduce(species):
    #random percentage from 10% - 60% of the population that will reproduce
    num_parent = (random.randint(10,60))
    #useless variable assignmnet
    population = species.population
    #two parents to make one child
    num_offspring = num_parent/2
    #if the species' 'babies' column has a even number than 3x the offspring, if not then * 0.9
    if species.babies % 2 == 0:
        num_offspring *= random.randint(3,6)
    else:
        num_offspring *= 0.9

    species.population += num_offspring

    species.population = round(species.population)

#this is our natural disaster / mass extinction event calculator

#a and b are both values decided outside the loop,  a is recommended to have a random int from 0,2, b is recommended to have a random int from 0,100000
def bad_boi(a, b):
    #a hurricane and a mass extinction event CANNOT happen in the same generation
    #category 1 events are things like hurricanes or typhoons; very common but does do that much damage;  reduces each species' population by 10%
    #1 in 3 chance of a hurricane
    if a == 1:
        return 1
    else:
        #1 in 1000000 chance of a mass extinction ONLY IF there is not a hurricane
        if b == 999:
            print('a mass extinction event has occured!! Each species population decreased by 99.9%')
            return 2
        else:
            return 0

def compete(species_x, species_y):
    pass

def main():
    #creates an orgranism known as bob
	bob = organism("bob",3,4,5,2,4,8,1,2,4,5,6,2,3,4,1,6)
    #prints bobs health
	print(bob.health)

#runs the main loop
if __name__ == '__main__':
	main()
