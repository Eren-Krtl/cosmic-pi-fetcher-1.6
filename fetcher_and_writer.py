import subprocess
import sys
import threading
import time
import requests

from bs4 import BeautifulSoup


opened_window = subprocess.Popen(['kitty', '-e', 'python3',  'input.py'])

print("The Process Has Been Started")
print("If the terminal is closed the process will stop")

def watch_process():
	opened_window.wait()
	sys.exit()

watch_thread = threading.Thread(target=watch_process, daemon=True)
watch_thread.start()


def read_and_write():
	#with open("./index.html", "r") as file:
	#	html = file.read()

	response = requests.get("http://192.168.0.1")
	html = response.text
	soup = BeautifulSoup(html, "html.parser")


	panels = soup.find_all("div", class_="panel-heading")

	for panel in panels:
		if("Auto refresh dashboard every 5 seconds" not in panel.get_text()):
			print(f"{panel.get_text()}")
			with open("veri.txt", "a") as file:
				file.write(panel.get_text() + "\n")
	with open("veri.txt", "a") as file:
		file.write("end" + "\n")
	return

while (True):
	print("a loop has happened")
	read_and_write()

	time.sleep(5)

