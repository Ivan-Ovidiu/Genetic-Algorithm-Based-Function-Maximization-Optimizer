from chromosome import Chromosome
from Tools import *

"""  start_domain = input("Start of the domain: ")
    end_domain = input("End of the domain: ")
    a = input("a: ")
    b = input("b: ")
    c = input("c: ")
    precision = input("Precision: ")
    crossover_probability = input("Crossover probability: ")
    mutation_probability = input("Mutation probability: ")
    stages_number = input("Number of stages: ")
"""
def functionMax(population_size, start_domain, end_domain, a,  b,  c,  precision, crossover_probability, mutation_probability, stages_number):


    output = open('functionMax_output', 'w')
    file(output)

    population = create_population(population_size, start_domain, end_domain, a, b, c, precision) #populez vectorul cu cromozomi

    print_population(population) #afisez populatia initiala


    for stage in range(stages_number):
         fitness_sum = 0
         for chromosome in population:
            fitness_sum += chromosome.fitness

         max_fitness = max([chromosome.fitness for chromosome in population])



         partial_sum = []
         partial_sum.append(0)
         partial_value = 0.0

         for j in range(1, population_size + 1):
             partial_value += population[j - 1].fitness
             partial_sum.append(partial_value / fitness_sum)

         partial_sum.append(1)

         if stage == 0 :
                print("Probabilitati selectie: " ,file = output)
         for j in range(1, population_size + 1):
                    probability = partial_sum[j] - partial_sum[j - 1]
                    if stage == 0:
                      print(f"Cromozom     {j} probabilitate {probability}", file = output)
         if stage == 0:
             print("Intervale probabilitati selectie: ", file=output)
         for j in range(population_size + 1):
             if stage == 0:
                 print(partial_sum[j], end=" ", file=output)
             if j % 3 == 0 and stage == 0:
                print(file=output)

         if stage == 0:
             print(file=output)

         next_population = []
         for j in range(population_size):           #aici ma folosesc de cautarea binara pentru
             rand_num = randomFloat(0,1)            #a gasi cel mai apropiata valoarea de un numar random din vectorul de suma partiale pentru fitness
             left = 0
             right = population_size - 1
             while left < right:
                 mid = left + (right - left) // 2
                 if rand_num <= partial_sum[mid]:
                     right = mid
                 else:
                     left = mid + 1
             if stage == 0:
                 print(f"u= {rand_num} selectam cromozomul {left}", file = output)
             next_population.append(population[left-1])

         if stage == 0:
             print("Dupa selectie: ", file = output)
             print_population(next_population)


         crossover_population = {}
         if stage == 0:
             print(f"Probabilitatea de incrucisare: {crossover_probability}", file = output)
         for i in range(population_size):
            rand_num = randomFloat(0,1)
            if stage == 0:
                print(f"{i}: {next_population[i].binary} u= {rand_num}",end = " ", file = output)

            if rand_num <= crossover_probability:
                if stage == 0:
                    print(f"< {crossover_probability} participa",file = output)
                crossover_population.update({i: next_population[i]})
            else:
                if stage == 0:
                    print(file = output)

         if len(crossover_population) % 2 !=0: #daca numarul de cromozomi selectati e impar il socatem pe ultimul
            crossover_population.popitem()

         after_crossover_population = next_population
         chromosomes = list(crossover_population.items())
         for i in range(0, len(chromosomes), 2):
             if i + 1 < len(chromosomes):
                 (key1, value1), (key2, value2) = chromosomes[i], chromosomes[i + 1]
                 chromosome1 = value1
                 chromosome2 = value2

                 if stage == 0:
                     print("Recombinare dintre cromozomul " + str(key1) + " si cromozomul " + str(key2) + ":", file = output)

                 chromosome1.binary, chromosome2.binary, point = crossover(chromosome1.binary, chromosome2.binary,stage)
                 chromosome1.real_value = bits_to_float(chromosome1.binary)
                 chromosome2.real_value = bits_to_float(chromosome2.binary)
                 chromosome1.fitness = calculate_fitness( a, b, c,chromosome1.real_value)
                 chromosome2.fitness = calculate_fitness( a, b, c,chromosome1.real_value)
                 after_crossover_population[key1] = chromosome1
                 after_crossover_population[key2] = chromosome2

                 if stage == 0:
                     print(f"{chromosome1.binary} {chromosome2.binary} punct {point}", file=output)
                     print(f"Rezultat {chromosome1.binary} {chromosome2.binary}", file = output)




         if stage == 0 :
                print("Dupa recombinare: ", file = output)
                print_population(after_crossover_population)
                print( file = output)
                print(f"Probabilitate de mutatie pentru fiecare gena {mutation_probability/100} \n Au fost modificati cromozomii:", file = output)

         next_population = mutate_chromosomes(next_population, mutation_probability, a, b, c, stage,start_domain,end_domain)
         if stage == 0:
             print("Dupa mutatie: ", file = output)
             print_population(next_population)
             print(file = output)

         maximum_fitness = max([chromosome.fitness for chromosome in next_population])
         average_fitness = sum([chromosome.fitness for chromosome in next_population]) / len(next_population)

         print("Evolutia maximului: ", file = output)
         print(f"Fitness-ul maxim: {maximum_fitness}", file = output)
         print(f"Medie fitness:  {average_fitness}", file = output)

    return average_fitness,maximum_fitness

functionMax(20, -1, 2.3, -1, 1, 2, 6, 0.25, 1, 50)

