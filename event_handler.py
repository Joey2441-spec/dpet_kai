import tkinter as tk
from pet import Pet
from animation import Animation
from sprite_data import SpriteData

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

    # test
    self.action('climbWall', 'floor', 'up')


  def generate_random_events(self):
    # generates events and its duration
    pass




  # name = walk, climb ceil
  def action(self, type, orientation, direction):
    self.pet.remove_state()
    self.animation.remove_animation()

    # set configs 
    self.pet.change_state_data(orientation, direction, self.sprite_data[type]['speed'], self.sprite_data[type]['duration'])
    self.animation.change_animation(direction, self.sprite_data[type]['imgs'], self.sprite_data[type]['duration'])

    if (direction == 'right'):
      self.animation.invert_images()

    self.pet.move()
    self.animation.animation()


    
    
  