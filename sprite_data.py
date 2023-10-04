
import json
"""
Focused on returning and getting all the data we need in the config.json
"""
class SpriteData:
  def __init__(self):
    self.name = 'none'
    self.imgs = []
    self.duration = []
    self.speed = []
    self.sprite_data = 'none'

  def loadData(self):
    with open('config.json') as f:
      self.sprite_data = json.load(f)
    return self.sprite_data
    