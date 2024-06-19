import cv2 as cv
import time


def findCamIndex():
    for i in range(10):

        cap = cv.VideoCapture(i)

        if cap.isOpened():
            cap.release()
            return i
        
        cap.release()

    return None


def gen_frames(index):
    
    camera = cv.VideoCapture(1)

    inicio = time.time()
    tempo = time.time() - inicio

    while tempo <= 30:
        tempo = time.time() - inicio
        
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv.imencode('.jpeg', frame)
            frame = buffer.tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    camera.release()

    return
