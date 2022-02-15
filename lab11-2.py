# Author: CCG 2/15/22

my_file = open("alma_mater.txt", "r") 

while True:
      lines = my_file.readlines() 
      for lines in reversed(lines):  
            print(lines) 
