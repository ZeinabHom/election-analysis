#import scv & os module 
import csv
import os
#Generate file path
file_to_load= os.path.join ('Resources','election_results.csv')
file_to_save = os.path.join("analysis", "election_analysis.txt")

#open file into variable
with open(file_to_load,newline='') as election_data:
    #convert election_data to CSV  format
    file_reader = csv.reader(election_data)
    #retrieve header of CSV file and put it in header variable
    headers = (next(file_reader))
    
    
    # for row in file_reader:
    #     print(row[0])
    # print(election_data)

# with open(file_to_save, "w") as txt_file:
    
#     txt_file.write("Counties in the Election\n")
#     txt_file.write("----------------------------\n")
#     txt_file.write("Arapahoe\n")
#     txt_file.write("Denver\n")
#     txt_file.write("Jefferson")

