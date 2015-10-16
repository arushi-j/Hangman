import random

#List to store the Words and dictionary for hints as values
movie_list = ["the martian", "gravity", "interstellar", "trainwreck", "steve jobs", "inside out", "minions"]
movie_hint = {"the martian" : "Stuck on Mars", "gravity" : "Stars Sandra Bullock", "interstellar" : "Nolan Space Throry", "trainwreck" : "Amy Schumer", "steve jobs" : "mac", "inside out" : "what happens in our head?", "minions" : "cute yellow creatures"}
animal_list = ["tiger", "monkey", "zebra", "unicorn", "donkey"]
animal_hint = {"tiger" : "yellow", "monkey" : "imitators", "zebra" : "crossing", "unicorn" : "magic", "donkey" : "stupid"}
tv_list = ["breaking bad", "sherlock", "criminal minds", "narcos", "daredevil"]
tv_hint = {"breaking bad" : "meth", "sherlock" : "mystery", "criminal minds" : "serial killers", "narcos" : "new drug show", "daredevil" : "blind"}
geek_list = ["darth vader", "coding", "gadgets", "gandalf", "heisenberg"]
geek_hint = {"darth vader" : "star trek" , "coding" : "we love it", "gadgets" : "tech stuff" , "gandalf" : "Sauron's enemy", "heisenberg" : "quantum mechanics"}

#Asks User to enter a category choice
user_input = raw_input("Enter your choice 1 - Movies, 2 - Animals, 3 - TV series, 4 - Geek Stuff : ")

if (user_input == "1"):
	hangman_words = random.choice(movie_list) #Randomly selecting the movie
	hangman_index = movie_list.index(hangman_words) #Finding the index of the movie selected
	hint = movie_hint[hangman_words]

elif (user_input == "2"):
 	hangman_words = random.choice(animal_list)
 	hangman_index = animal_list.index(hangman_words)
 	hint = animal_hint[hangman_words]

elif (user_input == "3"):
 	hangman_words = random.choice(tv_list)
 	hangman_index = tv_list.index(hangman_words)
 	hint = tv_hint[hangman_words]

elif (user_input == "4"):
 	hangman_words = random.choice(geek_list)
 	hangman_index = geek_list.index(hangman_words)
 	hint = geek_hint[hangman_words]

else:
	print "Invalid Input"

#Stages of hangman in ASCII art	
hangman_stage = ['''

   +---+
       |
       |
       |
       |
       |
 =========''','''
   +---+
   |   |
       |
       |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
       |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
   |   |
       |
       |
 =========''', '''
 
   +---+
   |   |
   O   |
  /|   |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|\  |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
 ========='''] 	

hangman_list= list(hangman_words) #Converting the string into a list
blank_list = list(hangman_words) #for blanks
gameIsDone = False

print "H A N G M A N"
print "Hint : " , hint

incorrect_guessed_letters = []
incorrect_guess = 0
correct_guessed_letters = []
correct_guess=0
blanks_check = len(hangman_words) #for number of characters
c=0 #counter

#Assigns '/' to spaces and '_' to strings and stores in blank_list
for i in range (len(blank_list)):
	if (blank_list[i] == ' '):
		c +=1 #counts the number of spaces
		blank_list[i] = ' / '
	else:
		blank_list[i] = '_'
	
print ' '.join(blank_list) #Prints the hangman word in secret
blanks_check = blanks_check - c #Number of character in word excluding the space
print "Number of Characters ", blanks_check

while (gameIsDone != True): #runs till the game is complete
	letter = raw_input("Enter a letter : ") #Makes the user input a letter
	letter = letter.lower() #converts the letter to lower case

	if (len(letter) != 1): #checks the user enters a single letter
		print ("Enter a single letter ")
	elif (letter in correct_guessed_letters): #ensures that the user doesnt enter the same letter twice
		print ("You have already guessed that. Choose again. ")
	elif (letter not in 'abcdefghijklmnopqrstuvwxyz'): #ensures that the user enters only a letter	
		print ("Please enter a letter. ")

	if (letter not in hangman_words):
		incorrect_guessed_letters.append(letter) #adds incorrect guesses to list
		incorrect_guess += 1

		print hangman_stage[incorrect_guess] #displays hangman ASCII art according to stage
		print "Oh no!, Wrong guess! "
		print "Incorrect Guesses : ", ','.join(incorrect_guessed_letters)

		if (len(incorrect_guessed_letters) == len(hangman_stage)-1): #checks wrong guesses
			print "You have run out of guesses! You lose."
			print "The secret word was : ", hangman_words
			gameIsDone = True #breaks out of while loop. Ends the game
		else:
			gameIsDone = False #goes down the while loop

	elif (letter in hangman_words):
		correct_guessed_letters.append(letter) #adds correct guesses to list
		#Checks for user input in the word
		for i in range (len(hangman_list)):
			if (letter == hangman_list[i]):
				blank_list[i] = letter #replaces the blank with the correct guessed letter
				print ' '.join(blank_list) #prints progress
				if blank_list.count('_') == 0: #checks whether the user has guessed all the letters
					print ("You win!")
					print "The secret word is ", hangman_words
					gameIsDone = True
					quit() #leaves the loop. finishs game
				else:
					gameIsDone = False

	else:
		gameIsDone = False				
		
		
		

		

		