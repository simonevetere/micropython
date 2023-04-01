import display
import device
import uasyncio
import gc
import time
import touch

battlev = ""
firstaccess = True
battlevint = 100
app = ["phone", "camera" , "next?", "oppo", "aaaa"]
idx = 0
alive = ""
inapp = ""
time = "x"

def main_mia():
	async def battery_level():
		global battlevint
		
		if device.battery_level() < battlevint:
			battlevint = device.battery_level()

		battlev = str(battlevint) + '%'
		display.text(battlev, 0,0,0xffffff)

	def change_text(button):
		global app
		global idx
		global alive
		global lastapp
		global nextapp

		lastapp = alive
		limit = len(app) - 1
		
		if button == "A":
			idx = idx + 1
			if idx > limit:
				idx = 0
		if button == "B":
			idx = idx - 1
			if idx < 0:
				idx = limit
		alive = app[idx]

		draw_ui()
		persistent()
		print(alive)

	def draw_ui():
		
		global idx
		uasyncio.run(battery_level())

		y = 250
		xa = 50
		xb = 250
		xc = 450
		sizea = 100
		sizeb = 100
		sizec = 100
		colora = 0xffffff
		colorb = 0xffffff
		colorc = 0xffffff


		if idx == 0:
			colora = 0xf8db5E
			xa = 25
			sizea = 150 
		if idx == 1:
			colorb = 0xf8db5E
			xb = 225
			sizeb = 150
		if idx > 1:
			colorc = 0xf8db5E
			xc = 425
			sizec = 150

		display.hline(xa, y, sizea, colora)

		display.hline(xb, y, sizeb, colorb)

		display.hline(xc, y, sizec, colorc)

	def touch_listener(button):
		change_text(button)
		uasyncio.run(touch_listener_async(button))

	async def touch_listener_async(button):
		global inapp
		pressed = touch.state(button)
		uasyncio.sleep_ms(5000)
		pressed = touch.state(button)

		if pressed and button == "A":
			inapp = lastapp
			print("nav",inapp)

			display.show();
			display.text("LOADING : " + inapp,150,175,0xffffff)
			display.show();

		if pressed and button == "B":
			inapp = ""
			print("nav","back")



	def persistent():
		app1 = app[0]
		app2 = app[1]
		app3 = app[2]

		colorapp = 0xffffff
		
		if idx > 2:
			app1 = "< " + app[idx-2]
			app2 = app[idx-1]
			app3 = app[idx]

		display.text(app1[:4],50,175,colorapp)
		display.text(app2[:4],250,175,colorapp)
		display.text(app3[:4] + " >",450,175,colorapp)
		
		battery_level()
		display.show()
		gc.collect()

	touch.callback(touch.BOTH, touch_listener)

	display.text("MONOCLE",250,175,0xffffff)
	display.text("Press A to continue, B to go back",0,350,0xffffff)
	display.show()

main_mia()