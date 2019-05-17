import random

#creates an object class known as species
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
            self.health = random.randint(1,100)
            self.strength = random.randint(50,100)
            #rate of offspring production
            #####***********************change this to be involved with wether or not a species reproduces via eggs or live birth
            self.rate = random.randint(10000,1000000)
            #population size of a species
            self.population = random.randint(100,1000)
'''
    def reproduce(self):
        parent_percentage = random.randint(1,10)
        parent_percentage = 1/parent_percentage

        self.population = self.population + (population.rate * parent_percentage)
        self.population = round(self.population)
'''

def reproduce(species):
    #random percentage from 10% - 60% of the population that will reproduce
    parent_percentage = (random.randint(1,6))/10
    #useless variable assignmnet
    population = species.population
    num_offspring = population * parent_percentage
    #if the species' 'babies' column has a even number than 3x the offspring, if not then * 0.9
    if species.babies % 2 == 0:
        num_offspring *= 3
    else:
        num_offspring *= 0.9

    species.population += num_offspring

    species.population = round(species.population)

#this is our natural disaster / mass extinction event calculator
def bad_boi():
    #a hurricane and a mass extinction event CANNOT happen in the same generation
    #category 1 events are things like hurricanes or typhoons; very common but does do that much damage;  reduces each species' population by 3%
    cat_1_true = None
    #1 in 3 chance of a hurricane
    cat_1 = random.randint(0,2)
    if random.randint == 1:
        cat_1_true = True
        return 1
    else:
        cat_1_true = False

        cat_2_true = None
        #1 in 1000000 chance of a mass extinction ONLY IF there is not a hurricane
        cat_2 = random.randint(1,1000000)
        if cat_2 == 999:
            cat_2_true = True
            print('a mass extinction event has occured!! Each species population decreased by 99.9%')
            return 2
        else:
            cat_2_true = False
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
