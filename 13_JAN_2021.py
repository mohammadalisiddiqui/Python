import pandas as pd
import numpy as np
from numpy import random

# dataset_1 = {'car':['BMW',"Toyota","FORD","Suzuki"],'win':[2,1,3,4]}

# print(type(dataset_1))

# report_1 = pd.DataFrame(dataset_1)

# print(report_1)

# subjects = {'subjects':['Physics','Maths','Chemistry'],'Obtained Marks':[52,66,50]}

# report_sub = pd.DataFrame(subjects)

# print(report_sub)

# a = [1,5,22,33,4]

# report_a = pd.Series(a)
# print(report_a)   #also use report_a[2] to print index value of  2

# report_a = pd.Series(a,index=["Maths","Phy","Chem","urdu","bio"])
# print(report_a)


# calories = {'day1':40 ,'day2':100 , 'day3':15}

# report_calo = pd.Series(calories)

# print(report_calo)

# dataset_1 = {'car':['BMW',"Toyota","FORD","Suzuki"],'win':[2,1,3,4]}

# print(type(dataset_1))

# report_1 = pd.DataFrame(dataset_1)

# print(report_1)
# print(report_1.loc[1])   

# change_index = pd.DataFrame(dataset_1, index=["Car1","Car2","Car3","Car4"])  #to change index number
# print(change_index)
# print(change_index.loc["Car4"])  


# make 10 student data and 4 marks

student_data = {
    'Student_Name':['Tanzeel','Ahad','Adil','Anus','Abdullah','Hashim','Faiz','Faraz','Umair','Erdum'],
    'Physics':[36,56,99,87,74,58,60,35,64,87],
    'Maths':[26,76,49,67,74,28,30,35,47,82],
    'Chemistry':[36,56,99,87,74,58,60,35,64,87],
    'Pak Studies':[36,56,99,87,74,58,60,35,64,87],
}

report_student = pd.DataFrame(student_data)

# print(report_student)
print(report_student.head(2))
print(report_student.tail(2))
print(report_student.info())


# d = pd.read_csv("student_data.csv")
# # print(d)
# # print(d.to_string)
# print(d.head())
# print(d.tail())
# print(d.info())