import pygame
import numpy as np

RGB_COLOR = {
    'BLACK': (0,0,0),
    'WHITE': (255,255,255),
    'RED': (255,0,0),
    'GREEN': (0,255,0),
    'BLUE': (0,0,255)
}

S_WIDTH, S_HEIGHT = (1400, 800)

pygame.init()
screen = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
pygame.display.set_caption('Simple Pendulum in Python')

class Ball:
    def __init__(self, length, color, theta):
        self.gravity = 9.81
        self.length = length
        self.color = color
        self.theta = theta
        self.position = np.zeros(2)
        self.theta_velocity = 0
        self.theta_acceleration = 0
    
    def update(self):
        self.theta_acceleration = -1 * self.gravity / self.length * np.sin(self.theta)
        self.theta_velocity += self.theta_acceleration
        self.theta += self.theta_velocity
        
        x = self.length * np.sin(self.theta) + S_WIDTH // 2
        y = self.length * np.cos(self.theta)
        self.position = np.array([x, y])

class Pendulum: 
    def __init__(self, ball_info):
        self.ball_info = ball_info
        
    def update(self):
        for item in self.ball_info.values():
            item.update()
        
    def draw(self):
        screen.fill(RGB_COLOR['BLACK'])    
        pygame.draw.line(screen, RGB_COLOR['WHITE'], start_pos=(0, 15), end_pos=(1400, 15), width=30)
        
        for item in self.ball_info.values():
            x, y = item.position
            pygame.draw.line(screen, item.color, start_pos=(S_WIDTH//2, 30), end_pos=(x, y), width=1)
            pygame.draw.circle(screen, item.color, (x, y), radius=15)


if __name__== '__main__':

    ball_info = {
        '1st': Ball(length=80, color=RGB_COLOR['RED'], theta=np.pi / 4),
        '2nd': Ball(length=320, color=RGB_COLOR['GREEN'], theta=np.pi / 4),
        '3rd': Ball(length=720, color=RGB_COLOR['BLUE'], theta=np.pi / 4)
    }
    
    pendulum = Pendulum(ball_info)
    
    while True:
        pendulum.update()
        pendulum.draw()

        pygame.time.delay(30)
        pygame.display.flip()