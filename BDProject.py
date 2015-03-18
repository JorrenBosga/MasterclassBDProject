# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



import pandas as pd
import scipy as sp
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

data = pd.io.stata.read_stata("GSS2012.DTA")

## create age groups
def AgeGroup(data):
    AGE = {}     
    for i in range(10,90):
        AGE[i] = 0
        for ages in data.age:
            if i == ages:
                AGE[i] = AGE[i]+1
    agecounts = []
    for i in range(10,90):
        agecounts.append(AGE[i])
        
    return agecounts
     
## create race groups 
def RaceGroup(data):
    RACE = {}
    for race in data.race:
        if race not in RACE:
            RACE[race] = 1
        else:
            RACE[race] = RACE[race] + 1        
    # Proportions
    total = float((RACE['white'] + RACE['black'] + RACE['other']))
    whiteprop = float(RACE['white']) / total
    blackprop = float(RACE['black']) / total
    otherprop = float(RACE['other']) / total

    return whiteprop, blackprop, otherprop

## create sex groups
def SexGroup(data): 
    male = 0
    female = 0
    for sex in data.sex:
        if sex == 'male':
            male += 1
        if sex == 'female':
            female += 1
    # Proportions        
    maleprop = float(male) / float((male+female))
    femaleprop = float(female) / float((male+female))

    return maleprop, femaleprop        

        
## Creating income groups
def IncomeGroup(data):
    incomegroups = [[0,0,0,0,0,0,0,0,0,0,0,0,0],('nan','<1k','1k-3k','3k-4k','4k-5k','5k-6k','6k-7k','7k-8k','8k-10k','10k-15k','15k-20k','20k-25k','>25k')]
    for income in data.income:
        if income == 'nan':
            incomegroups[0][0] += 1
        elif income == 'LT $1000':
            incomegroups[0][1] += 1
        elif income == '$1000 TO 2999':
            incomegroups[0][2] += 1
        elif income == '$3000 TO 3999':
            incomegroups[0][3] += 1
        elif income == '$4000 TO 4999':
            incomegroups[0][4] += 1
        elif income == '$5000 TO 5999':
            incomegroups[0][5] += 1
        elif income == '$6000 TO 6999':
            incomegroups[0][6] += 1
        elif income == '$7000 TO 7999':
            incomegroups[0][7] += 1
        elif income == '$8000 TO 9999':
            incomegroups[0][8] += 1
        elif income == '$10000 - 14999':
            incomegroups[0][9] += 1
        elif income == '$15000 - 19999':
            incomegroups[0][10] += 1
        elif income == '$20000 - 24999':
            incomegroups[0][11] += 1
        elif income == '$25000 OR MORE':
            incomegroups[0][12] += 1
            
    return incomegroups

def ReligionList(data):
    religions = []
    for religion in data.relig:
        if religion in religions:
            pass
        else:
            religions.append(religion)
    return religions

def RelDist(data):
    beliebers = []
    for belieber in data.relig:
        beliebers.append(belieber)
    print type(beliebers)    
    sns.distplot(beliebers)
    return 
    
RelDist(data)
## Marital status
def maritalstatus(data):
    
    marriage = [[0,0,0,0,0], ('Never married', 'Divorced', 'Married', 'Separated', 'Widowed')]
    for marital in data.marital:
        if marital == 'NEVER MARRIED':
            marriage[0][0] += 1
        if marital == 'divorced':
            marriage[0][1] += 1
        if marital == 'married':
            marriage[0][2] += 1
        if marital == 'separated':
            marriage[0][3] += 1
        if marital == 'widowed':
            marriage[0][4] += 1
    return marriage

def sexualorientation(data):
    
    orientation = [[0,0,0,0], ('nan','bi','gay','straight')]
    for ornt in data.sexornt:
        if ornt == 'nan':
            orientation[0][0] +=1
        if ornt == 'Bisexual':
            orientation[0][1] +=1
        if ornt == 'Gay, lesban, or homosexual':
            orientation[0][2] +=1
        if ornt == 'Heterosexual or straight':
            orientation[0][3] +=1        
    return orientation
    
def degree(data):
    degree = [[0, 0, 0, 0, 0], ('High school', 'Junior college', 'LT high school', 'bachelor', 'graduate')]
    for degree in data.degree:
        if degree == 'HIGH SCHOOL':
            degree[0][0] += 1
        if degree == 'JUNIOR COLLEGE':
            degree[0][1] += 1
        if degree == 'LT HIGH SCHOOL':
            degree[0][2] += 1
        if degree == 'bachelor':
            degree[0][3] += 1
        if degree == 'graduate':
            degree[0][4] += 1
    return degree
            
def religion(data):
    religions = [[0,0,0,0,0,0],("Christian","Jewish","Hinduism/Buddhism", "Islam","Other", "none")]
    for religion in data.relig:
        if religion == "ORTHODOX-CHRISTIAN" or religion == "catholic" or religion == "christian" or religion == "protestant":
            religions[0][0] += 1
        if religion == "jewish":
            religions[0][1] += 1
        if religion == "buddhism" or religion == "hinduism":
            religions[0][2] += 1
        if religion == "MOSLEM/ISLAM":
            religions[0][3] += 1
        if religion == "none":
            religions[0][5] += 1
        else:
            religions[0][4] += 1
            
    return religions


def PlotAgeSexRace(data): 
    '''Returns 3 plots with age, sex, and race distributions.'''
    age = AgeGroup(data)
    sex = SexGroup(data)
    race = RaceGroup(data)
    
    # Figure size
    plt.figure(1,(5,11))
        
    ageplot = plt.subplot(3,1,1)
    ageplot.bar(range(10,90), age)
    # Labels for age plot
    plt.title("Age Distribution")
    plt.xlabel("age")
    plt.ylabel("frequency")
    
    sexplot = plt.subplot(3,1,2)
    sexplot.bar([1,2], [sex[0], sex[1]])
    # labels for sex plot
    plt.title("Gender Distribution")
    plt.xticks([1.5,2.5], ("Male", "Female"))
    plt.ylabel("Probabiliy")
    plt.ylim(0,1)
    raceplot = plt.subplot(3,1,3)
    raceplot.bar([1,2,3], [race[0], race[1], race[2]], 0.5)
    plt.xticks([1.25,2.25,3.25], ('White', 'Black', 'Other'))
    plt.title("Race Distribution")      
    plt.ylabel("Probability")
    plt.ylim(0,1)


def PlotIncome(data):
    '''Returns a plot with income distribution.'''
    incomegroups = IncomeGroup(data)
    
    # Figure size
    plt.figure(2,(9,5))
    
    plt.bar(range(0,13,1), incomegroups[0], 1)
    plt.xticks(np.arange(0.5,12.5,1), incomegroups[1])


def PlotMaritalSexOrnt(data):
    marstate = maritalstatus(data)    
    sexornt = sexualorientation(data)
    # Figure Size
    plt.figure(3, (5,7))
    
    # Marital status plot
    plt.subplot(2,1,1)
    plt.title("Marital Status")
    plt.bar([0, 1, 2, 3, 4], marstate[0])
    plt.xticks(np.arange(0.5, 5.5, 1), marstate[1])
    
    # Sexual Orientation plot
    plt.subplot(2,1,2)
    plt.title("Sexual orientation")
    plt.bar([0,1,2,3], sexornt[0])
    plt.xticks(np.arange(0.5,4.5,1), sexornt[1])

