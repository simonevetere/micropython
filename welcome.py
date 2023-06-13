import touch
import display
import time
import gc

start = display.Fill(display.WHITE);
display.show(start)

vetere = display.Text("VETERE", 200, 150, display.BLACK);
TECH = display.Text("TECH", 350, 150, display.BLACK);

time.sleep(1);
display.show(start,vetere)
time.sleep(1);
display.show(start,vetere,TECH)

time.sleep(1);

gc.collect()

welcome = display.Text("welcome in vetere.tech", 20, 150, display.BLACK);
display.show(start,welcome)

gc.collect()

time.sleep(2);

welcome2 = display.Text("interface", 200, 150, display.BLACK);
display.show(start,welcome2)


print("app=menu&server=get_app&callback=display_text")