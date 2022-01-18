# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 16:13:24 2022

@author: Zifan Ma
"""



import win32com.client
import os
import glob

o = win32com.client.Dispatch("Excel.Application")
o.Visible = False
input_dir = r"C:\Users\Zifan Ma\OneDrive - Washington University in St. Louis\2021- WashU\TA Automatic Grade Project\xls"  #Set Input path every time 
output_dir = r"C:\Users\Zifan Ma\OneDrive - Washington University in St. Louis\2021- WashU\TA Automatic Grade Project\xlsx"  #Set Output path every time
files = glob.glob(input_dir + "/*.xls")

for filename in files:
    file = os.path.basename(filename)
    output = output_dir + '/' + file.replace('.xls','.xlsx')
    wb = o.Workbooks.Open(filename)
    wb.ActiveSheet.SaveAs(output,51)
    wb.Close(True)