import arcade
import arcade.key
from choice import Choice
 
SCREEN_WIDTH = 850
SCREEN_HEIGHT = 600
 
class YouBetMeWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.choice = Choice()
        self.world = World()
 
        arcade.set_background_color(arcade.color.WHITE)
        self.box = arcade.Sprite('images/box.png')
        self.box.set_position(305, 325)
        self.box2 = arcade.Sprite('images/box.png')
        self.box2.set_position(545, 325)
 
 
    def on_draw(self):
        arcade.start_render()
        self.box.draw()
        self.box2.draw()
        arcade.draw_text(str(self.choice.heart),
                         10, self.height - 30,
                         arcade.color.BLACK, 20)
        arcade.draw_text(str(self.choice.list[self.world.question-1][0]),
                         285, 310,
                         arcade.color.BLACK, 40)
        arcade.draw_text(str(self.choice.list[self.world.question-1][1]),
                         525, 310,
                         arcade.color.BLACK, 40)

class World():
    question = 1
    ans = 0
    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.LEFT:
            ans = 1
        if key == arcade.key.RIGHT:
            ans = 2
        if choice.random_answer() == ans-1:
            question+=1

 
if __name__ == '__main__':
    window = YouBetMeWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()