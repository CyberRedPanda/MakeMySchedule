# Replace the following catagories with things you want to do every day:
# RFI Hours
# Product Hours
# Work out
# Python 
# Cert
# Typing

import time
import random
import sys

def eight_hours_a_day(total_time, schedule):
	total_time = 0
	for item in schedule:
		for value in item.values():
			total_time += value
	if total_time < 480:
		free_time = 480 - total_time
		free_time = round(free_time, 2)
		string_to_print = "All right, it looks like you have {free_time} hours of free time today!".format(free_time=(free_time)/60)
		print(string_to_print)
		add_tasks(schedule)
	elif total_time > 480:
		total_time = round(total_time, 2)
		string_to_print = "uh-oh, it looks like you have scheduled {over_time} hours instead of 8!\n".format(over_time=(total_time/60))
		print(string_to_print)
		time.sleep(1)
		print("Maybe I can help you modify that a bit")
		time.sleep(1)
		take_away_tasks(total_time, schedule)

def take_away_tasks(total_time, schedule):
	done = ""
	while done != "y":
		print("This is what I have right now: \n")
		for item in schedule:
			print(item)
		print("")
		modify = input("What can I modify for you? (please type the name of the activity you see above)\n")
		for item in schedule:
			for key, value in item.items():
				if modify == key:
					time = input("And how long would you like to spend on that (in minutes)?\n")
					item[key] = int(time)
					done = input("all done? (y/n)")
		if done != "y":
			print("Sorry, I don't think I have that on the list.")

	eight_hours_a_day(total_time, schedule)

def add_tasks(schedule):
	more = input("want me to add any activities to fill that free time? (y/n)\n")
	if more == "y":
		add_new_task()
	elif more == "n":
		total_time = 0
		for item in schedule:
			for value in item.values():
				total_time += value
		if total_time > 480:
			over_time = total_time - 480
			print("uh-oh, it looks like you have scheduled {over_time} hours instead of 8!\n").format(over_time=over_time)
			take_away_tasks()
		else:
			free_time = 480 - total_time
			schedule.append({"Free Time":(free_time)})
			make_schedule(schedule)
	else:
		print("Sorry, I didn't understand you, can you please try again?")
		add_tasks(schedule)

def make_schedule(schedule):
	print("All right! One second, I'm making your schedule now.\n")
	print("Here is what I have for you: \n")
	time.sleep(1)
	start = 9
	random.shuffle(schedule)
	for item in schedule:
		print(str(round(start, 2)) + " to ", end="")
		for integer in item.values():
			start += integer/60
		print(start)
		for key in item.keys():
			print(key)
			print("\n")
	done = input("\n Is This all right? (y/n)\n")
	if done != "y":
		time.sleep(1)
		print("All right, let me try again, one second please...")
		time.sleep(1)
		make_schedule(schedule)
	else:
		print("all right, good luck, and have fun!")
		sys.exit()

def add_new_task():
	done = ""
	new_tasks = {}
	while done != "y":
		new_task_name = input("What other tasks do you need to do today?\n If there isn't anything, please type \"none\"\n")
		if new_task_name == "none":
			done = "y"
		else:
			add = input("add " + str(new_task_name) + " to schedule? (y/n)\n")
			if add != "y":
				add_new_task()
			elif add == "y":
				new_tasks[new_task_name] = int(input("how many minutes will it take?\n"))
				done = input("Is that everything? (y/n)\n")
			else:
				print("Sorry, I didn't understand you. \n")
				add_new_task()
	correct(typing, work_out, python, cert, new_tasks)

def correct(typing, work_out, python, cert, new_tasks):
	correction_list = [typing, work_out, python, cert]
	print("Okay, I also have this for the day\n")
	for item in correction_list:
		print(item)
	answer = input("Are these all okay? (y/n)\n")
	if answer == "n":
		done = ""
		while done != "y":
			correction = input("Which item should I change?\n").lower()
			if correction == "typing":
				typing["Typing"] = int(input("How long would you like to spend on typing?\n").lower())
				done = input("is that all? (y/n)\n")
			elif correction == "work_out":
				work_out["Work_out"] = int(input("How long would you like to spend working out?\n").lower())
				done = input("is that all? (y/n)\n")
			elif correction == "python":
				python["Python"] = int(input("How long would you like to spend on python?\n").lower())
				done = input("is that all? (y/n)\n")
			elif correction == "cert":
				cert["Cert"] = int(input("How long would you like to spend studying for a certification?\n").lower())
				done = input("is that all? (y/n)\n")
			else:
				print("Sorry, I didn't get that, can you please try again?\n")

	if new_tasks == {}:
		schedule = [typing, work_out, python, cert, rfis, product]
	else:
		schedule = [typing, work_out, python, cert, rfis, product, new_tasks]
	total_time = 0
	eight_hours_a_day(total_time, schedule)
			


# Daily standard tasks
typing = {"Typing":15}
work_out = {"Work_out":60}
python = {"Python":60}
cert = {"Cert":30}
# Variable hour tasks
print("Good morning! I'm going to help you out with your schedule today, I'll just ask a few quick questions if that's okay.\n")
rfi_hours = int(input("Firstly, how many minutes do you need to work on RFIs?\n"))
product_hours = int(input("Okay, thank you. And how many minutes do you need to work on product tasks?\n"))
rfis = {"RFIs":rfi_hours}
product = {"Product":product_hours}
# Day specific tasks
add_new_task()




