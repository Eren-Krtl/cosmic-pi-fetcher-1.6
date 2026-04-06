extends Control

@export var Start_Timer: Timer
@export var List: VBoxContainer
@export var ListText: PackedScene

func _ready():
	return

func _on_refresh_timer_timeout() -> void:
	print("the timer has run")
	Thread.new().start(execute_fetcher)
	read_and_show()
	return


func _on_start_button_toggled(toggle_b: bool) -> void:
	if(toggle_b == true):
		Start_Timer.start()
		#read_and_show()
	elif(toggle_b == false):
		Start_Timer.stop()
	print("the toggle is : ", toggle_b)

func read_and_show():
	var file = FileAccess.open("data.json", FileAccess.READ)
	if file:
		var data = JSON.parse_string(file.get_as_text())
		var latest_data = data[0]
		print(typeof(latest_data))
		print(latest_data)
		file.close()

func update_info(size_l:int):
	return

func execute_fetcher():
	OS.execute("nohup", [])
	print("Ran execute_fetcher")
	return
