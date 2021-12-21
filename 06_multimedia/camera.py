import picamera
import time

path = '/home/pi/src4/06_multimedia/'

camera = picamera.PiCamera()

try:
    while(True):
        camera.resolution = (640, 480)
        camera.start_preview()
        time.sleep(1)
        camera.rotation = 180
        user_value = input('photo : 1, video : 2, exit : 9 > ')
        now_str = time.strftime("%Y%m%d_%H%M%S")
        if user_value == '1':
            print('사진촬영')
            camera.capture('%sphoto_%s.jpg' % (path, now_str))
        elif user_value == '2':
            print('동영상촬영')
            camera.start_recording('%s/video_%s.h264' % (path, now_str))
            input('press enter to stop')
            camera.stop_recording()
        elif user_value == '9':
            break
        else:
            print('incorrect command')
        

finally:
    camera.stop_preview()