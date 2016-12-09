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
        if (not self.world.is_ans):
            arcade.draw_text(str(self.world.bet), 400, 180, arcade.color.RED, 20)
        if (self.world.is_ans):
            arcade.draw_text(str(self.world.bet), 400, 180, arcade.color.BLACK, 20)

    def on_key_press(self, key, key_modifiers):
        right_choice = self.choice.random_answer()
        self.world.on_key_press(key, key_modifiers, right_choice)

class World():
    def __init__(self):
        self.heart = 5000
        self.question = 1
        self.ans = 0
        self.input = ''
        #self.num_key = {48:'0', 49:'1', 50:'2', 51:'3', 52:'4', 53:'5', 54:'6', 54:'7', 56:'8', 57:'9'}
        self.num_key = {48:0, 49:1, 50:2, 51:3, 52:4, 53:5, 54:6, 55:7, 56:8, 57:9}
        self.bet = 0
        self.is_ans = False
        self.tmp = 0

    def on_key_press(self, key, key_modifiers, right_choice):
        if key == arcade.key.LEFT and self.is_ans:
            self.ans = 1
            self.check_ans(right_choice)
        if key == arcade.key.RIGHT and self.is_ans:
            self.ans = 2
            self.check_ans(right_choice)
        if key == arcade.key.BACKSPACE:
            self.convert_input(False, tmp)
        if 48 <= key <= 57:
            tmp = self.num_key[key]
            self.convert_input(True, tmp)
        if int(self.bet) >= 2000:
            self.is_ans = True

    def reset(self):
        self.ans = 0
        self.input = ''
        self.is_ans = False
        self.bet = 0
        self.tmp = 0

    def check_ans(self, right_choice):
        if (self.ans == right_choice):
            self.heart += self.bet
            self.question += 1
        if (self.ans != right_choice):
            self.heart -= self.bet
        self.reset()

    def convert_input(self, is_value, value):
        if not is_value:
            self.bet = (self.bet-value)/10
        else:
            self.bet = self.bet*10+value



 
if __name__ == '__main__':
    window = YouBetMeWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()