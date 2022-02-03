# Author : Esra Eryılmaz - 171044046
# MATH 118: Statistics and Probability
# Homework 2
# 03.06.2021

import numpy as np
import math
import matplotlib.pyplot as plt

fileName = 'manufacturing_defects.txt'
defects = [0, 1, 2, 3, 4]


# problem a
def number_of_cases(arr):
    table1 = []
    print("\n# of Defects    | # of Cases")
    print("-----------------------------")
    for k in defects:
        count = 0
        for line in arr:
            count = count + line[1:].count(str(k))  # Take each column except first column
        table1.append(count)
        print(k ,"\t\t|\t", table1[k])
    return table1


# problem b
def estimate_lambda(table1):
    total_defects, total_case = 0, 0
    for i in defects:
        total_defects += i * table1[i]
        total_case += table1[i]

    lambdaa = total_defects/total_case    # Lambda = total number of defects / total number of cases
    print("\nLambda : " ,lambdaa)
    return lambdaa, total_case


# problem c
def find_predicted_cases(table1, lambdaa, total_case):
    table2 = []
    temp = 0
    print("\n# of Defects    |  # of Cases   |  Predicted # of Cases")
    print("--------------------------------------------------------")

    for k in defects:
        temp = (pow(math.e, -1*lambdaa) * pow(lambdaa, k)) / math.factorial(k)  # apply poisson distribution formula
        temp *= total_case
        temp = round(temp,4)
        table2.append([table1[k], temp])
        print(k ,"\t\t|\t", table2[k][0], "\t|\t" , table2[k][1])

    return table2


# problem d
def draw_barplot(table2):
    # Set width of bar
    barWidth = 0.2

    # Set height of bar
    actual, predicted = [], []
    for i in defects:
        actual.append(table2[i][0])     # height of actual case bar
        predicted.append(table2[i][1])  # height of predicted case bar

    # Set position of bar on X axis
    x_axis = np.arange(len(defects))
    
    # Make the plot
    plt.bar(x_axis, actual, color ='purple', width = barWidth, label ='Actual Cases')
    plt.bar(x_axis + barWidth, predicted, color ='orange', width = barWidth, label ='Predicted Cases')

    plt.title('Actual - Predicted Cases', fontweight ='bold', fontsize = 15)
    plt.xlabel('# of defects', fontweight ='bold', fontsize = 10)
    plt.ylabel('# of cases', fontweight ='bold', fontsize = 10)
    plt.xticks(x_axis + barWidth, defects)

    plt.legend()
    plt.show()



# Driver code
def main():
    arr = []
    # Read the file line by line and each line is a list in itself
    with open(fileName, 'r') as infile:
        data = infile.readlines()
        for i in data:
            line = i.split()
            arr.append(line)
    infile.close()

    # Problem a (find total number of cases in all company)
    table1 = number_of_cases(arr)

    # Problem b (find lambda)
    lambdaa, total_case = estimate_lambda(table1)

    # Problem c (find poisson predicted cases with estimated lambda)
    table2 = find_predicted_cases(table1, lambdaa, total_case)

    # Problem d (draw barplot)
    draw_barplot(table2)



if __name__=="__main__": 
    main()
