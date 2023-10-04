"""
Holds information about the pet state
Manages the shifting of the window to mimic movement

"""
class Pet:
  def __init__(self, window):
    # reference the window
    self.window = window
    
    # idle, left, right, up, down
    self.direction = "idle"
    # idle, walk, run, climb, jump ...
    self.current_state = "none"
    # floor, ceiling, wall
    self.orientation = "floor"
    
    # speed
    self.speed = []
    # duration 
    self.duration = []
    # current index
    self.current_index = 0

  def move(self):
    self.current_index = (self.current_index + 1) % len(self.speed)
    current_speed = self.speed[self.current_index]
    current_duration = self.duration[self.current_index]

    current_position = 0
    new_position = 0

    match self.direction:
      case 'left':
        current_position = self.window.winfo_x()
        new_position = current_position + current_speed
      case 'right':
        current_position = self.window.winfo_x()
        new_position = current_position - current_speed
      case 'up':
        current_position = self.window.winfo_y()
        new_position = current_position + current_speed
      case 'down':
        current_position = self.window.winfo_y()
        new_position = current_position - current_speed

    if self.direction == 'left' or self.direction == 'right':
      if (new_position < 0):
        new_position = self.window.winfo_screenwidth()
      elif (new_position > self.window.winfo_screenwidth()):
        new_position = 0
    elif self.direction == 'up' or self.direction == 'down':
      if (new_position < 0):
        new_position = self.window.winfo_screenheight()
      elif (new_position > self.window.winfo_screenheight()):
        new_position = 0


    if (self.direction == 'left' or self.direction == 'right'):
      self.window.geometry(f"+{new_position}+{self.window.winfo_y()}")
    elif (self.direction == 'up' or self.direction == 'down'):
      self.window.geometry(f"+{self.window.winfo_x()}+{new_position}")

    self.current_state = self.window.after(current_duration * 15, self.move)


  def change_state_data(self, orientation, direction, speed, duration):
    self.orientation = orientation
    self.direction = direction
    self.duration = duration
    self.speed = speed
    self.current_index = 0

  def remove_state(self):
    if (self.current_state != 'none'):
      self.window.after_cancel(self.current_state)
      self.current_state = 'none'
