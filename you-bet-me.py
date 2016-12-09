import arcade
 
SCREEN_WIDTH = 850
SCREEN_HEIGHT = 600
 
class YouBetMeWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
 
        arcade.set_background_color(arcade.color.WHITE)
        self.box = arcade.Sprite('images/box.png')
        self.box.set_position(305, 325)
        self.box2 = arcade.Sprite('images/box.png')
        self.box2.set_position(545, 325)
 
 
    def on_draw(self):
        arcade.start_render()
        self.box.draw()
        self.box2.draw()
 
 
if __name__ == '__main__':
    window = YouBetMeWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()