import os 
import re

# problme statement 
# user need to remove extension of dot html from all the files and save them without extension 

list = os.listdir("FULL PATH WHERE,HTML FILE EXIST")

for filename in list:
    if ".html" in filename:
        #replace
        new_name = re.sub('\.html$', '', filename)  
        os.rename(filename,new_name)        
        
        
    else:
        # do not replace 
        print("No Need")