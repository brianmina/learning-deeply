import plotly.express as px

from die import Die

die_1 = Die(6)
die_2 = Die(6)

results = []
for result in range(500):
    value = die_1.roll() * die_2.roll()
    results.append(value)

# Analyze data:
frequencies = []
max_results = die_1.num_sides * die_2.num_sides
times_results = range(1, max_results+1)
for item in times_results:
    items = results.count(item)
    frequencies.append(items)

fig = px.bar(x=times_results, y=frequencies)
fig.update_layout(xaxis_dtick=1)
fig.show()



