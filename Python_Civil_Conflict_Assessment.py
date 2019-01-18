import json
import csv 

#Open the DR Congo civil conflict file and name it DRC
with open("Conflict_DRC_New.json") as file:
    DRC = json.load(file)
#print(DRC) 

#Write the csv file
with open("DRC_Conflict.csv", 'w',newline = '') as file:
    filewriter = csv.writer(file)
    #Write the header
    filewriter.writerow(["year", "type_of_violence"]) 
    
    # Print year and type_of_violence for each required conflict
    # ... to make sure you can access them. Then put in list, and write to row.
    for conflict in DRC:
        #print(f'year: {conflict["year"]}, type of violence: {conflict["type_of_violence"]}')
        #Previous print command works so use that format to write each row
        filewriter.writerow([conflict["year"],conflict["type_of_violence"]])

       


    


