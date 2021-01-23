import matplotlib.pyplot as plt
import pandas as pd
import math
import time
import csv
import random


class sortedList():
    def __init__(self,data,comparisions,runningTime):
        self.data = data
        self.comparisions = comparisions
        self.runningTime = runningTime

    def __str__(self):
        return f'{self.comparisions:<7} \t {self.runningTime:<7}'

class timeComplexity():
    def __init__(self,avg,best,worst):
            self.avg = avg
            self.best = best
            self.worst = worst
        
    def __str__(self):
        return f'{len(self.avg.data):<7}  {self.avg.__str__()} \t {self.best.__str__()} \t {self.worst.__str__()}'

def getNumbers():
    try:
        numbersFile = open('numbers.txt', "r")
        numbers = []
        for number in numbersFile:
            numbers.append(int(number))
    except FileNotFoundError:
        print("File Not Found")
        exit(-1)
    finally:
        numbersFile.close()
    return numbers

def getGraph():
    comparisions = pd.read_csv('comparisions.csv')
    comparisions = comparisions.sort_values("SIZE")
    size = comparisions["SIZE"]
    plt.plot(size,comparisions["WORST"])
    plt.plot(size,comparisions["AVERAGE"])
    plt.plot(size,comparisions["BEST"])
    plt.plot(size,[x*math.log2(x) for x in size],'--')
    plt.plot(size,[x*x for x in size],'--')
    plt.legend(["WORST","AVERAGE","BEST","nlogn","n^2"])    
    plt.xlabel('Input Size')
    plt.ylabel('Number of Comparisons')
    plt.ylim(0, 20000)
    plt.xlim(0, 1000)
    plt.savefig('graph.png')
    # plt.show()
    plt.close()

def getComparisonCSV(data):
    try:
        with open('comparisions.csv', mode='w') as c:
            writer = csv.writer(c)
            writer.writerow(['SIZE','AVERAGE','BEST','WORST'])
            for t in data:
                writer.writerow([len(t.avg.data),t.avg.comparisions,t.best.comparisions,t.worst.comparisions])
    except RuntimeError:
        print(RuntimeError)