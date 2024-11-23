import random


def crossover(parent1, parent2):
    # Cruce de dos padres para producir un descendiente
    n = len(parent1)
    crossover_point = random.randint(1, n - 1)
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child


#best_solution = genetic_algorithm(pop_size=100, mutation_rate=0.1, generations=100)
def genetic_algorithm(pop_size, mutation_rate, generations):
    # Asignamos la población en una lista con 8 reinas y una población de 100,
    population = [list(range(8)) for _ in range(pop_size)]
    # Iteramos por cada generacion para buscar la mejor solución
    for gen in range(generations):
        # Se inicializa la variable con cada nueva poblacion para que no se pise con la anterior
        new_population = []
        # Aqui iteramos por el tamaño de la población
        for _ in range(pop_size):
            # Selecciona a los padres de forma aleatoria
            parents = select_parents(population, fitness, 2)
            # Cruza los padres y guardamos al descendiente
            child = crossover(parents[0], parents[1])
            # Esta función determinará si el descendiente mutará o no
            child = mutate(child, mutation_rate)
            # Se agrega a la lista de la la nueva población
            new_population.append(child)
        # Guardamos esta generacion con las anteriores
        population = new_population
    # Se selecciona la mejor opcion
    best_chromosome = max(population, key=fitness)
    # Devolvemos el valor a la función principal
    return best_chromosome


def fitness(chromosome):
    # Función de aptitud: cuántas reinas no se amenazan mutuamente
    n = len(chromosome)
    clashes = 0
    for i in range(n):
        for j in range(i + 1, n):
            if chromosome[i] == chromosome[j] or abs(chromosome[i] -
                                                     chromosome[j]) == j - i:
                clashes += 1
    return n - clashes


def mutate(chromosome, mutation_rate):
    # Mutación de un cromosoma con una cierta probabilidad
    for i in range(len(chromosome)):
        if random.random() < mutation_rate:
            chromosome[i] = random.randint(0, len(chromosome) - 1)
    return chromosome


def select_parents(population, fitness_fn, num_parents):
    parents = []
    for _ in range(num_parents):
        # Realizar la selección por ruleta
        total_fitness = sum(fitness_fn(chrom) for chrom in population)
        pick = random.uniform(0, total_fitness)
        current_fitness = 0
        for chrom in population:
            current_fitness += fitness_fn(chrom)
            if current_fitness > pick:
                parents.append(chrom)
                break
    if len(parents) < 2:
        parents = select_parents(population, fitness_fn, num_parents)
        # Realizar una nueva selección si no se obtienen suficientes padres
    return parents


if __name__ == "__main__":
    best_solution = genetic_algorithm(pop_size=100, mutation_rate=0.1, generations=100)
    print("Mejor solución encontrada:", best_solution)
