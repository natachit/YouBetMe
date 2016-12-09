import arcade
import arcade.key
from choice import Choice
 
SCREEN_WIDTH = 850
SCREEN_HEIGHT = 600
BOX_POS = [[305,325],[545, 325]]
 
class YouBetMeWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.choice = Choice()
        self.world = World()
 
        arcade.set_background_color(arcade.color.WHITE)
        self.box_img = arcade.Sprite('images/box.png')
        self.box_img.set_position(BOX_POS[0][0], BOX_POS[0][1])
        self.box2_img = arcade.Sprite('images/box.png')
        self.box2_img.set_position(BOX_POS[1][0], BOX_POS[1][1])
        self.heart_img = arcade.Sprite('images/heart1.png')
        self.heart_img.set_position(30, 575)
        self.heart2_img = arcade.Sprite('images/heart1.png')
        self.heart2_img.set_position(350, 190)
        self.right_choice = 0
 

    def on_draw(self):
        arcade.start_render()
        check_render = self.world.is_ans
        self.box_img.draw()
        self.box2_img.draw()
        self.heart_img.draw()
        self.heart2_img.draw()
        arcade.draw_text(str(self.world.heart),
                         60, self.height - 35,
                         arcade.color.BLACK, 20)
        arcade.draw_text(str(self.choice.list[self.world.question-1][0]),
                         305, 325, arcade.color.BLACK, 30, width=223, align="center",
                         anchor_x="center", anchor_y="center")
        arcade.draw_text(str(self.choice.list[self.world.question-1][1]),
                         545, 325, arcade.color.BLACK, 30, width=223, align="center",
                         anchor_x="center", anchor_y="center")
        if not self.world.can_ans:
            arcade.draw_text(': '+str(self.world.bet), 380, 180, arcade.color.RED, 20)
            
        if self.world.can_ans:
            arcade.draw_text(': '+str(self.world.bet), 380, 180, arcade.color.BLACK, 20)

        if check_render[0]:
            if check_render[1]:
                self.ans_img = arcade.Sprite('images/right.png')
                arcade.draw_text("Correct! You got "+str(self.world.bet)+" hearts",
                         420, 450, arcade.color.BLACK, 30, width=1000, align="center",
                         anchor_x="center", anchor_y="center")

            if not check_render[1]:
                self.ans_img = arcade.Sprite('images/wrong.png')
                arcade.draw_text("Wrong! You lose "+str(self.world.bet)+" hearts",
                         420, 450, arcade.color.RED, 30, width=1000, align="center",
                         anchor_x="center", anchor_y="center")
            #arcade.draw_text(str(self.right_choice),100,100,arcade.color.BLACK, 20)     #print right answer
            self.ans_img.set_position(BOX_POS[check_render[2]][0], BOX_POS[check_render[2]][1])
            self.ans_img.draw()

        if not self.world.can_ans:
            if self.world.bet < 2000:
                arcade.draw_text('Too low',380,130,arcade.color.RED, 15)
            if self.world.bet > self.world.heart:
                arcade.draw_text('Too high',380,130,arcade.color.RED, 15)


    def on_key_press(self, key, key_modifiers):
        self.right_choice = self.choice.random_answer()
        self.world.on_key_press(key, key_modifiers, self.right_choice)



class World():
    def __init__(self):
        self.heart = 5000
        self.question = 1
        self.ans = 0
        self.num_key = {48:0, 49:1, 50:2, 51:3, 52:4, 53:5, 54:6, 55:7, 56:8, 57:9}
        self.bet = 0
        self.can_ans = False
        self.tmp = 0
        self.is_ans = [False, None, 0]    #false=not answer yet, None=right or wrong, 0=right choice


    def on_key_press(self, key, key_modifiers, right_choice):
        if key == arcade.key.C and self.can_ans and not self.is_ans[0]:
            self.ans = right_choice
            self.check_ans(right_choice)

        if key == arcade.key.V and self.can_ans and not self.is_ans[0]:
            if right_choice == 1:
                self.ans = 2
            if right_choice == 2:
                self.ans = 1
            self.check_ans(right_choice)

        if key == arcade.key.LEFT and self.can_ans and not self.is_ans[0]:
            self.ans = 1
            self.check_ans(right_choice)

        if key == arcade.key.RIGHT and self.can_ans and not self.is_ans[0]:
            self.ans = 2
            self.check_ans(right_choice)

        if key == arcade.key.BACKSPACE and not self.is_ans[0]:
            self.convert_input(False, self.tmp)

        if 48 <= key <= 57 and not self.is_ans[0]:
            self.tmp = self.num_key[key]
            self.convert_input(True, self.tmp)

        #if 2000 <= self.bet and not self.is_ans[0]:
        #   if self.bet <= self.heart:
    #        self.can_ans = True

        if key == arcade.key.ENTER and self.is_ans[0]:
            self.reset()


    def reset(self):
        self.ans = 0
        self.can_ans = False
        self.bet = 0
        self.question += 1
        self.is_ans = [False, None, 0] 


    def check_ans(self, right_choice):
        if (self.ans == right_choice):
            self.heart += self.bet
            self.is_ans = [True, True, self.ans-1]
        if (self.ans != right_choice):
            self.heart -= self.bet
            self.is_ans = [True, False, self.ans-1]


    def convert_input(self, is_value, value):
        if not is_value:
            self.bet = int((self.bet-value)/10)
        if is_value:
            self.bet = int(self.bet*10+value)
        if self.heart >= self.bet >= 2000:
            self.can_ans = True
        else: 
            self.can_ans = False


 
if __name__ == '__main__':
    window = YouBetMeWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()