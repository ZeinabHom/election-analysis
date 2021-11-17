#import scv & os module 
import csv
import os
from typing import Counter
#Generate file path
file_to_load= os.path.join ('Resources','election_results.csv')
file_to_save = os.path.join("analysis", "election_analysis.txt")
#define total_votes as a variable with 0 value
total_votes = 0
candidate_name = []

#open file into variable
with open(file_to_load,newline='') as election_data:
    #convert election_data to CSV  format
    file_reader = csv.reader(election_data)
    #retrieve header of CSV file and put it in header variable
    headers = (next(file_reader))
    
    #iterate each row of CSV file
    for row in file_reader:
        # count the votes
        total_votes += 1
        row[2] = row[2]
    
    
    
   
# open a text file with write mode
with open(file_to_save, "w") as txt_file:
  # write results in  text file   
    txt_file.write("Election Results\n")
    txt_file.write("----------------------------\n")
    txt_file.write("Total Votes  " +str(total_votes)+ "\n")
    txt_file.write("----------------------------\n")
 

