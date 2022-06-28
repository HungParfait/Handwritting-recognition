from textwrap import fill
from keras.models import load_model
from tkinter import *
import tkinter as tk
import win32gui
from PIL import ImageGrab, Image
import numpy as np

model = load_model('handwriting.h5')
cates = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def predict_digit(img):
    #resize image to 28x28 pixels
    img = img.resize((28,28))
    #convert rgb to grayscale
    img = img.convert('L')
    img = np.array(img)
    #reshaping to support our model input and normalizing
    img = img.reshape(1,28,28,1)
    img = img.astype('float32')
    img = img/255.0
    #predicting the class
    res = model.predict(img).flatten()
    index = np.argmax(res)
    return cates[index], max(res)

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.lastx = self.lasty = 0

        # Creating elements
        self.canvas = tk.Canvas(self, width=300, height=300, bg = "black", cursor="cross")
        self.label = tk.Label(self, text="Draw..", font=("Helvetica", 32))
        self.classify_btn = tk.Button(self, text = "Recognise", command = self.classify_handwriting)   
        self.button_clear = tk.Button(self, text = "Clear", command = self.clear_all)
       
        # Grid structure
        self.canvas.grid(row=0, column=0, sticky=W, )
        self.label.grid(row=0, column=1)
        self.classify_btn.grid(row=1, column=1)
        self.button_clear.grid(row=1, column=0)
        
        #self.canvas.bind("<Motion>", self.start_pos)
        self.canvas.bind("<B1-Motion>", self.draw_lines)
        self.canvas.bind("<Button-1>", self.save_posn)
        

    def clear_all(self):
        self.canvas.delete("all")
        
    def classify_handwriting(self):
        HWND = self.canvas.winfo_id()  # get the handle of the canvas
        rect = win32gui.GetWindowRect(HWND)  # get the coordinate of the canvas
        a, b, c, d = rect
        rect = (a+4, b+4, c-4, d-4)
        im = ImageGrab.grab(rect)
        digit, acc = predict_digit(im)
        self.label.configure(text= digit + ', Accuracy:' + str(int(acc*100)) + '%')

    def draw_lines(self, event):
        self.canvas.create_line((self.lastx, self.lasty, event.x, event.y), width=20, capstyle='round', fill='white')
        self.save_posn(event)

    def save_posn(self, event):
        self.lastx, self.lasty = event.x, event.y

        
       
app = App()
mainloop()
