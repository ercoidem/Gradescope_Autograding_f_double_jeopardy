# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 14:11:02 2022

@author: Zifan Ma
"""
#APPLY YOUR RUBRICS EVERYTIME!

#This is the main program for grading, including setting relationship between questions
#and converting relationships to rubrics

import Library_for_student_values_and_name
lib = Library_for_student_values_and_name.library()
#lib stores values of each questions in each list
import pandas as pd
names = pd.DataFrame(lib[1]).T.to_numpy()[0]
grades = []
rubrics = []

#Return 
def main_for_grading():
# Here we convert it to values of each student in each list 
    str_values = pd.DataFrame(lib[0]).T.to_numpy() #type = String!! Use this to judge PD and SF!
    values = pd.DataFrame(lib[0]).T.to_numpy().astype(float) #type = float!!
    
    i = 0

    import judgers as j
    for i in range(len(values)):  
        #Judgings that lead to how I will grade:
        print('Student', i+1)
        #Usually objects and compare is values[i][somenumber]
        
        #21X
        grades.append(j.ran_rat(values[i][1],values[i][0],0.05,24.31))
        grades.append(j.ran_dir(values[i][2],21.0,3)) #2
        grades.append(j.ran_dir(values[i][4],values[i][3]-values[i][2],0.2))#4
        grades.append(j.ran_dir(values[i][5],293,5))#5_1,2
        grades.append(j.ran_rat(values[i][6],values[i][5]*values[i][4],0.05,1))#5_1,2
        grades.append(j.ran_rat(values[i][7],values[i][6]/values[i][1],0.05,1))#6 _1,2
        #22X
        grades.append(j.ran_rat(values[i][9],values[i][8],0.05,24.31))
        grades.append(j.ran_dir(values[i][10],21.0,3))#2
        grades.append(j.ran_dir(values[i][12],values[i][11]-values[i][10],0.2))#4
        grades.append(j.ran_dir(values[i][13],293,5))#5 _1,2
        grades.append(j.ran_rat(values[i][14],values[i][13]*values[i][12],0.05,1))#5 _1,2
        grades.append(j.ran_rat(values[i][15],values[i][14]/values[i][8],0.05,1))#6 _1,2
        #5,6,7,8
        grades.append(j.ran_dir(values[i][16],0.2/values[i][4]*100,0.3))#7 _1,2
        grades.append(j.ran_dir(values[i][17],2,0.2))#8 _1,2
        grades.append(j.ran_dir(values[i][18],100,5)) #9 _1
        grades.append(j.ran_dir(values[i][18],(values[i][15]+values[i][16])*values[i][16]/100,5)) #9 _2
        grades.append(j.ran_rat(values[i][19],values[i][7]-values[i][6]-285.85,0.05,1)) #10 _1 and 4, maybe have to look for other options
        #111X
        grades.append(j.ran_dir(values[i][22],values[i][21]-values[i][20],0.2))#15 _1,2
        grades.append(j.ran_dir(values[i][23],335,10))
        grades.append(j.ran_rat(values[i][24],values[i][23]*values[i][22],0.05,1))
        grades.append(j.ran_dir(values[i][25],values[i][24]/55810,0.003))
        grades.append(j.ran_dir(values[i][26],values[i][25]/(40e-3),0.03))
        #112X
        grades.append(j.ran_dir(values[i][29],values[i][21]-values[i][20],0.2))
        grades.append(j.ran_dir(values[i][30],335,10))
        grades.append(j.ran_rat(values[i][31],values[i][30]*values[i][29],0.05,1))
        grades.append(j.ran_dir(values[i][32],values[i][31]/55810,0.003))
        grades.append(j.ran_dir(values[i][33],values[i][32]/(40e-3),0.03))
       
        j.DP(str_values[i][4],1)#4 _3
        j.DP(str_values[i][12],1)#4 _3
        j.SF(str_values[i][5],3)#5 _4
        j.SF(str_values[i][6],3)#5 _4
        j.SF(str_values[i][13],3)#5 _4
        j.SF(str_values[i][14],3)#5 _4
        j.SF(str_values[i][7],3)#6 _4
        j.SF(str_values[i][15],3)#6 _4
        j.SF(str_values[i][16],1)#7 _3
        j.SF(str_values[i][17],1)#8 _3
        j.SF(str_values[i][18],1)#9 _4
#Change Grade Codes into Rubrics selections on gradescope
#m means that this problem cannot be graded automatically, has to be graded mannually 
#append . everytime so that it can change from questions   
#. separates questions, in this manner we can multichoose rubrics

        rubric = []

#0
        rubric.append('m')
        rubric.append('.') 
#1      
        rubric.append('m')
        rubric.append('.') 
#2      
        if j.ran_dir(values[i][2],21.0,3) and j.ran_dir(values[i][10],21.0,3):
            rubric.append('1')
        else :
            rubric.append('2')
        rubric.append('.')  
#3      
        rubric.append('1')
        rubric.append('.')
#4      
        if j.ran_dir(values[i][4],values[i][3]-values[i][2],0.2) and j.ran_dir(values[i][12],values[i][11]-values[i][10],0.2):
            rubric.append('1')
        else :
            rubric.append('2')
        if not (j.DP(str_values[i][4],1) and j.DP(str_values[i][12],1)):
            rubric.append('3')
        rubric.append('.')  
#5      
        if j.ran_rat(values[i][6],values[i][5]*values[i][4],0.05,1) and j.ran_rat(values[i][14],values[i][13]*values[i][12],0.05,1):
            rubric.append('1')
        else :
            rubric.append('2')
        if not (j.SF(str_values[i][5],3) and  j.SF(str_values[i][6],3 and j.SF(str_values[i][13],3) and j.SF(str_values[i][14],3))):
            rubric.append('4')
        rubric.append('.')
#6      
        if j.ran_rat(values[i][7],values[i][6]/values[i][1],0.05,1) and j.ran_rat(values[i][15],values[i][14]/values[i][8],0.05,1):
            rubric.append('1')
        else :
            rubric.append('2')
        if not (j.SF(str_values[i][7],3) and j.SF(str_values[i][15],3)):
            rubric.append('4')
        rubric.append('.')
#7
        if j.ran_dir(values[i][16],0.2/values[i][4]*100,0.3):
            rubric.append('1')
        else :
            rubric.append('2')
        if not (j.SF(str_values[i][16],1)):
            rubric.append('3')
        rubric.append('.')
#8
        if j.ran_dir(values[i][17],2,0.2):
            rubric.append('1')
        else :
            rubric.append('2')
        if not (j.SF(str_values[i][17],1)):
            rubric.append('3')
        rubric.append('.')
#9
        if j.ran_dir(values[i][18],(values[i][15]+values[i][16])*values[i][16]/100,5):
            rubric.append('1')
        else :
            rubric.append('2')
        if not (j.SF(str_values[i][18],1)):
            rubric.append('3')
        rubric.append('.')  
#10
        if j.ran_rat(values[i][19],values[i][7]-values[i][6]-285.85,0.05,1):
            rubric.append('1')
#11
        rubric.append('m')
        rubric.append('.') 
#12      
        rubric.append('m')
        rubric.append('.') 
#13
        rubric.append('m')
        rubric.append('.') 
#14      
        rubric.append('m')
        rubric.append('.')
#15
        if j.ran_dir(values[i][22],values[i][21]-values[i][20],0.2):
            rubric.append('1')
        else :
            rubric.append('2')
#16
        rubric.append('m')
        rubric.append('.') 
#17      
        rubric.append('m')
        rubric.append('.')    
#18
        rubric.append('1')
        rubric.append('.') 
#19      
        rubric.append('1')
        rubric.append('.')
#Missed 16 and 17
        rubrics.append(rubric)
    #return grades,values,str_values,names,rubric,rubrics,'You should Mannually check question 11([10]) and ELN late condition'
    return names,rubrics,'You should Mannually check question 11([10]) and ELN late condition'
