# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 14:11:02 2022

@author: Zifan Ma
"""
# Counting Number of Significance Reference to https://stackoverflow.com/questions/8142676/python-counting-significant-digits
import pandas as pd
import numpy as np
import glob

lib = [] #library stores all results
str_lib = [] #library stores all results with string

templib = [] #temporary list

#Obtaining all xlsx files
xlsx_dir = r"C:\Users\Zifan Ma\OneDrive - Washington University in St. Louis\2021- WashU\TA Automatic Grade Project\xlsx"
#xlsx_dir = r"C:\Users\m.zifan\OneDrive - Washington University in St. Louis\2021- WashU\TA Automatic Grade Project\xlsx"
filenames = glob.glob(xlsx_dir + "/*.xlsx")

#Extracting all student data in lib
for filename in filenames: 
    inputs = pd.read_excel(filename)
    inputs.drop(inputs.columns[1:5], axis = 1, inplace = True)   
    #print(inputs.iloc[:,1][2]) #All number for same Student
    templib.append(inputs.iloc[:,1])
lib = pd.DataFrame(templib).T.to_numpy() 
str_lib = lib.astype(str)

#First Function: Judge if student write correctly or not in a range
#For instance the rubrics are:
#1. Correct 2. -2 (Miss)

def rangejudger_ratio(objects, compare, ratio, a): #You can add more delta if needed
#Custom rangejudger whenever needed
    if compare*(1-ratio) <= objects*a <= compare*(1+ratio):
        print('1') #We may append it to operations related to auto grading in the future
    if not (compare*(1-ratio) <= objects*a <= compare*(1+ratio)):
        print('2')

def rangejudger_direct(objects, compare, delta1): #You can add more delta if needed
#Custom rangejudger whenever needed
    if compare-delta1 <= objects <= compare+delta1:
        print('1') #We may append it to operations related to auto grading in the future
    if not (compare-delta1 <= objects <= compare+delta1):
        print('2')
    

def valuejudger(objects, compare): 
#Custom rangejudger whenever needed
    if compare == objects:
        print('1') #We may append it to operations related to auto grading in the future
    if compare != objects:
        print('2')

def SF(x): #Number of Significance Figures #Use str_lib
#https://stackoverflow.com/questions/8142676/python-counting-significant-digits
    '''Returns the number of significant digits in a number. This takes into account
       strings formatted in 1.23e+3 format and even strings such as 123.450'''
    # change all the 'E' to 'e'
    x = str(x)
    x = x.lower().lstrip('-')

    if ('e' in x):
        # return the length of the numbers before the 'e'
        myStr = x.split('e')
        if '.' in x:
            if not (1 <= float(myStr[0]) < 10) :
                return ('Zifan Error Notification: Error Type1: Something like 0.5E-5 or -19.3E9')
            else:
                return (len( myStr[0] ) - 1) # to compenstate for the decimal point
        if '.' not in x:
            if not (1 <= float(myStr[0]) < 10) :
                return ('Zifan Error Notification: Error Type2: Something like -31E7')
            else:
                return (len( myStr[0])) # Not to compenstate for the decimal point
    else:
        # put it in e format and return the result of that
        ### NOTE: because of the 8 below, it may do crazy things when it parses 9 sigfigs
        n = ('%.*e' %(18, float(x))).split('e')
        # remove and count the number of removed user added zeroes. (these are sig figs)
        if '.' in x:
            s = x.replace('.', '')
            #number of zeroes to add back in
            l = len(s) - len(s.rstrip('0'))
            #strip off the python added zeroes and add back in the ones the user added
            n[0] = n[0].rstrip('0') + ''.join(['0' for num in range(l)])
        else:
            #the user had no trailing zeroes so just strip them all
            n[0] = n[0].rstrip('0')
        #pass it back to the beginning to be parsed
    return SF('e'.join(n)) 

def DP(x):
    x = x.lower().lstrip('-')
    if ('e' in x):
        # return the length of the numbers before the 'e'
        myStr = x.split('e')
        if '.' in x:
            '''PB Here'''
            return (len(myStr[0].split('.')[1])) # to compenstate for the decimal point
        if '.' not in x:
            return (0) # Not to compenstate for the decimal point
    if not('e' in x):
        if '.' in x:
            myStr = x.split('.')
            return(len(myStr[1]))
        if not '.' in x:
            return(0) 
        
#Specific For Each Experiment
for i in range(len(lib)):  
    #Judgings that lead to how I will grade:
    print('Student', i+1)
    #Usually objects and compare is lib[i][somenumber]
    #21X
    rangejudger_ratio(lib[i][1],lib[i][0],0.05,24.31)
    rangejudger_direct(lib[i][2],lib[i][1],3)
    rangejudger_direct(lib[i][4],lib[i][3]-lib[i][2],0.2)
    rangejudger_direct(lib[i][5],293,5)
    rangejudger_ratio(lib[i][6],lib[i][5]*lib[i][4],0.05,1)
    rangejudger_ratio(lib[i][7],lib[i][6]/lib[i][1],0.05,1)
    #22X
    rangejudger_ratio(lib[i][8],lib[i][0],0.05,24.31)
    rangejudger_direct(lib[i][9],lib[i][8],3)
    rangejudger_direct(lib[i][12],lib[i][10]-lib[i][9],0.2)
    rangejudger_direct(lib[i][13],293,5)
    rangejudger_ratio(lib[i][14],lib[i][13]*lib[i][12],0.05,1)
    rangejudger_ratio(lib[i][15],lib[i][14]/lib[i][8],0.05,1)
    #5,6,7,8
    rangejudger_direct(lib[i][16],0.2/lib[i][4]*100,0.3)
    rangejudger_direct(lib[i][17],2,0.2)
    rangejudger_direct(lib[i][18],(lib[i][15]+lib[i][16])*lib[i][16]/100,5)
    rangejudger_ratio(lib[i][19],lib[i][7]-lib[i][6]-285.85,0.05,1)
    #111X
    rangejudger_direct(lib[i][22],lib[i][21]-lib[i][20],0.2)
    rangejudger_direct(lib[i][23],335,10)
    rangejudger_ratio(lib[i][24],lib[i][23]*lib[i][22],0.05,1)
    rangejudger_direct(lib[i][25],lib[i][24]/55810,0.003)
    rangejudger_direct(lib[i][26],lib[i][25]/(40e-3),0.03)
    #112X
    rangejudger_direct(lib[i][29],lib[i][21]-lib[i][20],0.2)
    rangejudger_direct(lib[i][30],335,10)
    rangejudger_ratio(lib[i][31],lib[i][30]*lib[i][29],0.05,1)
    rangejudger_direct(lib[i][32],lib[i][31]/55810,0.003)
    rangejudger_direct(lib[i][33],lib[i][32]/(40e-3),0.03)





    '''
    Result for student 3:
        Student 3
3
3
3
1
Though student 3 made the 3rd answer incorrect, the fourth answer is graded correctly according to his/her own 3rd answer
'''

