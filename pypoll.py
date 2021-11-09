#the data we need to retrieve 
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes 
# 3. the percentage of votes each candidate won
# 4. The winner of election base on popular vote

# Import the datetime class from the datetime module. Import Module as dt to help with confusing text 
#from datetime import datetime # this is a specific function import - Or you can import whole modules like import datetime as dt 
# Use the now() attribute on the datetime class to get the present time.
#now = datetime.now()
# Print the present time.
#print("The time right now is ", now)


# Assign a variable for the file to load and the path.
# file_to_load = 'Resources/election_results.csv'

# # Open the election results and read the file
# with open(file_to_load) as election_data:

#      # To do: perform analysis.
#      print(election_data)
     



# # Indirect path to file opening 
import csv
import os
# # Assign a variable for the file to load and the path.
# file_to_load = os.path.join("Resources", "election_results.csv")
# # Open the election results and read the file.
# with open(file_to_load) as election_data:

#     # Print the file object.
#      print(election_data)




# Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# # Using the with statement open the file as a text file.
# with open(file_to_save, "w") as txt_file:

#     # Write some data to the file.
#     txt_file.write("Counties in the Election\n")
#     txt_file.write("_" * 25)
#     txt_file.write("\nArapahoe\nDenver\nJefferson")


# Add our dependencies.
# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)

