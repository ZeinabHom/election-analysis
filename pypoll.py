#import scv & os module 

import csv
import os

#Generate file path
file_to_load= os.path.join ('Resources','election_results.csv')
file_to_save = os.path.join("analysis", "election_analysis.txt")
#define total_votes as a variable with 0 value
total_votes = 0
candidate_name = []
candidate_votes = {}
county_name = []
county_votes ={}

#open file into variable
with open(file_to_load,newline='') as election_data:
    #convert election_data to CSV  format
    file_reader = csv.reader(election_data)
    #retrieve header of CSV file and put it in header variable
    headers = (next(file_reader))
   
    #iterate each row of CSV file
    for row in file_reader:
                #make county list
        if row[1] not in county_name:
            county_name.append(row[1])
            county_votes [row[1]]=0
        county_votes[row[1]] += 1

         # count the votes
        total_votes += 1
         # make a candicates list
        if row[2] not in candidate_name:
              candidate_name.append(row[2])         
              candidate_votes[row[2]]=0
        candidate_votes[row[2]] += 1
    #find winner with max votes from candidate_votes dictionary
    winner_name = max(candidate_votes, key=candidate_votes.get)
    #find max vote from candidate_votes dictionary
    winner_vote= max(candidate_votes.values())
                 
    #  find county winner with max votes from county_vote dictionary
    county_winner = max(county_name, key=county_votes.get)
    print(county_winner)
 

 # open a text file with write mode
with open(file_to_save, "w") as txt_file:
     #write results in  text file   
    txt_file.write("Election Results\n")
    txt_file.write("----------------------------\n")
    txt_file.write("Total Votes  " +str(total_votes)+ "\n")
    txt_file.write("----------------------------\n")
    txt_file.write(f" county votes :\n")
    
    for y in county_votes:
        county_percentage = county_votes[y] /total_votes *100
        txt_file.write(f"{y}: {county_percentage:.1f}% ({county_votes[y]})\n")

    txt_file.write("----------------------------\n")
    txt_file.write(f"Largest Country turnount :  {county_winner}\n")
    txt_file.write("----------------------------\n")

    # make empty list for percentages
    max_percentage= []
    #calculate vote percentage of each candidate
    for x in candidate_votes:
       vote_percentage = candidate_votes[x] / total_votes *100
    # find max vote percentage
       max_percentage.append(vote_percentage)

    # write results in  text file 
    # txt_file.write(f" {x}: {vote_percentage:.1f}% ({candidate_votes[x]})\n")
    txt_file.write(f" winner: {winner_name}\n")
    txt_file.write(f" Winning Vote Count: {winner_vote}\n")
    txt_file.write(f" Winning Percentage: {max(max_percentage):.1f}%\n")
    txt_file.write("----------------------------\n")

   