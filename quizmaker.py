from os import system, name, path, getcwd, listdir
from time import sleep
from colorama import Fore, Style, init
ART = """
**************
******/\******
*****/--\*****
****/-MM-\****
***/--MB--\***
***\--JD--/***
****\-YY-/****
*****\--/*****
******\/******
**************
"""

MENU = """
	Welcome to the quiz maker.
	Make a selection below to begin.

	1. Edit existing quiz
	2. Create new quiz
	3. Show instructions
	4. Write and exit
"""

INSTRUCTIONS = """
	This programs creates and edits the 
	companion files for the engine.py 
	program.  

	TO CREATE NEW:
	If you do not have current question
	and answer files in the current folder
	this option will create them.  If you
	do have question and answer files in 
	this folder it will delete them and 
	create new ones.  Only choose this to 
	create brand new tests.

	TO EDIT:
	This option will allow you to edit 
	existing question and answer files. 
	You will be prompted to enter a question 
	number to edit.  If your file is blank
	you will automatically start at question 
	one.
"""

INVALID = Fore.RED +"	INVALID CHOICE"+Style.RESET_ALL
EDITING = Fore.BLUE +"	Editing file "+Style.RESET_ALL
QUESTION = []
ANSWER = []
current_question = 0
current_test = ""
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

def list_files(directory, extension):
    return (f for f in listdir(directory) if f.endswith('.' + extension))
	
def question_filler():
	with open(current_test+'.jdq','r') as questionfile:
		for line in questionfile:
			QUESTION.append(line.rstrip("\n"))

def answer_filler():
	with open(current_test+'.jda','r') as answerfile:
		for line in answerfile:
			ANSWER.append(line.rstrip("\n"))

def show_all_q():
	clear()
	count = 1
	for i in QUESTION:
		print("Q"+str(count)+"	"+i)
		count +=1

def show_all_a():
	clear()
	count=1
	for i in ANSWER:
		print("A"+str(count)+"	"+i)
		count+=1

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

def show_pair(set):
	clear()
	first = Fore.GREEN+set[0]
	second = Fore.RED+" "+set[1]+Style.RESET_ALL
	print(first+second)
	#print(set[0]+": "+set[1])
	
def show_all_sets():
	clear()
	count = 0
	for i in QUESTION:
		first = Fore.GREEN+i
		second = Fore.RED+" "+ANSWER[count]+Style.RESET_ALL
		print("Q"+str(count+1)+"	"+first+second)
		count +=1
def push_qa():
		with open(current_test+'.jdq','w+') as questionfile:
			for i in QUESTION:
				questionfile.write(i+"\n")
		
		with open(current_test+'.jda','w+') as answerfile:
			for j in ANSWER:
				answerfile.write(j+"\n")
def add_set():
	clear()
	print(EDITING+current_test)
	print("	Adding question %s to file " %str(len(QUESTION)+1))
	q = input("Q: ")
	a = input("A: ").lower()
	QUESTION.append(q)
	ANSWER.append(a)
	push_qa()
	
def edit_set():
	clear()
	show_all_q()
	current_question=

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
	Enter the name of the test you would like to edit.
	Enter q to exit the quizmaker.
			""")
			print("	Choices:")
			for i in fileList:
				print("	"+i.rstrip("\.jdq"))
			
			current_test = input("Choice: ")
			if current_test == "q":
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
		
def editor_menu():
	global current_test
	editing = True
	argument = 7
	while editing:
		choosing = True
		while choosing:
			clear()
			print(EDITING+current_test)
			print("""
	Make a choice below
	
	1. Show questions
	2. Show answers
	3. Show a question and answer
	4. Show all questions and answers
	5. Add Question and answer 
	6. Edit Question and answer
	7. Return to the main menu
			""")
		
			try:
				argument = int(input("Choice: "))
				choosing = False
			except:
				print(INVALID)
				
		if argument == 1:
			print("selected one")
			show_all_q()
			print(EDITING+current_test)
			hold()
		elif argument==2:
			show_all_a()
			print(EDITING+current_test)
			hold()
		elif argument==3:
			show_pair(set_question(-1))
			print(EDITING+current_test)
			hold()
		elif argument==4:
			show_all_sets()
			print(EDITING+current_test)
			hold()
		elif argument==5:
			add_set()
			hold()
		elif argument==6:
			edit_set()
			print(EDITING+current_test)
			hold()
		elif argument==7:
			editing=False
		else:
			print(INVALID)
def edit_exitsing():
	choose_test()
	editor_menu()
	
def create_new():
	print("Create")
	
def instructions():
	print(INSTRUCTIONS)

def menu():
	choosing = True
	while choosing:
		print(MENU)
		try:
			argument = int(input("Choice: "))
			choosing = False
		except:
			print(INVALID)
	
	if argument == 1:
		edit_exitsing()
	elif argument==2:
		create_new()
	elif argument==3:
		instructions()
	elif argument==4:
		exit()
	else:
		print(INVALID)
	
		
if __name__ =="__main__":
	check_sys()
	running = True
	while running:
		menu()