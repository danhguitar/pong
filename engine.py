import pygame
import random
import time
from sys import exit

pygame.init()


RESOLUTION = (1024,768)

screen = pygame.display.set_mode(RESOLUTION)

FRAMERATE = 60

FONT = pygame.font.Font('assets/font.ttf', 15)

BACKGROUND = pygame.transform.scale(pygame.image.load('background.png').convert(), RESOLUTION)

PADDLE = pygame.transform.rotate(pygame.transform.scale(pygame.image.load('paddle.png').convert(), (48,16)), 90)
BALL = pygame.transform.scale((pygame.image.load('ball.png').convert()), (16,16))


GAMESTATES = [
  'load',
  'title',
  'game'
]
gamestate = GAMESTATES[2]


class paddle(pygame.sprite.Sprite):
  def __init__(self, posX, posY, accelSpeed):
    pygame.sprite.Sprite.__init__(self)
    self.image = PADDLE
    self.rect = self.image.get_rect()
    self.rect.x = posX
    self.defaultX = posX
    self.defaultY = posY
    self.rect.y = posY
    self.Xoffset = self.image.get_width()/2
    self.Yoffset = self.image.get_height()/2
    self.width = self.image.get_width()
    self.height = self.image.get_height()
    self.accelY = 0
    self.accelSpeed = accelSpeed
  
  def move(self):
    if self.accelY < 0 and (self.rect.y > 0):
      self.rect.y += 2 * self.accelY
      self.accelY += self.accelSpeed/2
      if self.accelY > 0:
        self.accelY = 0
    
    if self.accelY > 0 and (self.rect.y+self.height)<screen.get_height():
      self.rect.y += 2 * self.accelY
      self.accelY -= self.accelSpeed/2
      if self.accelY < 0:
        self.accelY = 0

  def update(self):
    self.move()

class ball(pygame.sprite.Sprite):
  def __init__(self, posX, posY, directX, directY, constSpeed, accelSpeed):
    pygame.sprite.Sprite.__init__(self)
    self.image = BALL
    self.rect = self.image.get_rect()
    self.rect.x = posX
    self.rect.y = posY
    self.defaultX = posX
    self.defaultY = posY
    self.speed = constSpeed
    self.defaultSpeed = constSpeed
    self.accelSpeed = accelSpeed
    self.accelX = 0
    self.accelY = 0
    self.directX = directX
    self.directY = directY

  def move(self):
    if self.rect.y <= 0:
      self.directY = "down"
    if self.rect.y >= screen.get_height()-self.image.get_height():
      self.directY = 'up'

    if self.directX == "left":
      self.rect.x -= self.speed
    if self.directX == 'right':
      self.rect.x += self.speed
    if self.directY == 'up':
      self.rect.y -= self.speed
    if self.directY == 'down':
      self.rect.y += self.speed

  def flip(self):
    if self.directX == 'left':
      self.directX = 'right'
    elif self.directX == 'right':
      self.directX = 'left'
    """
    if self.directY == 'up':
      self.directY = 'down'
    elif self.directY == 'down':
      self.directY = 'up'
    """
    self.speed += .5
    #self.accelX += self.accelSpeed
    #self.accelY += self.accelSpeed

  def update(self):
    self.move()

  def reset(self, score, side):
    if side == 'right':
      score[0] += 1
    elif side == 'left':
      score[1] += 1
    else:
      score = [0,0]
    self.rect.x = self.defaultX
    self.rect.y = self.defaultY
    self.speed = self.defaultSpeed
    self.directX = 'right'
    self.directY = random.choice(['up', 'down'])
    return score
