from PyQt5.QtCore import Qt,QPoint
class GO:
    def __init__(self):
        self.G_map=[[0 for i in range(15)] for j in range(15)]
        self.step_count = 0
    def move(self):
        while True:
            try:
                p_x=int(input('x:'))
                p_y=int(input('y:'))
                if 0 <= p_x <= 14 and 0 <= p_y <= 14:
                    if self.G_map[p_x][p_y] == 0:
                        self.G_map[p_x][p_y] = 1
                        self.step_count += 1
                        return
            except ValueError:
                continue

    def result(self):
        for x in range(15):
            for y in range(15):
                if self.G_map[x][y] == 1:
                    if self.G_map[x+1][y]==1 and self.G_map[x+2][y]==1 and self.G_map[x+3][y]==1 and self.G_map[x+4][y]==1:
                        return 1
                    elif self.G_map[x+1][y+1]==1 and self.G_map[x+2][y+2]==1 and self.G_map[x+3][y+3]==1 and self.G_map[x+4][y+4]==1:
                        return 1
                    elif self.G_map[x][y+1]==1 and self.G_map[x][y+2]==1 and self.G_map[x][y+3]==1 and self.G_map[x][y+4]==1:
                        return 1

    def GO_AI(self):
        for x in range(15):
            for y in range(15):
                if self.G_map[x][y] == 0:
                    self.G_map[x][y] = 2
                    self.step_count += 1
                    return

    def show_map(self):
        for i in self.G_map:
            print(i)

    def play(self):
        while True:
            self.move()
            self.GO_AI()
            self.show_map()
            res = self.result()
            if res == 1:
                print('win')
            

class go_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        pass

    def drawele(self,e):
        def draw_map(self):
            pass
            
        def draw_check():
            pass
    
    def mous(self,e):


def main():
    g = GO()
    g.play()

if __name__ == '__main__':
    main()