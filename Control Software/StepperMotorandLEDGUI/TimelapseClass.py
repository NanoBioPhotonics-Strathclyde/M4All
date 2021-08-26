from time import sleep
import sys
from threading import Thread, Event
from picamera import PiCamera

class Timelapse():
    def __init__(self):
        
        self.width = 3280
        self.height = 2464
        self.frames = 10
        self.interval = 10
        self.File = "/home/pi/"
        
    def ChangeWidth(self,width):
        self.width = width
        return self
    
    def ChangeHeight(self,height):
        self.height = height
        return self
        
    def ChangeNumberOfFrames(self,frames):
        self.frames = frames
        return self

    def ChangeInterval(self,interval):
        self.interval = interval
        return self
    
    def ChangeFile(self,file):
        self.File = str(file)
        return self
    
    def StartTimelapseThread(self):
        self.tstopped = False
        t = Thread(target=self.StartTimelapse, args=())
        t.daemon = True
        t.start()
        return self

    def StartTimelapse(self):        
        if self.tstopped:
            return 
        camera = PiCamera()
        camera.resolution = (self.width,self.height)
        camera.start_preview(fullscreen=False, window=(200,200,800,800))
        sleep(self.interval)
        for i in range(self.frames):
            camera.capture(self.File + "/" + str(i) + ".jpg")
            sleep(self.interval)
        camera.close()
        camera.stop_preview()
        self.tstopped = True
        
    def StartPreviewThread(self):
        self.pstopped = False
        self.stop = False
        p = Thread(target=self.StartPreview, args=())
        p.daemon = True
        p.start()
        return self
        
    def StartPreview(self):
        if self.pstopped:
            return
        camera = PiCamera()
        camera.resolution = (self.width,self.height)
        camera.start_preview(fullscreen=False, window=(200,200,800,800))
        FramesTaken = 0
        while self.stop == False:
            FramesTaken = FramesTaken + 1           
        else:
            camera.close()
            camera.stop_preview()
    
    #def StartPreview(self):
        
            
    def StopPreview(self):
        self.stop = True
        