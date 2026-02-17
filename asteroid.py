import pygame
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from circleshape import CircleShape
from logger import log_event
import random

class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)
		
	def draw(self, screen):
		pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

	def update(self, dt):
		self.position += (self.velocity * dt)

	def split(self):
		self.kill()
		if self.radius <= ASTEROID_MIN_RADIUS:
			return
		else:
			log_event("asteroid_split")
			angle = random.uniform(20, 50)
			angle2 = 0 - angle
			x = self.position[0]
			y = self.position[1]
			rad = self.radius - ASTEROID_MIN_RADIUS
			asteroid1 = Asteroid(x, y, rad)
			asteroid2 = Asteroid(x, y, rad)
			asteroid1.velocity = self.velocity.rotate(angle) * 1.2
			asteroid2.velocity = self.velocity.rotate(angle2) * 1.2
