from die import Die
import plotly.express as px

# Create a D6.
die_1 = Die()
die_2 = Die()

# Make some rolls, and store results in list.
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

print(results)

# Analyze the results.
frequencies = []
max_results = die_1.num_sides + die_2.num_sides
poss_results = range(1, max_results+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

# Visualize the results.
title = "Results of rolling two dice"
labels = {'x': 'Result', 'y': 'Frequency'}
fig = px.line(x=poss_results, y=frequencies, title=title, labels=labels)
fig.show()