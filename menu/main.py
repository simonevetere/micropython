import display
import touch

def display_text(text):
	start = 50

	for app in text:
		display.text(app,150,start,0xffffff)
		start = start + 50   
	
	display.show()


def onclick(button):
	print('app=menu&server=get_app&callback=display_text')

touch.callback(touch.BOTH, onclick)