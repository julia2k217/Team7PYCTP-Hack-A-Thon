import tkinter.ttk
from tkinter import *
from tkinter import Button as Btn
from tkinter import messagebox as mbox
from tkinter.colorchooser import askcolor
from tkinter.ttk import *
import os
from PIL import Image
import keyboard


class Paint(object):
    INITIAL_PEN_SIZE = 5.0
    INITIAL_COLOR = 'black'

    def __init__(self):
        self.drawn_line = []
        self.all_drawn_lines = []
        self.popup = None
        self.active_btn = None
        self.eraser_on = None
        self.color = None
        self.save_btn = None
        self.line_width = None
        self.old_y = None
        self.old_x = None
        self.root = Tk()

        self.pen_btn = Btn(self.root, text='pen', command=self.use_pen)
        self.pen_btn.grid(row=0, column=0)

        self.color_btn = Btn(self.root, text='color', command=self.choose_color)
        self.color_btn.grid(row=0, column=1)
        keyboard.add_hotkey('q', self.choose_color)


        self.eraser_btn = Btn(self.root, text='eraser', command=self.use_eraser)
        self.eraser_btn.grid(row=0, column=2)

        self.undo_button = Btn(self.root, text='undo', command=self.use_undo)
        self.undo_button.grid(row=0, column=3)
        keyboard.add_hotkey('ctrl + z', self.use_undo)

        self.clear_btn = Btn(self.root, text='clear', command=lambda: self.c.delete("all"))
        self.clear_btn.grid(row=0, column=4)

        self.choose_size_btn = Scale(self.root, from_=1, to=10, orient=HORIZONTAL)
        self.choose_size_btn.grid(row=0, column=5)

        self.txt_file_name = tkinter.ttk.Entry()
        self.txt_file_name.grid(row=0, column=6, columnspan=1)

        self.save_btn = Btn(self.root, text='save', command=self.use_save)
        self.save_btn.grid(row=0, column=7)

        self.c = Canvas(self.root, bg='white', width=800, height=800)
        self.c.grid(row=1, columnspan=8)

        self.setup()
        self.root.mainloop()

    def setup(self):
        self.old_x = None
        self.old_y = None
        self.line_width = self.choose_size_btn.get()
        self.color = self.INITIAL_COLOR
        self.eraser_on = False
        self.active_btn = self.pen_btn
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)
        # initialize the variables
        self.all_drawn_lines = []
        self.drawn_line = []

    def use_pen(self):
        self.activate_btn(self.pen_btn)

    def choose_color(self):
        self.eraser_on = False
        self.color = askcolor(self.notag(self.color))[1]
    
    def notag (self, string):
        #to remove the tag from the decimal
        new_str = ""
        for character in string:
            if character != '#':
                new_str += character
        return new_str

    def use_eraser(self):
        self.activate_btn(self.eraser_btn, eraser_mode=True)

    def activate_btn(self, some_btn, eraser_mode=False):
        # pass
        self.active_btn.config(relief=RAISED)
        some_btn.config(relief=SUNKEN)
        self.active_btn = some_btn
        self.eraser_on = eraser_mode

    def paint(self, event):
        self.line_width = self.choose_size_btn.get()
        paint_color = 'white' if self.eraser_on else self.color
        if self.old_x and self.old_y:
            # store the lines drawn
            drawn_dot = self.c.create_line(self.old_x, self.old_y, event.x, event.y,
                                           width=self.line_width, fill=paint_color,
                                           capstyle=ROUND, smooth=TRUE, splinesteps=36)
            self.drawn_line.append(drawn_dot)

        self.old_x = event.x
        self.old_y = event.y

    def use_undo(self):
        if self.all_drawn_lines:
            last_line = self.all_drawn_lines.pop()
            for dots in last_line:
                self.c.delete(dots)
                

    def reset(self, event):
        self.old_x, self.old_y = None, None
        # update and reset the variable
        self.all_drawn_lines.append(self.drawn_line)
        self.drawn_line = []

    def use_save(self):
        file_save = self.txt_file_name.get()
        if len(str(file_save)) < 2:
            mbox.showerror("File Name Error", "Please enter valid file name!")
            return ""
        else:
            if not os.path.exists(file_save):
                print(file_save + '.png')
                self.c.postscript(file=file_save + '.eps')
                # use PIL to convert to PNG
                img = Image.open(file_save + '.eps')
                img.save(file_save + '.png', 'png')
            else:
                mbox.showerror("Error", "File already exists!")


if __name__ == '__main__':
    Paint()
