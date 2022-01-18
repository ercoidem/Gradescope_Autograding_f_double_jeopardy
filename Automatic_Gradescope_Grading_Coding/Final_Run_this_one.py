# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 15:58:29 2022

@author: Zifan Ma
"""

import pyautogui as pa
import Main_for_Grading
import time

rubrics = Main_for_Grading.main_for_grading()[1]

import requests
import re
urls = []
submis_url_temp = []
#Use Your Cookie!
#Use designated URL, URL in response is the same
URL_OF_FIRST_QUESTION_SUBMISSION_PAGE = 'https://www.gradescope.com/courses/YOUR NUMBER!!!/questions/YOUR NUMBER!!!/submissions'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
    'Cookie': 'YOUR COOKIE',
}
session = requests.Session()
response = session.get(URL_OF_FIRST_QUESTION_SUBMISSION_PAGE, headers=headers)

#Temp txt for F12 of grade url, must be created
f12_text = open(r"YOUR FILE PATH/f12_text_rubrics", "w")
f12_text.write(response.text)
f12_text.close()
f12_text = open(r"YOUR FILE PATH/f12_text_rubrics", errors = 'ignore')
#Save all submission pages like https://www.gradescope.com/courses/YOUR NUMBER!!!/questions/YOUR NUMBER!!!/submissions in submis_url
for links in f12_text:        
    submis_url_temp.append(re.findall('/courses/[0-9]+/questions/[0-9]+/submissions/[0-9]+/grade', links))
submis_url_temp = submis_url_temp[-1]
for i in submis_url_temp:
    urls.append('https://www.gradescope.com'+i)
#%%
#最后写一下输入不同学生网页的代码
count = 0

for rubric in rubrics:
    time.sleep(2)
    pa.click(202,50)
    pa.typewrite(urls[count], interval = 0.05)
    time.sleep(1)
    pa.hotkey('enter')
    time.sleep(3)
    pa.click(202,150)
    count = count + 1
    for i in rubric:
        pa.typewrite(i)
        time.sleep(0.5)


