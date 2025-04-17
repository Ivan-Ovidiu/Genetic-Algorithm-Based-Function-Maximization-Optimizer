import random
import struct
from chromosome import Chromosome


def file(file):      #pentru a putea face fisierul de output vizibil in tot proiectul
    global output
    output = file
def randomFloat(a, b):
    return random.uniform(a, b)
def randomInt(a, b):
    return random.randint(a, b)
def float_to_bits(num):
    return ''.join(format(byte, '08b') for byte in struct.pack('>f', num))

def bits_to_float(bits):

    if len(bits) < 32:
        bits = bits.zfill(32)
    elif len(bits) > 32:
        bits = bits[-32:]

    bytes_data = bytearray()
    for i in range(0, 32, 8):
        byte = bits[i:i + 8]
        bytes_data.append(int(byte, 2))


    return struct.unpack('>f', bytes_data)[0]


def mutation(cromozom, domain_start, domain_end):
    while True:
        cromozom = list(cromozom)
        mutation_mask = [str(randomInt(0, 1)) for x in range(len(cromozom))]
        for i in range(len(cromozom)):
            if mutation_mask[i] == "1":
                if cromozom[i] == "1":
                    cromozom[i] = "0"
                else:
                    cromozom[i] = "1"

        cromozom = "".join(cromozom)

        if domain_start <= bits_to_float(cromozom) <= domain_end:
            break

    return cromozom


def crossover(cromozom1, cromozom2, stage):
    cromozom1 = list(cromozom1)
    cromozom2 = list(cromozom2)

    crossover_index = randomInt(0, len(cromozom1) - 1)
    for i in range(crossover_index):
        cromozom1[i], cromozom2[i] = cromozom2[i], cromozom1[i]

    cromozom1 = "".join(cromozom1)
    cromozom2 = "".join(cromozom2)

    return cromozom1,cromozom2, crossover_index

def calculate_fitness(a,b,c,x):
    return a * x * x + b * x + c
def create_chromosome(domain_start,domain_end,a,b,c,precision):
    float_value = round(randomFloat(domain_start,domain_end),precision)
    fitness_value =  calculate_fitness(a,b,c,float_value)
    return Chromosome(float_to_bits(float_value),float_value,fitness_value)


def create_population(population_size,domain_start,domain_end,a,b,c,precision):
    population = []
    for i in range(population_size):
        population.append(create_chromosome(domain_start,domain_end,a,b,c,precision))
    return population

def mutate_chromosomes(population,mutation_probability,a,b,c,stage,start_domain,end_domain):
    for i in range(len(population)):
        rand_num = randomInt(0,100)
        if rand_num <= mutation_probability:
            if stage == 0:
                print(f"{i}", file = output)
            population[i].binary = mutation(population[i].binary,start_domain,end_domain)
            population[i].real_value = bits_to_float(population[i].binary)
            population[i].fitness = calculate_fitness(a,b,c,population[i].real_value)
    return population
def print_population(population):
    for i in range(len(population)):
        print(f"{i+1}: {population[i].binary} x= {population[i].real_value} f= {population[i].fitness}",file = output)

def output_chromosome(chromosome,index):
    print(f"{index}:  {chromosome.binary} x= {chromosome.real_value} f= {chromosome.fitness}",file =output)

