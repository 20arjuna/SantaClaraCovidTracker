import matplotlib.pyplot as p
import numpy as np
daysFile = open("days.txt", "r")
infectedFile = open("infected.txt", "r")

daysLines = daysFile.readlines()
infectedLines = infectedFile.readlines()

days = []
infected = []

for line in daysLines:
     days.append(line.rstrip("\n"))

for line in infectedLines:
    infected.append(int(line))

p.plot(days, infected)
p.xlabel('Date')
p.ylabel('Total Infected')
p.title('COVID-19 cases in Santa Clara County')

p.xticks(np.arange(0, len(days), step=14))
p.show()
