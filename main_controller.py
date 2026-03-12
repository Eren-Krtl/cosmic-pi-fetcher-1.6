import subprocess
import sys
import threading


opened_window = subprocess.Popen(['kitty', '-e', 'python3', 'fetcher_and_writer.py'])

def input_wait():
	input_s:str = input()
	if (input_s == "close"):
		print("Are you sure closing the process")

	opened_window.wait()
	sys.exit()
