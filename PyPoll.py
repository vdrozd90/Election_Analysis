# the data we need to retrieve
# Assign a variable for the file to load and the path
file_to_load = 'Resources/election_results.csv'
# Open the election results and read the file
with open(file_to_load) as election_data:
    print(election_data)

# create a filename varioable to the file
import os
file_to_save = os.path.join("analysis", "election_analysis.txt")
# open the file as a text file
with open(file_to_save, "w") as txt_file:
#write 3 countries to the file
    txt_file.write("Arapahoe\nDenver\nJefferson")

# import election data
import csv
import os
# assign variables to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")
# assign a variable to save the file to a pth
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter
total_votes = 0

# Candidate Options
candidate_options = []
# Declare the empty dictionary
candidate_votes = {}

# Track the winning candidate, vote count, percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# open the election results and read the file
with open(file_to_load) as election_data:
    # to do: read and analyze the data here
    # Read the file object with the reader function
    file_reader = csv.reader(election_data)
    # Read the header row
    headers = next(file_reader)
    # Print each rose in  the CSV file
    for row in file_reader:
        #2. Add to the total vote count
        total_votes += 1

        # Print the candidate name from each row
        candidate_name = row[2]

        # if the candidate does not match any existing candidates
        if candidate_name not in candidate_options:

            # add the candidate name to the candidate list
            candidate_options.append(candidate_name)
            
            #Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

# Save results to txt file
with open(file_to_save, "w") as txt_file:
    # print the final vote count
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"--------------------------\n")
    print(election_results, end="")
    # save the final vote count
    txt_file.write(election_results)

    # Percentage of votes for each candidate
    for candidate_name in candidate_votes:
        # Retrive vote count of a candidate
        votes = candidate_votes[candidate_name]
        # calculate percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        # print the candidate name and percentage of votes
        candidate_results = (
            f"{candidate_name}: received {vote_percentage:.1f}% ({votes:,})\n")

        #print candidates voter count and percentage
        print(candidate_results)
        # save results to txt file
        txt_file.write(candidate_results)
        # determine winning vote count, winning percentage and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
    # print the winning candidate results
    winning_candidate_summary = (
        f"---------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"----------------------------\n")
    print(winning_candidate_summary)
    # save the winning candidates results to txt file
    txt_file.write(winning_candidate_summary)


 
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. the winner of the election based on popular vote