# Election Result
In this project, election result was calculated based on candidate & county. Python was used to analyze data.The below steps was followed to find our result;
The original data file was excel so first of all we converted our excel file to csv format as well as the import statement was used to access to default modules of csv  and  os.

		 -  import  csv
		 - import  os
	- file_to_load=  os.path.join ('Resources','election_results.csv')
After that we made one txt file to display our final result.
		 - file_to_save  =  os.path.join("analysis", "election_analysis.txt")
We opened our data in csv format and used reader function to read our data with below code
	    - open(file_to_load,newline='') as  election_data: file_reader  =  csv.reader(election_data)
Below lists & dictionaries were defined
		 - candidate_name  as a list
		 - candidate_votes  = as a dictionary
		 - county_name  as a list
		 - county_votes  as a dictionary
Moreover, for loop and if function were used to calculate and prepare the lists and dictionaries as follows;
	    for  row  in  file_reader:
		    if  row[1] not  in  county_name:
			    county_name.append(row[1])
			    county_votes [row[1]]=0
	    	county_votes[row[1]] +=  1
		total_votes  +=  1
	
	 if row[2] not  in  candidate_name:
		 candidate_name.append(row[2])
		 candidate_votes[row[2]]=0
	 candidate_votes[row[2]] +=  1
	 
Max() syntax was used to calculate maximum votes of candidate and county
			winner_name  =  max(candidate_votes, key=candidate_votes.get)
			winner_vote=  max(candidate_votes.values())
			county_winner  =  max(county_name, key=county_votes.get)
			
Write() syntax was used to show our final result in txt file and the percentage of candidate and county votes was calculated by for loop.

    with  open(file_to_save, "w") as  txt_file:
		  txt_file.write("Election Results\n")
		  txt_file.write("----------------------------\n")
		  txt_file.write("Total Votes "  +str(total_votes)+  "\n")
		  txt_file.write("----------------------------\n")
		  txt_file.write(f" county votes :\n")
	
	   for  y  in  county_votes:
	county_percentage  =  county_votes[y] /total_votes  *100
	txt_file.write(f"{y}: {county_percentage:.1f}% ({county_votes[y]})\n")
    txt_file.write("----------------------------\n")
	txt_file.write(f"Largest Country turnount : {county_winner}\n")
	txt_file.write("----------------------------\n")
	
  max_percentage= []
		 for  x  in  candidate_votes:
			    vote_percentage  =  candidate_votes[x] /  total_votes  *100
			    max_percentage.append(vote_percentage)
      txt_file.write(f" {x}  {vote_percentage:.1f}% ({candidate_votes[x]})\n")
      txt_file.write("----------------------------\n")
      txt_file.write(f" winner: {winner_name}\n")
      txt_file.write(f" Winning Vote Count: {winner_vote}\n")
      txt_file.write(f" Winning Percentage: {max(max_percentage):.1f}%\n")
      txt_file.write("----------------------------\n")
