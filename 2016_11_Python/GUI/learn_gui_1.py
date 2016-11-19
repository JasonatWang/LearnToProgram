from tkinter import *


class ProcessButtonEvent:
    def __init__(self):
        window = Tk()
        window.title("First GUI Demo")

        frame_1 = Frame(window)
        frame_1['bg'] = "white"
        frame_1.pack()
        self.lable = Label(frame_1, text='Welcome to Python!', bg="white")
        button = Button(frame_1, text="Click Me")
        btOK = Button(frame_1, text="OK", fg="white", bg="LimeGreen", command=self.processOkay)
        btCancel = Button(frame_1, text="Cancel", fg="white", bg="Tomato", command=self.processCancel)

        self.lable.pack()
        button.pack()
        btOK.pack()
        btCancel.pack()

        window.mainloop()

    def processOkay(self):
        self.lable['text'] = "OK button is clicked"
        print("OK button is clicked")

    def processCancel(self):
        self.lable['text'] = "Cancel button is clicked"
        print("Cancel button is clicked")


window_1 = ProcessButtonEvent()