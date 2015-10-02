#Collaborated with Sam and Danny
# File Header
#
# Kollin Schalhamer
# CIS- 125

# Define a function called piggy(string) that returns a string

def piggy(word):

    for letter in word:
	# Check if letter is a vowel
        vowels = "aeiou"
        if letter in vowels:
		# True?  We are done
            pig = word + "yay"
    else:
		# False? Consonant
        pig = word[1:] + word[0] + "ay"
	
    
	# Magic Happens Here
	# Ignore previous line
	
    return pig

# Open the file *getty.txt* for reading.  

infile = open("getty.txt", "r")

# Open a new file *piggy.txt* for writing.

outfile = open("piggy.txt", "w")

# Read the getty.txt file into a string. 

gettystring = infile.read()

# Strip out bad characters (, - .).  

gettystring = gettystring.replace("-", "")
gettystring = gettystring.replace(".", "")
gettystring = gettystring.replace(",", "")

# Split the string into a list of words.  

gettylist = gettystring.split()

# Create a new empty string.  

pigified = ""

# Loop through the list of words, pigifying each one.  

for word in gettylist:
	pigified = pigified + piggy(word) + " "

# Add the pigified word (and a space) to the new string.  



# Write the new string to piggy.txt.  
outfile.write(pigified)

# close the files.
infile.close()
outfile.close()