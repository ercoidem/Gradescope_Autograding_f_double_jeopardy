#DP Number Judgers
def DP(x,y): #x is object, y is compare
    x = x.lower().lstrip('-')
    if ('e' in x):
        # return the length of the numbers before the 'e'
        myStr = x.split('e')
        if '.' in x:
            '''PB Here'''
            dp = len(myStr[0].split('.')[1]) # to compenstate for the decimal point
        if '.' not in x:
            dp = 0 # Not to compenstate for the decimal point
    if not('e' in x):
        if '.' in x:
            myStr = x.split('.')
            dp = len(myStr[1])
        if not '.' in x:
            dp = 0
    if  dp == y:
        return True
    if dp!=y:
        return False
#Helps SF judger run
def SF_former(x): #x is object, y is compare
    # change all the 'E' to 'e'
    x = x.lower().lstrip('-')
    if ('e' in x):
        # return the length of the numbers before the 'e'
        myStr = x.split('e')
        if '.' in x:
            if not (1 <= float(myStr[0]) < 10) :
                return 999
                #return ('Zifan Error Notification: Error Type1: Something like 0.5E-5 or -19.3E9')
            else:
                a = len(myStr[0]) - 1
                return a # to compenstate for the decimal point
        if '.' not in x:
            if not (1 <= float(myStr[0]) < 10) :
                return 999
                #return ('Zifan Error Notification: Error Type2: Something like -31E7')
            else:
                a = len(myStr[0])
                return a # Not to compenstate for the decimal point
            
#Significance Number Judger
#Input must be string, otherwise python will automatically change 1.230 to 1.23, thus losing the 0
            
def SF(x,y): #x is object, y is compare
    '''Returns the number of significant digits in a number. This takes into account
       strings formatted in 1.23e+3 format and even strings such as 123.450'''
    # change all the 'E' to 'e'

    x = x.lower().lstrip('-')

    if ('e' in x):
        # return the length of the numbers before the 'e'
        myStr = x.split('e')
        if '.' in x:
            if not (1 <= float(myStr[0]) < 10) :
                sf = 999
                #return ('Zifan Error Notification: Error Type1: Something like 0.5E-5 or -19.3E9')
            else:
                sf = len(myStr[0]) - 1
                #return sf # to compenstate for the decimal point
        if '.' not in x:
            if not (1 <= float(myStr[0]) < 10) :
                sf = 999
                #return ('Zifan Error Notification: Error Type2: Something like -31E7')
            else:
                sf = len(myStr[0])
                #return sf # Not to compenstate for the decimal point
        if sf == y:
            return True
        if sf!=y:
            return False
    
    else:
        # put it in e format and return the result of that
        ### NOTE: because of the 8 below, it may do crazy things when it parses 9 sigfigs
        n = ('%.*e' %(8, float(x))).split('e')
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
        sf = SF_former('e'.join(n))
        if sf == y:
            return True
        if sf!=y:
            return False


   

def ran_rat(objects, compare, ratio, a): #range_ratio
#Custom rangejudger whenever needed
    if float(compare)*(1-ratio) <= float(objects)*a <= float(compare)*(1+ratio):
        return True #We may append it to operations related to auto grading in the future
    if not (float(compare)*(1-ratio) <= float(objects)*a <= float(compare)*(1+ratio)):
        return False

def ran_dir(objects, compare, delta1): #range_direct
#Custom rangejudger whenever needed
    if float(compare)-delta1 <= float(float(objects)) <= float(compare)+delta1:
        return True #We may append it to operations related to auto grading in the future
    if not (float(compare)-delta1 <= float(float(objects)) <= float(compare)+delta1):
        return False   

def absv(objects, compare): #absolute_value_judger
    if float(compare) == float(objects):
        return True #We may append it to operations related to auto grading in the future
    if float(compare) != float(objects):
        return False
         
