"""
Created on Sun Jan 16 00:23:01 2022

@author: Zifan Ma
"""
#Searching for student value and name on gradescope grade page, returning them as values and names by lib()

#You have to change response, and maybe cookie for different experiments

#I did not write any specific routine for txts, so it will be in the same folder as this py code

#You have to change path of txts, if you don't, it will overwrite previous txts in the folder
def library():
    import requests
    import re
    submis_url = []
    submis_url_temp = []
    #Use Your Cookie!
    #Use designated URL, URL in response is the same
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
        'Cookie': 'YOUR COOKIE',
    }
    session = requests.Session()
    response = session.get('https://www.gradescope.com/courses/YOUR NUMBER!!!/assignments/YOUR NUMBER!!!/grade', headers=headers)
    
    #Temp txt for F12 of grade url, must be created
    f12_text = open(r"YOUR FILE PATH/f12_text.txt", "w")
    f12_text.write(response.text)
    f12_text.close()
    f12_text = open(r"YOUR FILE PATH/f12_text.txt", errors = 'ignore')
    #Save all submission pages like https://www.gradescope.com/courses/354517/questions/13890418/submissions in submis_url
    for links in f12_text:        
        submis_url_temp.append(re.findall('/courses/[0-9]+/questions/[0-9]+/submissions', links))
    submis_url_temp = submis_url_temp[-1]
    for i in submis_url_temp:
        submis_url.append('https://www.gradescope.com'+i)
    
    #Getting Student Name and value input from gradescope
    txt_name = 'YOUR FILE PATH/f12_text_'
    sorting_number = 0
    values_temp = []
    names_temp = []
    
    #Iterate and using regular expression to obtain values and names, stripping useless parts (Empty lists and '/grade">')
    for i in range(len(submis_url)):
    #可以考虑下面strip优化一下成map(str.strip)不跑循环
        session2 = requests.Session()
        response2 = session2.get(submis_url[i], headers=headers)
        str_i = str(i)
        f12_text_1 = open(txt_name+str_i+".txt", "w")
        f12_text_1.write(response2.text)
        f12_text_1.close()
        f12_text_1 = open(txt_name+str_i+".txt", errors = 'ignore')
        
        for info in f12_text_1:
            sorting_number = sorting_number + 1
            #sorting_number = re.findall('td>[0-9]+</td', info) #To be honest, sorting number is not found in F12. Considering the fact the sequence in value should be never wrong, we use value here
            values_temp1 = re.findall('/grade">.{0,20}</a></td></', info)
            names_temp1 = re.findall('/grade">.{0,50}</a></td><t', info)
            if bool(values_temp1):
                values_temp.append(values_temp1)
            if bool(names_temp1):
                names_temp.append(names_temp1)
    #/grade">[value]</a></td></tr><tr><td>[sorting_number]</td><td class="tab #value and sorting_number
    #/grade">(needs labeling)</a> #Name
    #Stripping and merging all values in lists   
        values_2 = []
        names_2 = []
        for values_for_each_question in values_temp:
            for values_single in values_for_each_question:
                values_2.append(values_single.strip('/grade">').strip('</a></td></'))
        for names_for_each_question in names_temp:
            for names_single in names_for_each_question:
                names_2.append(names_single.strip('/grade">').strip('</a></td><t'))
        i = i + 1
    def split_list(a_list):
        return [a_list[i:i+len(values_for_each_question)] for i in range(0,len(values_2),len(values_for_each_question))]
    values = split_list(values_2)
    names = split_list(names_2)
    return values,names
