import tkinter as tk
from pet import Pet
from animation import Animation
from sprite_data import SpriteData
from random import Random
import time

"""
Contains all the binding methods
"""
class EventHandler:
  def __init__(self, window):
    self.window = window
    self.pet = Pet(self.window)
    self.animation = Animation(self.window)
    self.sprite = SpriteData()
    self.sprite_data = self.sprite.loadData()

    # event generator
    self.random = Random()
    # action, orientation, facing_direction, direction
    self.actions = [['walk', 'floor', 'left', 'left'],
                    ['walk', 'floor', 'right', 'right'],
                    ["climbWall", 'wall', 'left', 'up'],
                    ["climbWall", 'wall', 'left', 'down'],
                    ["climbWall", 'wall', 'right', 'up'],
                    ["climbWall", 'wall', 'right', 'down'],
                    ["climbCeiling", 'ceiling', 'left', 'left'],
                    ["climbCeiling", 'ceiling', 'right', 'right']]
  
    
    # its default action will always be starting to the left 
    self.current_action = self.actions[0]

    # test
    self.generate_random_events()


  def generate_random_events(self):
    # generates events and its duration
    # we need facing_direction then the type of action for that facing_direction like walk, climbWall, climbCeiling
    self.new_action = ["climbWall", 'wall', 'left', 'up']
    #self.random.choice(self.actions)
    # if the orientation does not match with the current one we need to make go to that orientation
    if (self.current_action[1] != self.new_action[1]):
        # need to add state change, if going from ceil to floor we need to go through an wall
        # if going from floor to ceil need to go through a wall 
        # otherwise we can directly shift orientation
        if (self.current_action[1] == 'floor' and self.new_action[1] == 'ceil'):
          self.shift_orientation('floor', 'wall', self.current_action)
          self.shift_orientation('wall', 'ceil', ['climbWall', 'wall', self.current_action[2], 'up'])
        elif (self.current_action[1] == 'ceil' and self.new_action[1] == 'floor'):
          self.shift_orientation('ceil', 'wall', self.current_action)
          self.shift_orientation('wall', 'floor', ['climbWall', 'wall', self.current_action[2], 'down'])
        else:
          self.shift_orientation(self.current_action[1], self.new_action[1], self.current_action)
        
    self.action(self.new_action[0], self.new_action[1], self.new_action[2], self.new_action[3])

    #self.window.after(10000, self.generate_random_events)


  def shift_orientation(self, fromOrientation, toOrientation, action):
    self.pet.change_state_data(fromOrientation, action[2], self.sprite_data[action[0]]['speed'], self.sprite_data[action[0]]['duration'])
    print(self.pet.direction)
    print(self.pet.duration)
    print(self.pet.speed)
    self.animation.change_animation(action[2], self.sprite_data[action[0]]['imgs'], self.sprite_data[action[0]]['duration'])
    
    if (fromOrientation == 'floor' or fromOrientation == 'ceiling'):
      self.animation.animation()
      while((self.window.winfo_x() > 25) and (self.window.winfo_x() < self.window.winfo_screenwidth())):
        print(self.window.winfo_x())
        self.pet.move(False)
        self.window.update() # need to update as setting geometry doesn't instantly update

      
      

  # name = walk, climb ceil
  def action(self, type, orientation, facing_direction, direction):
    self.pet.remove_state()
    self.animation.remove_animation()

    # set configs 
    self.pet.change_state_data(orientation, direction, self.sprite_data[type]['speed'], self.sprite_data[type]['duration'])
    self.animation.change_animation(facing_direction, self.sprite_data[type]['imgs'], self.sprite_data[type]['duration'])

    if (facing_direction == 'right'):
      self.animation.invert_images()

    self.pet.move(True)
    self.animation.animation()


    
    
  