# Followed https://kivy.org/docs/tutorials/pong.html
from random import randint

import kivy
from kivy.app import App
from kivy.logger import Logger
from kivy.properties import NumericProperty, ReferenceListProperty, Clock, \
    ObjectProperty
from kivy.uix.widget import Widget
from kivy.vector import Vector

kivy.require('1.10.0')


class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos


class PongGame(Widget):
    ball = ObjectProperty()
    player1 = ObjectProperty()
    player2 = ObjectProperty()

    def serve_ball(self, speed=4, min_angle=0, max_angle=360):
        self.ball.center = self.center
        new_velocity = Vector(speed, 0).rotate(randint(min_angle, max_angle))
        self.ball.velocity = new_velocity

    def update(self, dt):
        self.ball.move()

        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)

        if (self.ball.y < 0) or (self.ball.top > self.height):
            self.ball.velocity_y *= -1

        if self.ball.x < 0:
            self.player2.score += 1
            self.serve_ball(min_angle=-90, max_angle=90)
        if self.ball.x > self.width:
            self.player1.score += 1
            self.serve_ball(min_angle=90, max_angle=270)

    def on_touch_move(self, touch):
        if touch.x < self.width / 3:
            self.player1.center_y = touch.y
        if touch.x > self.width - self.width / 3:
            self.player2.center_y = touch.y


class PongPaddle(Widget):
    score = NumericProperty(0)

    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            vx, vy = ball.velocity
            offset = (ball.center_y - self.center_y) / (self.height / 2)
            bounced = Vector(-1 * vx, vy)
            vel = bounced * 1.1
            ball.velocity = vel.x, vel.y + offset


class PongApp(App):
    def build(self):
        Logger.info('Pong: Building PongApp')
        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game


if __name__ == '__main__':
    Logger.info('Pong: Running PongApp')
    PongApp().run()
