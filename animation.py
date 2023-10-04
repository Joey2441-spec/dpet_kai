import tkinter as tk
from PIL import ImageTk, Image

"""
Deals with processing the images and setting up the 
frame by frame
"""
class Animation:
  def __init__(self, window):
    self.window = window

    self.impath = "./sprites/img"
    self.current_frame = '/shime1.png'

    # holds the window.after
    self.current_animation_handle = 'none'
    # used in the case we need to invert the images
    self.facing_direction = 'none'

    # image data
    self.img_frames = []
    self.img_inverted = [] # if necessary 
    self.img_duration = []
    self.img_speed = []
    self.current_frame_index = 0

    self.image = tk.PhotoImage(file=self.impath + self.current_frame)
    self.image_label = tk.Label(self.window, image=self.image, bd=0, bg='black')
    self.image_label.pack()
    
  # type : walk, run, jump, stand based on the config.json
  def animation(self):
    # all information on which animation is given from change_animation
    self.current_frame_index = (self.current_frame_index + 1) % len(self.img_frames)

    if self.facing_direction == 'right': 
      self.image_label.config(image=self.img_inverted[self.current_frame_index])
    else:
      self.current_frame = self.img_frames[self.current_frame_index]
      self.image.config(file=self.impath + self.current_frame)
      self.image_label.config(image=self.image)

    self.current_animation_handle = self.window.after(self.img_duration[self.current_frame_index] * 15, self.animation)

  def invert_images(self):
    for img in self.img_frames:
      original_img = Image.open(self.impath + img)
      flipped_image = original_img.transpose(Image.FLIP_LEFT_RIGHT)
      tk_image = ImageTk.PhotoImage(flipped_image)
      self.img_inverted.append(tk_image)


  def change_animation(self, direction, imgs, duration):
    self.current_frame_index = 0
    self.facing_direction = direction
    self.img_frames = imgs
    self.img_duration = duration 
    self.img_inverted = []

  def remove_animation(self):
    if (self.current_animation_handle != 'none'):
      self.window.after_cancel(self.current_animation_handle)
      self.current_animation_handle = 'none'