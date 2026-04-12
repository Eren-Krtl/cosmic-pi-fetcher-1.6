extends Button

@export var TextEditButton : LineEdit
@export var FormatPanel : Panel

# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	if (TextEditButton.text == "Kedok123") :
		pass
	pass

func _on_toggled(toggle: bool) -> void:
	if (toggle == true):
		FormatPanel.show()
	else:
		FormatPanel.hide()


func _on_format_confirm_pressed() -> void:
	if(TextEditButton.text == "Kedok123"):
		print("Formatting in progress")
		OS.create_process(ProjectSettings.globalize_path("res://file_formatter"),[])

	TextEditButton.text = ""
