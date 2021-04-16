import cv2
from tkinter import *
from PIL import ImageTk, Image
import os
import numpy as np

dirSave = "C:\\Users\\Anmol Kumar\\Desktop\\Programs\\AgeGenderDetection\\Data"  # Enter your directory
n = 1
im = None

fName = dirSave + f"\\Prediction ({n}).jpg"
while os.path.isfile(fName):
    n += 1
    fName = dirSave + f"\\Prediction ({n}).jpg"


def click(image):
    cv2.imwrite(os.path.join(dirSave, fName), cv2.cvtColor(image, cv2.COLOR_RGB2BGR))
    screen.destroy()


def vid():
    global im
    ret, frame = cap.read()
    im = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    img = Image.fromarray(im)
    img = ImageTk.PhotoImage(image=img)

    lab.imgtk = img
    lab.configure(image=img)
    lab.after(1, vid)


choice = input("Live Detection or Photo ? (l or p) \nPress 'e' to exit\n")
while True:
    if choice == 'l':
        cap = cv2.VideoCapture(0)
        screen = Tk()

        app = Frame(screen)
        app.grid()
        lab = Label(app)
        lab.grid()
        but = Button(app, text="Click", command=lambda: click(im))
        but.grid()

        vid()
        screen.mainloop()

        cap.release()
        cv2.destroyAllWindows()

        break

    elif choice == 'p':
        fName = input("Enter file name with extension (<name>.<ext>): \n")
        break

    elif choice == 'e':
        break

    else:
        choice = input("Enter a correct choice:\nLive Detection or Photo ? (l or p) \nPress 'e' to exit \n")


if choice == 'l' or choice == 'p':
    from keras.models import load_model

    model = load_model("Detection.h5")

    imf = cv2.imread(dirSave + "\\" + fName)
    imf = imf[0:imf.shape[0], (imf.shape[1] - imf.shape[0]) // 2: imf.shape[1] - ((imf.shape[1] - imf.shape[0]) // 2)]
    imageFinal = cv2.resize(cv2.cvtColor(imf, cv2.COLOR_BGR2RGB), (48, 48))
    imageFinal = imageFinal / 255

    predIm = model.predict(np.array([imageFinal]))

    g = "Male" if int(np.round(predIm[1][0])) == 0 else "Female"
    print(f"Predicted Age: {int(np.round(predIm[0][0]))} Gender: {g}")
