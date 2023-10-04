import tkinter as tk
from event_handler import EventHandler

print(tk.TkVersion)


class App(tk.Tk):
  def __init__(self):
    super().__init__()
    # remove window's decorations
    self.overrideredirect(True)
    # set position
    self.geometry("128x128+1500+200")
    # update the geometry and position the moment of creation
    self.update_idletasks()
    # set any black color to transparent
    self.wm_attributes("-transparentcolor", "black")
    # set up event listeners
    self.events = EventHandler(self)



app = App()


app.mainloop()
