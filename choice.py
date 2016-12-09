class Choice:
    heart = 5000
    list = [[0,1],['YES','NO'],['BLACK','WHITE'],
            ['HEAD','TAIL'],['DAY','NIGHT'],['HOT','COLD'],
            ['AM','PM'],['HIGH','LOW'],['BIG','SMALL'],
            ['RIGHT','WRONG'],['GOOD','BAD'],['GET UP','GIVE UP']]
            
    def random_answer():
        return randint(0, 1)
