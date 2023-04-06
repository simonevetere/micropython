import display
import touch

idx = 0
in_app = []
endpoint = []

all_interface = [{"vetere.tech" : "https://vetere.tech/get_code?"},
                  {"example.com" : "https://example.com/example?"}]

def main():
  global in_app
  global endpoint
  for dictionary in all_interface:
      for key, value in dictionary.items():
        in_app.append(key)
        endpoint.append(value)
  display_text(in_app)

def display_text(in_app):
  global all_inteface
  display.text("Online Network Interface",50,0,0xffffff)
  start = 50
  all_inteface = in_app
  for app in in_app:
    if all_inteface[idx] == app:
      app = ">" + app
    display.text(app,150,start,0xffffff)
    start = start + 50   
  
  display.show()


def onclick(button):
  global idx
  global endpoint

  if button == "B":
    print(endpoint[idx])
  if button == "A":
    idx = idx + 1
    maxlen = len(in_app)
    if idx > maxlen - 1:
      idx = 0

touch.callback(touch.BOTH, onclick)
main()