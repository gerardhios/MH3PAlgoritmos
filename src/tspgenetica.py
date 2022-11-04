import numpy as np

def distances():
    return np.matrix([
        [0,     20.4,  22.2, 29.3,  17.4],
        [20.4,  0,     29.7, 21.8,  16.7],
        [22.2,  29.7,  0,    19.3,  12.6],
        [29.3,  21.8,  19.3, 0,     11.9],
        [17.4,  16.7,  12.6, 11.9,  0],
    ])
    
def fit(chromosome):
    d = distances()
    ret = 0
    print(d)
    for i in range(len(chromosome) - 2):
        ret += d[chromosome[i], chromosome[i+1]]
    return ret

def generate_chromosome():
    chromosome = np.random.permutation(6)
    fitness = fit(chromosome)
    chromosome = np.append(chromosome, fitness)
    return chromosome

def generate_first_population(size:int):
    population = np.empty((size, 7))
    cont = 0
    while(True):
        chromosome = generate_chromosome()
        if not chromosome in population:
            population[cont] = chromosome
            cont += 1
        if cont == size:
            break
    return population

def roulette_selection(population):
    mx = np.max(population)
    print(mx)
    
    
pop = generate_first_population(10)
roulette_selection(pop)