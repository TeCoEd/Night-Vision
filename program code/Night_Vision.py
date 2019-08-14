from guizero import App,PushButton
from guizero import info
from time import sleep
from subprocess import check_call
from picamera import PiCamera
camera=PiCamera()

global capture_number
capture_number = 0
video_capture_number = 0

###short previews###
####################

def short_preview():
    print("10 second preview")
    #camera.start_preview(fullscreen=False, window =(400, 25, 400, 240))
    camera.start_preview()
    sleep(10)
    camera.stop_preview()

def long_preview():
    print("30 second preview")
    #camera.start_preview(fullscreen=False, window =(0, 0, 800, 440))
    camera.start_preview()
    sleep(30)
    camera.stop_preview()

def sixty_preview():
    print("60 second preview")
    #camera.start_preview(fullscreen=False, window =(0, 0, 800, 440))
    camera.start_preview()
    sleep(60)
    camera.stop_preview()

### add the longer previews###
##############################

def One_Min():
    print("1 min")
    camera.start_preview()
    sleep(60)
    camera.stop_preview()

def Three_Min():
    print("3 min")
    camera.start_preview()
    sleep(180)
    camera.stop_preview()

def Five_Min():
    print("5 min")
    camera.start_preview()
    sleep(180)
    camera.stop_preview()    

### Other features ###
######################    

def capture_image():
    global capture_number
    print("image captured")
    camera.start_preview()
    # Camera warm-up time
    sleep(1)
    camera.annotate_text = (str(capture_number) +'.jpg')
    camera.capture(str(capture_number) +'.jpg')
    camera.stop_preview()
    capture_number = capture_number+1
    
def video_capture():
    global video_capture_number
    print("video")
    camera.resolution = (800, 480)
    camera.start_preview()
    camera.start_recording(str(video_capture_number)+"Video_Capture.h264")
    camera.wait_recording(10)
    camera.stop_recording()
    camera.stop_preview()
    video_capture_number = video_capture_number+1

def Always_on():
    print("Always")
    ### pop up are you sure
    always = app.yesno("Check", "Are you sure? Other features cannot be used")
    if always == True:
        camera.start_preview()
        sleep(5) #CHANGE TO 300
        camera.stop_preview() 
    else:
        pass
        
def shutdown():
    #check_call(['sudo', 'poweroff'])
    close_down = app.yesno("SHUTDOWN", "Are you sure?")
    if close_down == True:
        app.warn("Ready", "Shutting down")
        sleep(3)
        check_call(['sudo', 'poweroff'])
    else:
        app.info("Shutdown", "Shutdown aborted")
    
app = App(title = 'Night Vision', width = "780", height = "400")
app.bg = "black"
app.text_color = "green"
#app.tk.attributes("-fullscreen", True)

### Code for buttons and functions ###
P_10 = PushButton(app, text="10s", width = "fill", height = "fill", align = "right", command=short_preview) #30 seconds
P_20 = PushButton(app, text="30s", width = "fill", height = "fill", align = "right", command=long_preview)
P_30 = PushButton(app, text="60s", width = "fill", height = "fill", align = "right", command=sixty_preview)

One_Min = PushButton(app, text="5m", width = "fill", height = "fill", align = "right", command=One_Min) #1 minute full screen
Three_Min = PushButton(app, text="10m", width = "fill", height = "fill", align = "right", command=Three_Min) #add full screen
Five_Min = PushButton(app, text="15m", width = "fill", height = "fill", align = "right", command=Five_Min) #add full screen

Image = PushButton(app, text="Photo", width = "fill", height = "fill", align = "right", command=capture_image)
Video = PushButton(app, text="Vid10s", width = "fill", height = "fill", align = "right", command=video_capture)
Always_on = PushButton(app, text="ON", width = "fill", height = "fill", align = "right", command=Always_on)
shutdown = PushButton(app, text="QUIT", width = "fill", height = "fill", align = "right", command=shutdown)

app.display()
