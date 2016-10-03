# -*- coding: cp1252 -*-
import render, constants;

class figure:
       ###Kommentiert###
    imgs, pos, frame, isJumping, y, x, yVel, canJump = [], 0, 1, False, constants.Y_FLOOR, constants.PLAYER_X, 0, True;
    
    def jump(self):
        if not self.isJumping and self.canJump and render.jumpsLeft >=1:
                if render.settings.sounds_enabled:
                    render.pygame.mixer.Sound.play(constants.PLAYER_JUMP_SOUND);
                self.yVel = -25;
                self.isJumping = True;
                render.jumpsLeft -=1;

    def jumpMove(self, bottom, gravity):
            if self.isJumping:
                self.yVel += gravity;
                self.y += self.yVel;
                if self.y > bottom:
                    self.y = bottom;
                    self.yVel = 0;
                    self.isJumping = False;
            else:
                if not self.y == bottom:
                    self.yVel += gravity;
                    self.y += self.yVel;
                    if self.y > bottom:
                        self.y = bottom;
                        self.yVel = 0;
                    
    def jumpMove2(self, bottom, gravity):
            if self.isJumping:
                self.yVel += gravity;
                self.y += self.yVel;
                if self.y+constants.RESIZE_PLAYER[1]> bottom:
                    self.y = bottom-constants.RESIZE_PLAYER[1]-5;
                    self.yVel = 0;
                    self.isJumping = False;
                    
    def gravity(self):
        if render.intern_object == None:
             self.jumpMove(constants.Y_FLOOR, constants.GRAVITY);
        else:
            self.jumpMove2(render.intern_object.bb[1], constants.GRAVITY);
            
    def move(self, screen, stand):
        if not stand:
            self.gravity();
        #Packe ein Bisschen Delay zwischen den einzelnen AnimationsFrames.
        if self.frame == 1:
            self.pos +=1;
        self.frame += 1;
        if self.frame > 3:
            self.frame=1;
        #Resette die Animation, wenn pos größer als maximale Länge
        if self.pos >=(len(self.imgs)):
            self.pos = 0;
        #Gib das Bild an.
        #250 X POS
        screen.blit(self.imgs[self.pos], (self.x, self.y));
    ###Ende Kommentiert###
        
    def isVisible(self):
        if self.x+10 < 0:
            return False;
        if self.x+render.RESIZE_PLAYER[0]-10 > render.WIDTH:
            return False;
        return True;
        
    def __init__(self, pics):
        self.imgs = pics;
 
