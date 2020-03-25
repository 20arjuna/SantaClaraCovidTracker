import matplotlib.pyplot as p
import numpy as np
import requests

def plotGraph():

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

def getCases():
    r = requests.get("https://www.sccgov.org/sites/phd/DiseaseInformation/novel-coronavirus/Pages/home.aspx")
    sourceCode = r.text
    index = sourceCode.find("Total_Confirmed_Cases")
    cases = int(sourceCode[index+24:index+27])
    return cases


if __name__ == '__main__':
    cases = getCases()
    print(cases)
    plotGraph()
