Project reference:
A simple paint application using tkinter in Python 3 
By: Nikhil Kumar Singh
https://gist.github.com/nikhilkumarsingh/85501ee2c3d8c0cfa9d1a27be5781f06

Process overview
Imagine you have a digital canvas that you can draw on, like a drawing app. The Python script you provided is like the set of instructions that creates this drawing app.

Here's what the script does in simpler terms:

Getting Ready: The script starts by getting everything ready. It brings in tools (functions) from a library called "tkinter" that helps make the drawing app.

Drawing Tools: It sets up different buttons for different drawing tools you can use. You have buttons for a pen, choosing colors, undo, clear, save and an eraser, just like in a real art kit.

Canvas: The "canvas" is like your drawing paper. The script creates a big white canvas where you can draw. It also prepares for different things you might need while drawing.

Starting to Draw: When you start the app, it's like opening your art kit. You can pick a tool to use, like a pen. The script knows which tool you picked and shows it as active.

Picking Colors: If you want to use colors, there's a button to pick the color you want to draw with.

Using the Eraser: You can also "erase" things you draw. It's like having a magic eraser that deletes your drawings. There's a button for this too. In reality the eraser is actually just white paint. 

Changing Line Size: You can choose how thick or thin your lines will be. There's a tool to adjust this.

Drawing: When you move your mouse while holding down the left button, the script draws on the canvas. If you choose a color, it draws with that color. If you're erasing, it erases. It uses your mouse movements to make lines.

Stopping and Starting: When you let go of the mouse button, the script stops drawing. It's like lifting your pencil off the paper. If you start drawing again, the script knows where you left off and continues from there.

Running the App: At the end of the script, it runs the drawing app. It's like turning on your app and being able to draw and use all those tools.

So, this script helps you create a simple digital drawing app where you can use different tools to draw, erase, and choose colors on a canvas. It's like having a virtual art kit on your computer!


Tech overview
The provided Python script is a simple paint application built using the Tkinter library. It allows the user to draw using different tools (pen, brush, eraser) and change the drawing color and line size. Here's a review of the script:

1. Import Statements: The script starts by importing necessary classes from the `tkinter` module, such as `Tk`, `Button`, `Scale`, and `Canvas`, as well as the `askcolor` function from `tkinter.colorchooser`.

2. Class Definition - Paint: The main functionality of the paint application is encapsulated in the `Paint` class. The class has various methods to handle different actions and interactions.

3. Constructor `__init__`: The `__init__` method initializes the paint application. It creates the main window (`Tk`), initializes instance variables, creates buttons for different tools (pen, brush, color, eraser), a scale widget to select line size, and a canvas widget for drawing.

4. Method `setup`: This method is used to set up the initial state of the application. It resets variables like `old_x`, `old_y`, `line_width`, `color`, and `eraser_on`, and binds canvas events to corresponding methods.

5. Tool Methods: There are methods like `use_pen`, `choose_color`, and `use_eraser` which set the active tool and update the UI accordingly.

6. Method `activate_button`: This method is used to highlight the active tool button and set the eraser mode if needed.

7. Drawing Methods: The methods `paint` and `reset` handle the actual drawing. The `paint` method is triggered when the mouse is dragged on the canvas, and it creates lines based on the mouse movement. The `reset` method is called when the mouse button is released, resetting the previous position.

8. Main Execution Block: The script concludes with the standard `if __name__ == '__main__':` block, where an instance of the `Paint` class is created to start the application.


Tech Reference :

Tkinter Documentation:
Official Tkinter Documentation: https://docs.python.org/3/library/tkinter.html
Tkinter Tutorial: https://tkdocs.com/tutorial/index.html
Canvas Widget:
Canvas Widget Overview: https://tkdocs.com/tutorial/canvas.html
Button Widget:
Button Widget Documentation: https://docs.python.org/3/library/tkinter.html#button
Button Command Callbacks: https://effbot.org/tkinterbook/button.htm
Scale Widget:
Scale Widget Documentation: https://docs.python.org/3/library/tkinter.html#scale
Scale Widget Tutorial: https://www.tutorialspoint.com/python/tk_scale.htm
Color Chooser (askcolor):
Color Chooser Documentation: https://docs.python.org/3/library/tkinter.colorchooser.html
Example of Using askcolor: https://www.delftstack.com/howto/python-tkinter/how-to-create-color-picker-in-tkinter/
Event Handling:
Tkinter Event Handling: https://tkdocs.com/tutorial/introduction.html#events-and-binders
Understanding Tkinter Event Handling: https://zetcode.com/tkinter/events-and-binds/
Canvas Drawing Methods:
Canvas create_line method: https://docs.python.org/3/library/tkinter.html#create-line
Canvas create_oval method: https://docs.python.org/3/library/tkinter.html#create-oval
Canvas create_rectangle method: https://docs.python.org/3/library/tkinter.html#create-rectangle
OOP Concepts:
Python Classes and Objects: https://docs.python.org/3/tutorial/classes.html
Object-Oriented Programming (OOP) in Python: https://realpython.com/python3-object-oriented-programming/
