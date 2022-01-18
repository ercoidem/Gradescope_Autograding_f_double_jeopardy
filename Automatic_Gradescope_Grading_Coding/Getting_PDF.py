# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 19:34:23 2022

@author: Zifan Ma
"""
#Start when you are at the first student's grade page
#Suppose you have only one tab, which is gradescope page
import pyautogui as pa
import time
time.sleep(3)
for i in range(20):
    pa.moveTo(169,1293)
    time.sleep(1)
    pa.click(169,1293)
    time.sleep(1)
    pa.moveTo(283,1081)
    time.sleep(1)
    pa.click(283,1081)
    time.sleep(5)
    pa.moveTo(2446,100)
    time.sleep(3)
    pa.click(2446,100)
    time.sleep(1)
    pa.hotkey('enter')
    time.sleep(1)
    pa.moveTo(470,19)
    time.sleep(1)
    pa.click(470,19)
    time.sleep(1)
    pa.click(2542,1372)
    time.sleep(0.3)
    pa.click(2295,1361)
    time.sleep(3)
    