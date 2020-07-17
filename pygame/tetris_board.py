class Tetris_board():
    tetrislist = {
        "long":[
                [ '.1..',
                  '.1..',
                  '.1..',
                  '.1..'],
                [ '....',
                  '....',
                  '1111',
                  '....'] 
                ]
    }
    position = {'x':0,'y':0}

    def __init__(self, position):
        self.position['x'] = position['x']
        self.position['y'] = position['y']

    def gravity(self, key):  
        self.position['y']-=1

    def turnTetrist(self):
        pass