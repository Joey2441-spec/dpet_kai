import tkinter as tk
from event_handler import EventHandler
class App(tk.Tk):
  def __init__(self):
    super().__init__()
    # remove window's decorations
    self.overrideredirect(True)
    # set position
    self.geometry(f"128x128+{self.winfo_screenwidth() - 10}+200")
    # update the geometry and position the moment of creation
    self.update_idletasks()
    # set any black color to transparent
    self.wm_attributes("-transparentcolor", "black")
    # set up event listeners
    self.events = EventHandler(self)



app = App()


app.mainloop()
