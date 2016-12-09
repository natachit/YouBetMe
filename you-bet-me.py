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
        arcade.draw_text(str(self.world.heart),
                         10, self.height - 30,
                         arcade.color.BLACK, 20)
        arcade.draw_text(str(self.choice.list[self.world.question-1][0]),
                         305, 325, arcade.color.BLACK, 30, width=223, align="center",
                         anchor_x="center", anchor_y="center")
        arcade.draw_text(str(self.choice.list[self.world.question-1][1]),
                         545, 325, arcade.color.BLACK, 30, width=223, align="center",
                         anchor_x="center", anchor_y="center")
        arcade.draw_text(str(self.world.input), 10, 10,
                         arcade.color.BLACK, 20)

    def on_key_press(self, key, key_modifiers):
        choice = self.choice.random_answer()
        self.world.on_key_press(key, key_modifiers, choice)

class World():
    def __init__(self):
        self.heart = 5000
        self.question = 1
        self.ans = 0
        self.input = ''
        self.num_key = {48:'0', 49:'1', 50:'2', 51:'3', 52:'4',
                        53:'5', 54:'6', 54:'7', 56:'8', 57:'9'}
        self.bet = 0

    def on_key_press(self, key, key_modifiers, choice):
        if key == arcade.key.LEFT:
            self.ans = 1
        if key == arcade.key.RIGHT:
            self.ans = 2
        if choice == self.ans - 1:
            self.question += 1
        if key == arcade.key.BACKSPACE:
            self.input = self.input[:-1]
        if 48 <= key <= 57:
            tmp = str(self.num_key[key])
            self.input += tmp
            self.bet = 0
            
        #else:
           # self.input += str(key)



 
if __name__ == '__main__':
    window = YouBetMeWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()