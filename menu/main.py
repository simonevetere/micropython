import display
import touch

idx = 0
all_app = ""

def display_text(in_app):
  global all_app
  start = 50
  all_app = in_app
  for app in in_app:
    if all_app[idx] == app:
      app = ">" + app
    a = display.Text(app,150,start,0xffffff)
    start = start + 50   
  
  display.show(a)


def onclick(button):
  global idx
  
  if button == "B":
    print("app=" + all_app[idx] + "&server=&callback=")
  if button == "A":
    print("app=menu&server=get_app&callback=display_text")
    idx = idx + 1
    maxlen = len(all_app)
    if idx > maxlen - 1:
      idx = 0


a = display.Text("press R to show/move",150,50,0xffffff)
b = display.Text("then press L to choose",150,150,0xffffff)
display.show(a,b)
touch.callback(touch.BOTH, onclick)