import display
import touch

def display_text(in_app):
  
  display.text(app,150,start,0xffffff)
  
  display.show()


def onclick(button):

  if button == "B":
    print("app=menu&server=&callback=")
  if button == "A":
    print("app=example&server=get_random_json&callback=display_text")

display.text("press Right to show",150,50,0xffffff)
display.text("press Left to go back",150,150,0xffffff)
display.show()
touch.callback(touch.BOTH, onclick)