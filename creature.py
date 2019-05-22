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

            self.health = ((health_temp_1 + health_temp_2) * health_temp_3 + health_temp_4)

            strength_1 = self.size * 2

            if self.eating == 5 or self.eating == 6:
                strength_2 = 5

            elif self.eating == 3 or self.eating == 4:
                strength_2 = 2

            else:
                strength_2 = 1

            if self.hunting == 3:
                strength_3 = 2
            elif self.hunting == 5:
                strength_3 = 3
            else:
                strength_3 = 1


            self.strength = (strength_1 + strength_2 * strength_3)
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

def compete(species_lst):
    global winner
    #time of day of the conflict,  during the night creatures with ultrasoud (no eyes) have a 3x bonus but are reduced by 10% during the day
    time = random.uniform(1,24)
    #randomly picks the first species invovled in the conflict
    pick_1 = random.choice(species_lst)

    #randomly picks the second species invovled in the conflict
    pick_2 = random.choice(species_lst)
    #if pick_1 is equal to pick_2 then pick another

    while pick_2 == pick_1:
        pick_2 = random.choice(species_lst)
    else:
        pass

    #determine ultrasound multiplier
    if time <= 3:
        print("ultrasound gets a 7x strength advantage!!!")
        ultrasound_bonus = 6
    elif time >= 22:
        print("ultrasound gets a 7x strength advantage!!!")
        ultrasound_bonus = 6
    else:
        print("ultrasoud gets a 10% penalty!")
        ultrasound_bonus = 0.9

    #checks if a sepcies uses ultrasound then applies the bonus strength multiplier
    if pick_1.eye_count == 0:
        pick_1.strength *= ultrasound_bonus
        if pick_2.strength == 0:
            pick_2.strength *= ultrasound_bonus
        else:
            pass
    elif pick_2.eye_count == 0:
        pick_2.strength *= ultrasound_bonus
    else:
        pass

    first_hit = random.choice([1,2])

    if first_hit == 1:
        first = pick_1
        second = pick_2
    elif first_hit == 2:
        first = pick_2
        second = pick_1

    else:
        print('something broke, check the declaration of the variable "first_it"')


    #stores the strength and
    s1 = first.strength
    s2 = second.strength
    h1 = first.health
    h2 = second.health

    #310% bonus if first and uses stalking as hunting method
    if first.hunting == 1:
        s1 *= 3.1
    #325% if first and uses waiting
    elif first.hunting == 4:
        s1 *= 3.25
    #90% chance of getting a 300% bonus, 10% chance of getting a 700% bonus
    elif first.hunting == 6:
        rand_multi = random.uniform(1,0)     #let me sleep please ***********
        if rand_multi > 0.1:
            s1 *= 3
        else:
            s1 *= 7

    #both creatures are assigned a living value
    live1 = True
    live2 = True

    while live1 == True and live2 == True:
        #first attacks first
        h2 -= s1                                      #like actually pls its like 1 in the morning

        #checks if creature survived the attack
        if h2 <= 0:
            live2 = False
        else:
            winner = first
            second.population -= 1

        #creature 2 has survived and retaliates
        h1 -= s2
        if h1 <= 0:
            live2 = False
        else:
            winner = second
            first.population -= 1


    print("winner of this conflict is {0}".format(winner.name))

def mutate(biosphere):
    #creates random number between 1 and 100 and if that number is == to 69 or 70 then mutate the chosen species
    does_evolve = random.randint(1,100)
    if does_evolve == 69 or does_evolve == 70:
        #ranomly chooses a species from the biosphere to be mutated
        chosen_boi = random.choice(biosphere)
        #randomly generates possitive or negative multipliers to multiply to the strength and health values
        rand_strength_multi = random.uniform(0.5,6)
        rand_health_multi = random.uniform(0.5,6)

        #multiplys the two values we created earlier to the strength and health values
        chosen_boi.strength *= rand_strength_multi
        chosen_boi.health *= rand_health_multi
    else:
        pass



def main():
    bob = species("bob",3,4,5,2,4,8,1,2,4,5,6,2,3,4,1,6)
    yeetus = species("ya boi chips ahoy",3,6,2,10,3,4,4,0,4,6,5,6,5,4,4,2)
    carmen = species("carmen ;)" ,5,6,0,0,2,1,3,0,1,2,3,6,2,6,5,1)
    x = [bob,yeetus,carmen]

    compete(x)

    print(x[1].strength)
    print(x[2].strength)
    print(x[1].health)
    print(x[2].health)
#runs the main loop
if __name__ == '__main__':
	main()
