import random

# Hedef sayı
target_sum = 50

# Genetik Algoritma Fonksiyonu
def genetic_algorithm(population_size, gene_pool, target_sum, max_generations):
    # Başlangıç popülasyonunu oluştur
    population = []
    gene_pool_length = len(gene_pool)
    for _ in range(population_size):
        individual = [random.choice(gene_pool) for _ in range(gene_pool_length)]
        population.append(individual)
    
    # Genetik algoritma ana döngüsü
    for generation in range(max_generations):
        # Popülasyonu uygunluk fonksiyonuna göre değerlendir
        fitness_scores = [(individual, abs(sum(individual) - target_sum)) for individual in population]
        sorted_population = sorted(fitness_scores, key=lambda x: x[1])
        
        # En iyi bireyleri seç
        best_individual = sorted_population[0][0]
        
        # Hedefe ulaşıldı mı kontrol et
        if sum(best_individual) == target_sum:
            print("Hedefe ulaşıldı!")
            return best_individual
        
        # Yeni nesil oluştur (çaprazlama ve mutasyon)
        new_generation = []
        for _ in range(population_size):
            parent1, parent2 = random.choices(sorted_population[:population_size // 2], k=2)
            crossover_point = random.randint(0, len(parent1[0]) - 1)
            child = parent1[0][:crossover_point] + parent2[0][crossover_point:]
            mutated_child = mutate(child, gene_pool)
            new_generation.append(mutated_child)
        
        # Yeni nesli güncelle
        population = new_generation
    
    print("Hedefe ulaşılamadı.")
    return None

# Mutasyon işlemi
def mutate(individual, gene_pool):
    if random.random() < 0.1:
        index_to_mutate = random.randint(0, len(individual) - 1)
        individual[index_to_mutate] = random.choice(gene_pool)
    return individual

# Başlangıç parametreleri
population_size = 100
gene_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
max_generations = 1000

# Genetik algoritmayı çalıştır
solution = genetic_algorithm(population_size, gene_pool, target_sum, max_generations)

# Çözümü yazdır
if solution:
    print("Çözüm:", solution)
