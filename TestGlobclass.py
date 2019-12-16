import glob
from os import listdir
from os.path import isfile, join

mypath = 'D:/Initial Training/Software coding/Software Testing/Robot/robotframework_workshop'

list_pics = [p for p in listdir(mypath) if isfile(join(mypath, p))]
#print(list_pics)
"""for i in list_pics :
    print(i, end=' ')
"""
matching = [s for s in list_pics if "selenium-screenshot" in s]
"""for i in matching : 
    print(i)
"""
print(len(matching))
pic_number = str(len(matching))
pic_path = mypath +"/selenium-screenshot-"+pic_number+".png"
print(pic_path)