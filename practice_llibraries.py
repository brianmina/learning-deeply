import matplotlib.pyplot as plt

from die import Die


die_1 = Die(6)
die_2 = Die(6)
die_3 = Die(6)

#results = []
# for value in range(1_000):
result = die_1.roll() + die_2.roll() + die_3.roll()
print(result)
#     results.append(result)

results = [die_1.roll() + die_2.roll() + die_3.roll() for value in range(1_000)]

print(results)

# Analyze the results using count()

#frequencies = []
max_results = die_1.num_sides + die_2.num_sides + die_3.num_sides
poss_results = range(1, max_results+1)
# for value_freq in poss_results:
#     frequency = results.count(value_freq)
#     frequencies.append(frequency)

frequencies = [results.count(value_freq) for value_freq in poss_results]
print(frequencies)