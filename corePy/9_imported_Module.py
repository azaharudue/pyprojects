import time 
import os
import pandas
'''pandas Module to manipulate data '''
while True: 
    if os.path.exists("basics/files/temps_today.csv"):
        with open("basics/files/temps_today.csv") as file:
                data0=pandas.read_csv(file)
                print(data0)
                time.sleep(10)
    else:   
        print("File doesnot exist!")
#Using pandas
    if os.path.exists("basics/files/file.csv"):
        data = pandas.read_csv("basics/files/file.csv")
        print(data)
    else:   
        print("File doesnot exist!")
        
        
