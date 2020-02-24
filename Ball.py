import pygame


class Ball:
    left = 0
    right = 1

    def __init__(self, x_center, y_center, radius, color, fall=None, ball_id=None):
        self.x_center = x_center
        self.y_center = y_center
        self.radius = radius
        self.color = color
        self.ball_id = ball_id
        self.fall = fall

    def draw_ball(self, surface):
        self.ball_id = pygame.draw.circle(surface, self.color, (self.x_center, self.y_center), self.radius, 0)

    def move_along_x_axis(self, step_movement, left_bound, right_bound):
        if Ball.right == 1 and self.x_center <= right_bound - self.radius:
            self.x_center += step_movement
        elif Ball.left == 1 and self.x_center >= left_bound + self.radius:
            self.x_center -= step_movement
        if self.x_center >= right_bound - self.radius:
            Ball.left = 1
            Ball.right = 0
        if self.x_center <= left_bound + self.radius:
            Ball.right = 1
            Ball.left = 0

    def move_along_y_axis(self, step_movement, lower_bound, upper_bound=0):
        if self.y_center <= lower_bound:
            self.y_center += step_movement

    def refresh_ball(self):
        pygame.display.update(self.ball_id)