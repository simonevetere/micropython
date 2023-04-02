# This program allows users to activate the camera and zoom in/out using touch buttons.
# Touch button A activates the camera and touch button B zooms in/out.
# The current camera activation status and zoom level are displayed on the screen.
# When the camera is not activated, a message is displayed prompting the user to activate it.

import display
import touch
import camera
import time

camera_activated = False
zoom_activated = 1

def display_info():
    display.text("Tap a touch button:", 0, 0, 0xffffff)
    display.text("right for camera", 300, 60, 0xffffff)
    display.text("left for zoom", 0, 60, 0xffffff)
    display.show()

def activate_camera(button):
    global camera_activated, zoom_activated
    if camera_activated:
        camera_activated = False
        camera.overlay(camera_activated)
        display_info()
    else:
        camera_activated = True
        if zoom_activated != 1:
            zoom_activated = 1
            camera.zoom(zoom_activated)
        camera.overlay(camera_activated)
    time.sleep(0.5)
        
def zoom_camera(button):
    global zoom_activated, camera_activated
    if camera_activated:
        if zoom_activated == 1:
            zoom_activated = 16
            camera.zoom(zoom_activated)
        else:
            zoom_activated = 1
            camera.zoom(zoom_activated)
    else:
        display.show()
        display.text("Camera not activated!", 0, 0, 0xffffff)
        display.text("Tap right button to activate", 0, 50, 0xffffff)
        display.show()
    time.sleep(0.5)

touch.callback(touch.A, activate_camera)
touch.callback(touch.B, zoom_camera)

display_info()
