import display

def display_text(text):
    display.text(text,150,175,0xffffff)
    display.show();


def onclick(button):
	print('app=menu&server=get_app&callback=display_text')

touch.callback(touch.BOTH, onclick)