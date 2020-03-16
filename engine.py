#engine file for testing.
import colorama
from colorama import init, Fore, Style
from os import system, name, path, getcwd, listdir
import time

ART = Fore.BLUE+"""
	******************************
	**************/\**************
	*************/--\*************
	************/-03-\************
	***********/--MB--\***********
	***********\--JD--/***********
	************\-20-/************
	*************\--/*************
	**************\/**************
	******************************
"""+Style.RESET_ALL

QUESTION_ART = Fore.GREEN+"""
                               888   d8b                 
                                888   Y8P                 
                                888                       
 .d88888888  888 .d88b. .d8888b 888888888 .d88b. 88888b.  
d88" 888888  888d8P  Y8b88K     888   888d88""88b888 "88b 
888  888888  88888888888"Y8888b.888   888888  888888  888 
Y88b 888Y88b 888Y8b.         X88Y88b. 888Y88..88P888  888 
 "Y88888 "Y88888 "Y8888  88888P' "Y888888 "Y88P" 888  888 
     888                                                  
     888                                                  
     888                                                 
"""+Style.RESET_ALL

EXIT_ART = Fore.YELLOW+"""
   _____  ____   ____  _____  ______     ________ 
  / ____|/ __ \ / __ \|  __ \|  _ \ \   / /  ____|
 | |  __| |  | | |  | | |  | | |_) \ \_/ /| |__   
 | | |_ | |  | | |  | | |  | |  _ < \   / |  __|  
 | |__| | |__| | |__| | |__| | |_) | | |  | |____ 
  \_____|\____/ \____/|_____/|____/  |_|  |______|  
"""+Style.RESET_ALL

FAIL = Fore.RED +"""
_________ _        _______  _______  _______  _______  _______  _______ _________
\__   __/( (    /|(  ____ \(  ___  )(  ____ )(  ____ )(  ____ \(  ____ \\__   __/
   ) (   |  \  ( || (    \/| (   ) || (    )|| (    )|| (    \/| (    \/   ) (   
   | |   |   \ | || |      | |   | || (____)|| (____)|| (__    | |         | |   
   | |   | (\ \) || |      | |   | ||     __)|     __)|  __)   | |         | |   
   | |   | | \   || |      | |   | || (\ (   | (\ (   | (      | |         | |   
___) (___| )  \  || (____/\| (___) || ) \ \__| ) \ \__| (____/\| (____/\   | |   
\_______/|/    )_)(_______/(_______)|/   \__/|/   \__/(_______/(_______/   )_(   
                                                                                 
"""+Style.RESET_ALL

SUCCESS = Fore.GREEN+"""
 ____   U  ___ u   ____      ____    U _____ u   ____   _____   
U /"___|   \/"_ \/U |  _"\ uU |  _"\ u \| ___"|/U /"___| |_ " _|  
\| | u     | | | | \| |_) |/ \| |_) |/  |  _|"  \| | u     | |    
 | |/__.-,_| |_| |  |  _ <    |  _ <    | |___   | |/__   /| |\   
  \____|\_)-\___/   |_| \_\   |_| \_\   |_____|   \____| u |_|U   
 _// \\      \\     //   \\_  //   \\_  <<   >>  _// \\  _// \\_  
(__)(__)    (__)   (__)  (__)(__)  (__)(__) (__)(__)(__)(__) (__) 
"""+Style.RESET_ALL

INVALID = Fore.RED +"	INVALID CHOICE"+Style.RESET_ALL

NOTESTS = """
	There are no test files in this directory.
	This program must be run from the same directory 
	as your .jdq and .jda files.  Please locate them 
	or use the quizmaker to make a set.  There must be 
	both a jdq and jda file for each quiz.
"""

MENU = """
	Welcome to the testing engine.
	Make a choice below to proceed.

	1. Choose quiz
	2. Run the entire quiz
	3. Choose a single question
	4. Show a question/answer
	5. Show all questions
	6. Show all answers
	7. Exit the engine
"""

QUESTION = []
ANSWER = []
SCORE = []
current_test = ""
current_question = 1
question_choice = "change"
answer_choice = "change"
def check_sys():
	if name == 'nt':
		init(convert=True)
   # for mac and linux(here, os.name is 'posix')
	else:
		pass

def clear():
	if name == 'nt':
		system('cls')
   # for mac and linux(here, os.name is 'posix')
	else:
		system('clear')

	def hold():
		goon = input("Press enter to continue: ")
	
def question_filler():
	with open(current_test+'.jdq','r') as questionfile:
		for line in questionfile:
			QUESTION.append(line.rstrip("\n"))


def answer_filler():
	with open(current_test+'.jda','r') as answerfile:
		for line in answerfile:
			ANSWER.append(line.rstrip("\n"))
		
def set_question(qin):
	if qin == -1:
		choice = input("Choose a question number 1 through %d: " %len(QUESTION))
	else:
		choice = qin
	try:
		num_choice = int(choice)-1
		#print(num_choice)
		#time.sleep(5)
		qtext = QUESTION[num_choice]
		atext = ANSWER[num_choice]
		current_question = num_choice
		#print(current_question)
		return(qtext,atext)
	except:
		pass
	
def ask_question(set):
	clear()
	answer = input(QUESTION_ART+set[0]+": ")
	if answer.lower() == set[1]:
		return 1
		#print(SUCCESS)
		#set_score()
	else:
		return -1
		#print(FAIL)
		#set_fail()
	
def show_pair(set):
	clear()
	print(set[0]+": "+set[1])
	
def show_all_sets():
	clear()
	count = 0
	for i in QUESTION:
		print(i+": "+ANSWER[count])
		count +=1

def show_all_q():
	clear()
	for i in QUESTION:
		print(i)
		
def instructions():
	clear()
	if name == 'nt':
		text = """
		Instructions can be found in the readme file
		"""
   # for mac and linux(here, os.name is 'posix')
	else:
		text = """
	Instructions can be found in the readme file
	you may want to look into the screen command
	which will allow you to run this test and 
	other programs at the same time.
		"""
	print(text)

def question():
	choice=int(input("Which Question: "))
	print(question_filler(choice))
	
def continuous():
	global current_question
	continuing = True
	while continuing:
		pf = ask_question(set_question(current_question))
		if pf == 1:
			print(SUCCESS)
			current_question+=1
		elif pf == -1:
			print(FAIL)
		goon = input("Continue?(Y/N): ")
		if goon.lower() != "y":
			continuing = False
		else:
			pass
			
def list_files(directory, extension):
    return (f for f in listdir(directory) if f.endswith('.' + extension))
			
def choose_test():
	clear()
	global current_test
	cwd = getcwd()
	files = list_files(cwd, "jdq")
	fileList = []
	for i in files:
		fileList.append(i)
		
	if len(fileList)>0:
		choosing = True
		while choosing:
			print(ART)
			print("""
	Make a choice from the following files. 
	Enter the name of the test you would like to take.
	Enter q to exit the engine.
			""")
			print("	Choices:")
			for i in fileList:
				print("	"+i.rstrip("\.jdq"))
			
			current_test = input("Choice: ")
			if current_test == "q":
				print(EXIT_ART)
				exit()
			else:
				try:
					question_filler()
					answer_filler()
					choosing = False
				except:
					clear()
					print("""
	That test file does not exist. 
	Please choose a name from the list.
					""")
	else:
		print(NOTESTS)
		
def menu_switch(argument):
	
	try:
		argument = int(argument)
	except:
		pass
	if argument == 1:
		choose_test()
	elif argument == 2:
		continuous()
	elif argument == 3:
		pf = ask_question(set_question(-1))
		if pf == 1:
			print(SUCCESS)
		elif pf == -1:
			print(FAIL)
	elif argument == 4:
		show_pair(set_question(-1))
		hold()
	elif argument == 5:
		show_all_q()
		hold()
	elif argument == 6:
		show_all_sets()
		hold()
	elif argument == 7:
		clear()
		print(EXIT_ART)
		exit()
	else:
		print(INVALID)

if __name__ =="__main__":
	check_sys()
	print(ART)
	print("""
	Welcome to the testing engine. 
	You must choose which test you would like to take.
	Press enter to continue.
	""")
	dummy = input("")
	choose_test()
	running = True
	while running:
		print(MENU)
		Choice = input("Choice: ")
		menu_switch(Choice)
