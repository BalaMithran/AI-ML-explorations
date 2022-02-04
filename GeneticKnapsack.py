from random import randint
import random
# val = [2,4,7,4]
# wei = [4,1,6,3]
# capacity = 10

val = [2,4,7,4,1,4,3,7,6,12,4,7,4,1,4,3,7,6,1,7,4,1,4,3,7,6,1,4,7,4,1,4,3]
wei = [4,1,6,3,6,1,3,4,2,10,1,6,3,6,1,3,4,2,1,1,6,3,6,1,3,4,2,10,1,6,3,6,1]
capacity =70

respresentation = [0]*len(val)

def create_solns(population , gene_size):
    total_population = []
    
    for i in range(population):
        temp = []
        for i in range(gene_size):
            k = random.randint(0, 1)
            temp.append(int(k))
        total_population.append(temp)
    return total_population
# print(create_solns(10,len(val)))

def fitness(inp):
    bag_wei = 0
    for index,i in enumerate(inp):
        if i==1:
            bag_wei +=wei[index]
        if bag_wei>capacity:
            return 0
    return bag_wei/capacity
# print(fitness([1,0,1,1]))

def selection_of_parents(no_of_parents , current_total_population):
    final_score_dict = {}
    for index , individual in enumerate(current_total_population):
        score = fitness(individual)
        final_score_dict[index] = score
    d = sorted(final_score_dict.items(), key=lambda x: x[1], reverse=True)
    parents = []
    for i in range(no_of_parents):
        parents.append(current_total_population[d[i][0]])
    return parents

def crossover(parents , population_size):
    new_population = []
    new_population.extend(parents)
    splices1 = []
    splices2 = []
    splice_length = len(parents[0])//2
    # print("splice_length" , splice_length)
    for parent in parents:
        splices1.append(parent[:splice_length])
        splices2.append(parent[splice_length:])
    for i in range(population_size-len(parents)):
        pair1 = random.choice(splices1)
        # print(pair1 , end='        ')
        pair2  = random.choice(splices2)
        # print(pair2 , end="      ")
        final = pair1 + pair2
        # new.extend(random.choice(splices2))
        # print(final)
        new_population.append(final)
        new = []
    return new_population
    # return (splices1,splices2)

def mutation(population):
    mutation_percent = 1
    for i in range(mutation_percent):
        individual_loc = random.randint(0, len(population)-1)
        individual = population[individual_loc]
        # print("individual     " ,individual)
        # individual = random.choices(population)
        mutation_loc = random.randint(0, len(individual)-1)
        codon = individual[mutation_loc]
        if codon == 1:
            individual[mutation_loc] = 0
        else:
            individual[mutation_loc] = 1
        population[individual_loc] = individual
        # print("individual after mutation     " ,individual)

    return population


def average_fitness(population):
    count = len(population)
    score = 0
    for individual in population:
        score+=fitness(individual)
    return (score/count)      
def selection(no_of_generations , population_size , parents_count):
    total_pop = create_solns(population_size,len(val))
    # selected_parents = selection_of_parents(parents_count,total_pop)
    # new_population  = crossover(selected_parents , population_size)
    # new_population_with_mutation = mutation(new_population)
    for generation in range(no_of_generations):
        print("Round " , generation)
        selected_parents = selection_of_parents(parents_count,total_pop)
        new_population  = crossover(selected_parents , population_size)
        new_population_with_mutation = mutation(new_population)
        total_pop = new_population_with_mutation
        # total_pop = new_population
        print("average_fitness " , average_fitness(total_pop))
    print(total_pop)

selection(10 , 7 , 2)

# population_size = 10
# total_pop = create_solns(population_size,len(val))
# print(total_pop)
# parents = selection_of_parents(4,total_pop)
# print("parents /n")
# print(parents)
# print("new population")
# new_population  = crossover(parents , population_size)
# print(new_population)
# print("mutated")
# print(mutation(new_population))
