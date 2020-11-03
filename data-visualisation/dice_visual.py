import pygal
from random import randint


class Dice():
    """Class created to show single dice roll"""
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        """Returns value from range of roll"""
        return randint(1, self.num_sides)


dice = Dice()

results = []
for roll_num in range(100000):
    result = dice.roll()
    results.append(result)

#results analysis
frequencies = []
for value in range(1, dice.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#results visualization
hist = pygal.Bar()
hist.force_uri_protocol = 'http'

hist.title = "Results of hundred thousands rolls of single D6 dice "
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Values"
hist.y_title = "Frequency of the value"

hist.add('D6', frequencies)
hist.render_to_file('dice_visual.svg')
print("Data rendering complete. Your rendered visualisation is generated as .svg file in folder containing program.")
