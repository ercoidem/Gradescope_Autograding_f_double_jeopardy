# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 13:37:49 2022

@author: Zifan Ma
"""
#Previously used in main for grading
'''    
    import pandas
    import numpy
    import glob
 
    lib = [] #library stores all results
    str_lib = []
    
    templib = []
    
    #Obtaining all xlsx files
    xlsx_dir = r"C:\Users\Zifan Ma\OneDrive - Washington University in St. Louis\2021- WashU\TA Automatic Grade Project\xlsx"
    filenames = glob.glob(xlsx_dir + "/*.xlsx")
    
    #Extracting all student data in lib
    for filename in filenames: 
        inputs = pd.read_excel(filename)
        inputs.drop(inputs.columns[1:5], axis = 1, inplace = True)   
        #print(inputs.iloc[:,1][2]) #All number for same Student
        templib.append(inputs.iloc[:,1])
    lib = pd.DataFrame(templib).T.to_numpy() 
    str_lib = lib.astype(str)
''' 
 
'''   
    for i in range(len(lib)):  
        #Judgings that lead to how I will grade:
        print('Student', i+1)
        #Usually objects and compare is lib[i][somenumber]
        rangejudger_ratio(lib[i][2],lib[i][0],0.05,24.31)
        rangejudger_ratio(lib[i][3],lib[i][1],0.05,40.31)
        #Below are two examples of double jeopardy
        rangejudger_ratio(lib[i][4],lib[i][5],0.05,2)
        rangejudger_ratio(lib[i][5],lib[i][6],0.05,3)
    #Transforming blank grading to rubrics in gradescope
    for i in range(len(lib)):
'''        
'''
        Result for student 3:
            Student 3
    3
    3
    3
    1
    Though student 3 made the 3rd answer incorrect, the fourth answer is graded correctly according to his/her own 3rd answer
'''
    
