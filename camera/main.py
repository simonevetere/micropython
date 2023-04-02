import display
import touch
import camera
import time

camera_activated = False
zoom_activated = 1

def activate_camera(button):
    global camera_activated, zoom_activated
    if camera_activated:
        camera_activated = False
        camera.overlay(camera_activated)
    else:
        camera_activated = True
        time.sleep(2)
        camera.overlay(camera_activated)
        
def zoom_camera(button):
    global camera_activated, zoom_activated
    if camera_activated:
        if zoom_activated == 1:
            zoom_activated = 16
            camera.zoom(zoom_activated)
        else:
            zoom_activated = 1
            camera.zoom(zoom_activated)
    else:
        display.text("Camera not activated!", 0, 0, 0xffffff)
        display.text("Tap right button to activate", 0, 50, 0xffffff)
        display.show()

touch.callback(touch.A, activate_camera)
touch.callback(touch.B, zoom_camera)

display.text("Tap a touch button:", 0, 0, 0xffffff)
display.text("right for camera", 300, 60, 0xffffff)
display.text("left for zoom", 0, 60, 0xffffff)
display.show()
