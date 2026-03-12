import sys
import subprocess


while True:
	command_value:str = input()
	if (command_value == "write"): #Writes on top of the file
		input_i:str = input("Writing File: ")
		with open("veri.txt", "a") as file:
			file.write(input_i + "\n")
			print(f"Wrote: {input_i}")
	elif(command_value == "clear"): #Clears the target website
		print("Clear file")
		print("Are you sure this will clear every data and only should be used to clear experimental data")
		input_i:str =	input("Give in the password to clear the data: ")
		if (input_i == "Kedok123"):
			with open("veri.txt", "w") as file:
				file.write("")
			print("Deletion Complete")
		else:
			print("Password wrong cancelling deletion")
	elif(command_value == "close"): #Closes the process
		input_i:str = input("Closing the procces. Are you sure? (Y/n)")
		if(input_i == "y"):
			sys.exit()
		else:
			print("Cancelling closing")
	elif(command_value == "reset"):
		print("Resetting file")
		print("Are you sure resetting the file this will close the procces and erase the data")
		input_i:str = input("Give	in the password to reset the file: ")
		if(input_i == "Kedok123"):
			with open("veri.txt", "w") as file:
				file.write("")
			subprocess.run(["pkill", "-f", "main_controller.py"])
			subprocess.run(["pkill", "-f", "fetcher_and_writer.py"])
			sys.exit()
		else:
			print("Wrong password. Cancelling the procces")
	else:
		print(f"Couldn`t find the command {command_value}")
	pass
