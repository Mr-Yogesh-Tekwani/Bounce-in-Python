from Surface import *
from Entry import *
from pygame.locals import *
from Ball import *
from Slots import *
from Label import *
from data_helper import *

class State:

    def __init__(self):
        pygame.init()
        self.s = Surface((0, 0), "Ball Fall", black)
        self.s.draw_surface()
        self.run_game = True
        self.score = 0
        self.d = database()

    def state_zero(self):
        state_zero = pygame.image.load('state_zero.bmp')
        start_button_parameters = Rect(370, 415, 210, 60) # It's kind of structure that holds the location and size of entity
        quit_button_parameters = Rect(770, 415, 210, 60)
        self.s.game_display.blit(state_zero, (0, 0)) # blit function is used to attach some text or image on the screen at given location
        self.s.refresh_background()
        while self.run_game:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if start_button_parameters.collidepoint(event.pos):
                        self.state_one()
                    elif quit_button_parameters.collidepoint(event.pos):
                        self.state_seven()
                if event.type == pygame.QUIT:
                    self.run_game = False
        pygame.quit()
        quit()

    def state_one(self):
        state_one = pygame.image.load('state_one.bmp')
        back_button_parameters = Rect(35, 610, 210, 60)
        next_button_parameters = Rect(925, 440, 110, 75)
        self.s.game_display.blit(state_one, (0, 0))
        e1 = Entry(440,445,440,50)
        e1.draw(self.s.game_display)
        self.s.refresh_background()
        while self.run_game:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if back_button_parameters.collidepoint(event.pos):
                        self.state_zero()
                    elif next_button_parameters.collidepoint(event.pos):
                        self.state_two(e1.text)
                    elif e1.entry.collidepoint(event.pos):
                        e1.active = not e1.active
                        # e1.type(event)
                    else:
                        e1.active = False
                if event.type == pygame.KEYDOWN:
                    e1.type(event)
                if event.type == pygame.QUIT:
                    self.run_game = False
            self.s.game_display.blit(state_one, (0, 0))
            e1.draw(self.s.game_display)
            pygame.display.update()
        pygame.quit()
        quit()

    def state_two(self,name,level=0):
        list=[]
        if level == 0:
            speed_x = 10
            speed_y = 4
        elif level == 1:
            speed_x = 15
            speed_y = 6
        elif level == 2:
            speed_x = 20
            speed_y = 10
        b1 = Ball(0, 50, 30, blue, fall=False)
        state_level = []
        state_level.append(pygame.image.load('state_two_level.bmp'))
        state_level.append(pygame.image.load('state_three_level.bmp'))
        state_level.append(pygame.image.load('state_four_level.bmp'))
        self.s.draw_surface()
        self.s.game_display.blit(state_level[level], (0, 0))
        slots = []
        for i in range(7):
            denominator = random.randint(-10,10)
            if denominator==0:
                denominator=-2
            x = random.randint(1,1000)% denominator
            list.append(x)
            slots.append(Slots(i*196,550,196*(i+1),550,x))
            slots[i].draw_slot(self.s)
        b1.draw_ball(self.s.game_display)
        flag = 0
        while self.run_game:
            for event in pygame.event.get():  # Iterating over list of events
                if event.type == pygame.QUIT:  # Clicked The Close Button at the top right
                    self.run_game = False
                elif event.type == pygame.KEYDOWN:  # Any Keyboard Key Is Pressed
                    if event.key == pygame.K_SPACE:  # Key value Is Matched With Space bar Key Value
                        b1.fall = True

            if not b1.fall:
                b1.move_along_x_axis(speed_x, 0, 1370)
            self.s.draw_surface()
            self.s.game_display.blit(state_level[level], (0, 0))
            b1.draw_ball(self.s.game_display)

            if b1.fall:
                b1.move_along_y_axis(speed_y, 715 - b1.radius)
                if b1.y_center < 550 - b1.radius:
                    b1.move_along_x_axis(speed_x, 0, 1370)
                else:
                    for i in range(7):
                        if slots[i].start_x <= b1.x_center <= slots[i].end_x and b1.y_center <= 715 - b1.radius:
                            b1.move_along_x_axis(speed_x, slots[i].start_x +5, slots[i].end_x - 5)
                            if flag == 0:
                                self.score += slots[i].number
                                flag = 1
                            break
            for i in range(7):
                slots[i].draw_slot(self.s)

            self.s.refresh_background()
            b1.refresh_ball()
            for i in range(7):
                slots[i].refresh_slot()
            if b1.y_center >= 715 - b1.radius and level == 0:
                self.state_three(name)
            if b1.y_center >= 715 - b1.radius and level == 1:
                self.state_four(name)
            if b1.y_center >= 715 - b1.radius and level == 2:
                self.state_five(name)

        pygame.quit()
        quit()

    def state_three(self,name):
        self.state_two(name,1)

    def state_four(self,name):
        self.state_two(name,2)

    def state_five(self,name):
        # print("{} Score is {}".format(name,self.score))
        state_five = pygame.image.load('state_five.bmp')
        yes_button_parameters = Rect(480, 335, 175,85)
        no_button_parameters = Rect(700, 335, 175, 85)
        self.s.game_display.blit(state_five, (0, 0))
        l_score=Label(self.score,800,160,label_score_green,75)
        l_score.draw_label(self.s)
        self.d.insert(name,self.score)
        self.s.refresh_background()
        while self.run_game:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if yes_button_parameters.collidepoint(event.pos):
                        self.score=0
                        self.state_two(name)
                    elif no_button_parameters.collidepoint(event.pos):
                        self.state_six(name)
                if event.type == pygame.QUIT:
                    self.run_game = False
        pygame.quit()
        quit()

    def state_six(self,name):
        state_six = pygame.image.load('state_six.bmp')
        play_again_button_parameters = Rect(340, 590, 230, 80)
        quit_button_parameters = Rect(790, 590, 230, 80)
        clear_button_parameters = Rect(1190,40,155,60)
        self.s.game_display.blit(state_six, (0, 0))
        maximum_score_players_tuple=self.d.get_max_score_players()
        maximum_score_players_name_list = []
        maximum_score_players_score_list = []
        count=0
        y=255
        for external_tuple in maximum_score_players_tuple:
            maximum_score_players_name_list.append(Label(external_tuple[0] , 515, y, white, 50))
            maximum_score_players_score_list.append(Label(str(external_tuple[1]), 770, y, white, 50))
            maximum_score_players_name_list[count].draw_label(self.s)
            maximum_score_players_score_list[count].draw_label(self.s)
            y+=70
            count+=1
            if count==4:
                break
        self.s.refresh_background()
        while self.run_game:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_again_button_parameters.collidepoint(event.pos):
                        self.state_two(name)
                    elif quit_button_parameters.collidepoint(event.pos):
                        self.state_seven()
                    elif clear_button_parameters.collidepoint(event.pos):
                        self.s.game_display.blit(state_six, (0, 0))
                        self.s.refresh_background()
                        self.d.clear_data()
                if event.type == pygame.QUIT:
                    self.run_game = False
        pygame.quit()
        quit()

    def state_seven(self):
        state_seven = pygame.image.load('state_seven.bmp')
        yes_button_parameters = Rect(436, 420, 210, 60)
        no_button_parameters = Rect(720, 415, 210, 60)
        self.s.game_display.blit(state_seven, (0, 0))
        self.s.refresh_background()
        while self.run_game:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if yes_button_parameters.collidepoint(event.pos):
                        self.run_game = False
                    elif no_button_parameters.collidepoint(event.pos):
                        self.state_zero()
                if event.type == pygame.QUIT:
                    self.run_game = False
        pygame.quit()
        quit()