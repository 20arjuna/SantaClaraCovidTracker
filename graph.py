import matplotlib.pyplot as p

daysFile = open("days.txt", "r")
infectedFile = open("infected.txt", "r")

daysLines = daysFile.readlines()
infectedLines = infectedFile.readlines()

days = []
infected = []

for line in daysLines:
     days.append(int(line))
for line in infectedLines:
    infected.append(int(line))

p.plot(days, infected)
p.xlabel('Days since 1st case')
p.ylabel('Total Infected')
p.title('COVID-19 cases in Santa Clara County')
p.show()
