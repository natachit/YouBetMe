import arcade
import arcade.key
import arcade.sound
from random import randint
 
SCREEN_WIDTH = 750
SCREEN_HEIGHT = 500
BOX_POS = [[255,275],[495, 275]]
 
class YouBetMeWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.choice = Choice()
        self.world = World()
        arcade.set_background_color(arcade.color.BLACK)
        self.box_img = arcade.Sprite('images/box.png')
        self.box_img.set_position(BOX_POS[0][0], BOX_POS[0][1])
        self.box2_img = arcade.Sprite('images/box.png')
        self.box2_img.set_position(BOX_POS[1][0], BOX_POS[1][1])
        self.coin_img = arcade.Sprite('images/coin.png')
        self.coin_img.set_position(30, 475)
        self.coin2_img = arcade.Sprite('images/coin.png')
        self.coin2_img.set_position(300, 140)
        self.right_choice = 0
        self.time = 0


    def on_draw(self):
        arcade.start_render()
        end_status = self.world.end_status
        check_render = self.world.is_ans
        self.bg_img = arcade.Sprite(self.world.bg_pix)
        self.bg_img.set_position(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        self.bg_img.draw()
        if end_status == 0:
            if (self.time >= 320):
                self.world.play_bgsound()
                self.time = 0
            else:
                self.time += 1
            self.box_img.draw()
            self.box2_img.draw()
            self.coin2_img.draw()
            arcade.draw_text(str(self.choice.list[self.world.question-1][0]),
                            BOX_POS[0][0], BOX_POS[0][1], arcade.color.BLACK, 30, width=223, align="center",
                            anchor_x="center", anchor_y="center")
            arcade.draw_text('Press Left Key',
                            BOX_POS[0][0], BOX_POS[0][1]-55, arcade.color.GRAY, 12, width=223, align="center",
                            anchor_x="center", anchor_y="center")
            arcade.draw_text(str(self.choice.list[self.world.question-1][1]),
                            BOX_POS[1][0], BOX_POS[1][1], arcade.color.BLACK, 30, width=223, align="center",
                            anchor_x="center", anchor_y="center")
            arcade.draw_text('Press Right Key',
                            BOX_POS[1][0], BOX_POS[1][1]-55, arcade.color.GRAY, 12, width=223, align="center",
                            anchor_x="center", anchor_y="center")
            if not self.world.can_ans:
                arcade.draw_text(': '+str(self.world.bet), 330, 130, arcade.color.RED, 20)
                
            if self.world.can_ans:
                arcade.draw_text(': '+str(self.world.bet), 330, 130, arcade.color.BLACK, 20)

            if check_render[0]:
                if check_render[1]:
                    self.ans_img = arcade.Sprite('images/right.png')
                    arcade.draw_text("Correct! You got "+str(self.world.bet)+" coins",
                            370, 400, arcade.color.BLACK, 30, width=1000, align="center",
                            anchor_x="center", anchor_y="center")

                if not check_render[1]:
                    self.ans_img = arcade.Sprite('images/wrong.png')
                    arcade.draw_text("Wrong! You lose "+str(self.world.bet)+" coins",
                            370, 400, arcade.color.RED, 30, width=1000, align="center",
                            anchor_x="center", anchor_y="center")
                self.ans_img.set_position(BOX_POS[check_render[2]][0], BOX_POS[check_render[2]][1])
                self.ans_img.draw()
                arcade.draw_text('Press Enter to continue',250,80,arcade.color.GRAY, 15)

            if not self.world.can_ans:
                if self.world.bet < 2000:
                    arcade.draw_text('( min '+str(self.world.check_coin())+' )',300,100,arcade.color.RED, 13)
                if self.world.bet > self.world.coin:
                    arcade.draw_text('  ( Too high )',300,100,arcade.color.RED, 13)
                    
        self.coin_img.draw()
        arcade.draw_text(str(self.world.coin),60, self.height - 35, arcade.color.WHITE, 20)

        if end_status != 0:
            self.world.play_endsound(True)
            self.world.is_ans[0] = True
            if self.world.is_restart == True:
                self.world = World()
            arcade.draw_text('Press Enter to play again',230, 20, arcade.color.GRAY, 18)
            if end_status == 1:
                arcade.draw_text('You are a billionaire!!!',85, 250, arcade.color.WHITE, 40)
            if end_status == 2:
                arcade.draw_text('Oop! You go bankrupt!',65, 250, arcade.color.WHITE, 40)
            if end_status == 3:
                arcade.draw_text('You are a commoner',105, 250, arcade.color.BLACK, 40)


    def on_key_press(self, key, key_modifiers):
        self.right_choice = self.choice.random_answer()
        self.world.on_key_press(key, key_modifiers, self.right_choice)



class Choice:
    list = [['0','1'],['YES','NO'],['BLACK','WHITE'],
            ['HEAD','TAIL'],['DAY','NIGHT'],['HOT','COLD'],
            ['AM','PM'],['HIGH','LOW'],['BIG','SMALL'],
            ['RIGHT','WRONG'],['GOOD','BAD'],['GET UP','GIVE UP']]

    def random_answer(self):
        #return 1
        return randint(0, 1) + 1



class World():
    def __init__(self):
        self.choice = Choice()
        self.coin = 5000
        self.question = 1
        self.ans = 0
        self.num_key = {48:0, 49:1, 50:2, 51:3, 52:4, 53:5, 54:6, 55:7, 56:8, 57:9}
        self.bet = 0
        self.can_ans = False
        self.tmp = 0
        self.is_ans = [False, None, 0]    #false=not answer yet, None=right or wrong, 0=right choice
        self.end_status = 0
        self.is_restart = False
        self.coin_max = self.check_coin
        self.bg_pix = 'images/bg.png'
        self.theme_sound = arcade.sound.load_sound('sounds/theme sound.wav')
        arcade.sound.play_sound(theme_sound)
        self.end_sound = arcade.sound.load_sound('sounds/end.wav')


    def on_key_press(self, key, key_modifiers, right_choice):
        if key == arcade.key.A:
            self.coin = 50000
            self.check_ans(right_choice)

        if key == arcade.key.S:
            self.coin = 0
            self.check_ans(right_choice)

        if key == arcade.key.D:
            self.question = len(self.choice.list)
            self.check_ans(right_choice)

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

        if key == arcade.key.ENTER and self.is_ans[0]:
            if self.end_status != 0:
                self.play_endsound(False)
                self.reset_hard()
            else:
                self.reset()


    def reset(self):
        self.ans = 0
        self.can_ans = False
        self.bet = 0
        self.question += 1
        self.is_ans = [False, None, 0]


    def check_ans(self, right_choice):
        if self.ans == right_choice:
            self.coin += self.bet
            self.is_ans = [True, True, self.ans-1]

        if self.ans != right_choice:
            self.coin -= self.bet
            self.is_ans = [True, False, self.ans-1]

        if self.coin >= 30000:
            self.end_status = 1
            self.bg_pix = 'images/bg_billion.png'

        if self.coin <= 0:
            self.end_status = 2
            self.bg_pix = 'images/bg_bankrupt.png'

        if self.question >= len(self.choice.list):
            self.end_status = 3
            self.bg_pix = 'images/bg_common.png'


    def convert_input(self, is_value, value):
        x = self.check_coin()
        if not is_value:
            self.bet = int((self.bet-value)/10)

        if is_value:
            self.bet = int(self.bet*10+value)

        if self.coin >= self.bet >= x:
            self.can_ans = True

        else: 
            self.can_ans = False


    def reset_hard(self):
        self.is_restart = True


    def check_coin(self):
        if self.coin >= 3000:
            self.coin_max = 2000
        
        if 2500 <= self.coin < 3000:
            self.coin_max = 1500

        if 2000 <= self.coin < 2500:
            self.coin_max = 1000

        if self.coin < 2000:
            self.coin_max = 500

        return self.coin_max

    
    def play_bgsound(self):
        theme_sound.pause()
        arcade.sound.play_sound(theme_sound)


    def play_endsound(self, true):
        if (true):
            theme_sound.pause()
            arcade.sound.play_sound(end_sound)
        else
            end_sound.pause()

 
if __name__ == '__main__':
    window = YouBetMeWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()