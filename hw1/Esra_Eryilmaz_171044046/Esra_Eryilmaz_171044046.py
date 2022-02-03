# Author : Esra Eryılmaz - 171044046
# MATH 118: Statistics and Probability
# Homework 1
# 24.04.2021

import pandas as pd
import numpy as numpy
import math


fileName = 'owid-covid-data.xlsx'
sheetName = 'Sheet1'
dash = '-' * 100
dash2 = '-' * 240

file = open("output.txt", "w")
df = pd.read_excel(fileName, sheet_name=sheetName, usecols="C")
countries = df.to_numpy()       # countries array, I used it in many functions


# problem1
def number_of_countries():
    numb_countries = []
    for i in countries:
        if i not in numb_countries:
            numb_countries.append(i)
    file.write("\t\t\t" + str(len(numb_countries)) + " countries\n")

# problem2
def earliest_date(column):
    df = pd.read_excel(fileName, sheet_name=sheetName, usecols=column)
    date = df.to_numpy()
    file.write("\t\t\t" + str(date.min()) + " " + str(countries[numpy.where(date == date.min())]) + "\n")

# problem3
def total_case(column):
    df = pd.read_excel(fileName, sheet_name=sheetName, usecols=column)
    case = df.to_numpy().tolist()
    for i in range(1,len(countries)-1):
        if (countries[i] != countries[i+1]) or (i == len(countries)-2):
            file.write('{:<10s}{:<25s}{:>10s}'.format(" ", str(countries[i]), str(case[i]) ) + "\n")

# problem4
def total_death(column):
    df = pd.read_excel(fileName, sheet_name=sheetName, usecols=column)
    death = df.to_numpy().tolist()
    for i in range(1,len(countries)-1):
        if (countries[i] != countries[i+1]) or (i == len(countries)-2):
            file.write('{:<10s}{:<25s}{:>10s}'.format(" ", str(countries[i]), str(death[i]) ) + "\n")


# problem5,6,7,8,9,10,12,13
def find_min_max_avg_var(column):
    df = pd.read_excel(fileName, sheet_name=sheetName, usecols=column)
    arr = df.to_numpy()

    file.write("\t\t" + dash + '\n')
    file.write('{:<10s}{:<25s}{:>15s}{:>15s}{:>15s}{:>15s}'.format(" " ,"Country", "minimum", "maximum", "average", "variation\n"))
    file.write("\t\t" + dash + '\n')
    start, finish = 0, 0
    flag = False
    tempArr = []

    for i in range(0,len(arr)-1):
        if countries[i] == countries[i+1]:
            finish += 1
        if (countries[i] != countries[i+1]) or (i == len(arr)-2):  # country change point o(-2 for to take the last country)
            for k in range(start, finish):
                if math.isnan(arr[k]) == False:
                    minValue = arr[k]
                    maxValue = arr[k]
                    flag = True
                    break

            if flag == False:       # if all values in that country are nan
                file.write('{:<10s}{:<25s}{:>15s}{:>15s}{:>15s}{:>15s}'.format(" ", str(countries[i]), "[nan]","[nan]","[nan]","[nan]")+'\n')
                finish += 1
                start = finish
                continue        # there is no value in this country; continue to other country

            total, x = 0, 0
            for j in range(start, finish):          # finding min max
                if math.isnan(arr[j]) == False:        # if data exist 
                    if minValue > arr[j]:
                        minValue = arr[j]
                    if maxValue < arr[j]:
                        maxValue = arr[j]
                    tempArr.append(arr[j])
                    total = total + arr[j]
                    x = x + 1

            avgValue = total / x        # average

            file.write('{:<10s}{:<25s}{:>15s}{:>15s}{:>15s}{:>15s}'.format( " ", str(countries[i]), str(minValue), str(maxValue), 
                                                                            str(avgValue), str(variance(tempArr))) + '\n')
            finish += 1
            start = finish
            flag = False
            tempArr = []        # make temp empty

def variance(data):
    n = len(data)
    mean = sum(data) / n
    deviations = [(x - mean) ** 2 for x in data]
    variance = sum(deviations) / n
    return variance


# problem11,14,15,16
def test_vaccination(column):
    df = pd.read_excel(fileName, sheet_name=sheetName, usecols=column)
    arr = df.to_numpy()
    total = 0
    for i in range(1,len(countries)-1):
        if math.isnan(arr[i]) == False:
            total = arr[i]
        if (countries[i] != countries[i+1]) or (i == len(countries)-2):
            file.write('{:<10s}{:<25s}{:>10s}'.format(" ", str(countries[i]), str(total) ) + "\n")
            total = 0

# problem17
def list_info():
    """
    population          -> AS
    median_age          -> AU
    aged_65_older       -> AV
    aged_70_older       -> AW
    economic_perf       -> AX
    heart_disease_rate  -> AZ
    diabetes_prevalence -> BA
    female_smokers      -> BB
    male_smokers        -> BC
    handwashing_fac     -> BD
    hospital_beds       -> BE
    life_expectancy     -> BF
    human_dev_index     -> BG
    """

    df = pd.read_excel(fileName, sheet_name=sheetName, usecols="AS")
    population = df.to_numpy()
    df = pd.read_excel(fileName, sheet_name=sheetName, usecols="AU")
    median_age = df.to_numpy()
    df = pd.read_excel(fileName, sheet_name=sheetName, usecols="AV")
    aged_65_older = df.to_numpy()
    df = pd.read_excel(fileName, sheet_name=sheetName, usecols="AW")
    aged_70_older = df.to_numpy()
    df = pd.read_excel(fileName, sheet_name=sheetName, usecols="AX")
    economic_perf = df.to_numpy()
    df = pd.read_excel(fileName, sheet_name=sheetName, usecols="AZ")
    heart_disease_rate = df.to_numpy()
    df = pd.read_excel(fileName, sheet_name=sheetName, usecols="BA")
    diabetes_prevalence = df.to_numpy()
    df = pd.read_excel(fileName, sheet_name=sheetName, usecols="BB")
    female_smokers = df.to_numpy()
    df = pd.read_excel(fileName, sheet_name=sheetName, usecols="BC")
    male_smokers = df.to_numpy()
    df = pd.read_excel(fileName, sheet_name=sheetName, usecols="BD")
    handwashing_fac = df.to_numpy()
    df = pd.read_excel(fileName, sheet_name=sheetName, usecols="BE")
    hospital_beds = df.to_numpy()
    df = pd.read_excel(fileName, sheet_name=sheetName, usecols="BF")
    life_expectancy = df.to_numpy()
    df = pd.read_excel(fileName, sheet_name=sheetName, usecols="BG")
    human_dev_index = df.to_numpy()

    file.write(dash2 + '\n')
    file.write('{:<15s}{:>20s}{:>10s}{:>10s}{:>10s}{:>10s}{:>10s}{:>10s}{:>10s}{:>10s}{:>10s}{:>10s}{:>10s}{:>10s}'
                .format("  Country", "|population|", "|median age|", "|people 65 older|", "|people 70 older|",
                "|economic perf.|", "|death;heart disease|", "|diabetes prev.|", "|female smokers|", "|male smokers|",
                "|handwashing fac.|", "|hospital beds|", "|life expectancy|", "|human dev. index|\n"))
    file.write(dash2 + '\n')

    for i in range(1,len(countries)-1):
        if (countries[i] != countries[i+1]) or (i == len(countries)-2):
            file.write('{:<15s}{:>20s}{:>10s}{:>15s}{:>15s}{:>20s}{:>20s}{:>15s}{:>15s}{:>15s}{:>15s}{:>15s}{:>15s}{:>15s}'
                        .format(str(countries[i]), str(population[i]), str(median_age[i]), str(aged_65_older[i]),
                        str(aged_70_older[i]), str(economic_perf[i]), str(heart_disease_rate[i]), str(diabetes_prevalence[i]),
                        str(female_smokers[i]), str(male_smokers[i]), str(handwashing_fac[i]), str(hospital_beds[i]),
                        str(life_expectancy[i]), str(human_dev_index[i])) + '\n')


# Driver code
def main():
    file.write('{:>30s}{:>40s}{:>30s}'.format("- MATH 118 -\n", "Statistics and Probability\n","Homework #1\n\n"))

    file.write("PROBLEM 1 : How many countries the dataset has?\n")
    number_of_countries()

    file.write("\nPROBLEM 2 : When is the earliest date data are taken for a country? Which country is it?\n")
    earliest_date("D")

    file.write("\nPROBLEM 3 : How many cases are confirmed for each country so far? Print pairwise results of country and total cases.\n")
    total_case("E")

    file.write("\nPROBLEM 4 : How many deaths are confirmed for each country so far? Print pairwise results of country and total deaths.\n")
    total_death("H")

    file.write("\nPROBLEM 5 : What are the average, minimum, maximum and variation values of the reproduction rates for each country?\n")
    find_min_max_avg_var("Q")

    file.write("\nPROBLEM 6 : What are the average, minimum, maximum and variation values of the icu patients (intensive care unit patients) for each country?\n")
    find_min_max_avg_var("R")

    file.write("\nPROBLEM 7 : What are the average, minimum, maximum and variation values of the hosp patients (hospital patients) for each country?\n")
    find_min_max_avg_var("T")

    file.write("\nPROBLEM 8 : What are the average, minimum, maximum and variation values of the weekly icu (intensive care unit) admissions for each country?\n")
    find_min_max_avg_var("V")

    file.write("\nPROBLEM 9 : What are the average, minimum, maximum and variation values of the weekly hospital admissions for each country?\n")
    find_min_max_avg_var("X")

    file.write("\nPROBLEM 10 : What are the average, minimum, maximum and variation values of new tests per day for each country?\n")
    find_min_max_avg_var("Z")

    file.write("\nPROBLEM 11 : How many tests are conducted in total for each country so far?\n")
    test_vaccination("AA")

    file.write("\nPROBLEM 12 : What are the average, minimum, maximum and variation values of the positive rates of the tests for each country?\n")
    find_min_max_avg_var("AF")

    file.write("\nPROBLEM 13 : What are the average, minimum, maximum and variation values of the tests per case for each country?\n")
    find_min_max_avg_var("AG")

    file.write("\nPROBLEM 14 : How many people are vaccinated by at least one dose in each country?\n")
    test_vaccination("AJ")

    file.write("\nPROBLEM 15 : How many people are vaccinated fully in each country?\n")
    test_vaccination("AK")

    file.write("\nPROBLEM 16 : How many vaccinations are administered in each country so far?\n")
    test_vaccination("AI")

    file.write("\nPROBLEM 17 : List information about population, median age, # of people aged 65 older, # of people aged 70 older, economic performance, death rates due to heart disease, diabetes prevalence, # of female smokers, # of male smokers, handwashing facilities, hospital beds per thousand people, life expectancy and human development index.\n")
    list_info()

    file.close()


if __name__=="__main__": 
    main()
