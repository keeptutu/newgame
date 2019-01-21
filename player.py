class Player():
    def __init__(self, name):
        self.name = name
        self.pos = 0

    def show_player(self, screen, selfimg):
        xy = (262,0)
        if self.pos == 0:
            xy = (262, 0)
        elif self.pos == 1:
            xy = (438, 0)
        elif self.pos == 2:
            xy = (540, 0)
        elif self.pos == 3:
            xy = (642, 0)
        elif self.pos == 4:
            xy = (744, 0)
        elif self.pos == 5:
            xy = (846, 0)
        elif self.pos == 6:
            xy = (948, 0)
        elif self.pos == 7:
            xy = (1050, 0)
        elif self.pos == 8:
            xy = (1152, 0)
        elif self.pos == 9:
            xy = (1186, 174)
        elif self.pos == 10:
            xy = (1186, 276)
        elif self.pos == 11:
            xy = (1186, 378)
        elif self.pos == 12:
            xy = (1186, 480)
        elif self.pos == 13:
            xy = (1186, 582)
        elif self.pos == 14:
            xy = (1152, 684)
        elif self.pos == 15:
            xy = (1050, 718)
        elif self.pos == 16:
            xy = (948, 718)
        elif self.pos == 17:
            xy = (846, 718)
        elif self.pos == 18:
            xy = (744, 718)
        elif self.pos == 19:
            xy = (642, 718)
        elif self.pos == 20:
            xy = (540, 718)
        elif self.pos == 21:
            xy = (438, 718)
        elif self.pos == 22:
            xy = (262, 684)
        elif self.pos == 23:
            xy = (262, 582)
        elif self.pos == 24:
            xy = (262, 480)
        elif self.pos == 25:
            xy = (262, 378)
        elif self.pos == 26:
            xy = (262, 276)
        elif self.pos == 27:
            xy = (262, 174)

        screen.blit(selfimg,xy)

    def move(self,n):
        for i in range(n):
            if self.pos > 27:
                self.pos -= 26
            else:
                self.pos += 1
