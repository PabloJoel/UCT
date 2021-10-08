import pygame

class Button:
 
    def __init__(self, text, col, row, width, height, font, color, bg="black"):
        #Create rectangle
        self.col, self.row = col,row
        self.width, self.height = width,height
        self.rect = pygame.Rect(col, row, width, height)

        #Text to display
        self.font = font
        self.text = font.render(text, True, color)
        
        #Text color and background color
        self.color = color
        self.background_color = bg
        
    def show(self, screen):
        pygame.draw.rect(screen, self.background_color, self.rect, 0)
        screen.blit(self.text, (self.col, self.row))
 
    def click_on_button(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.mouse_on_button():
                    return 1
        return 0
 
    def mouse_on_button(self):
        col, row = pygame.mouse.get_pos()
        if self.rect.collidepoint(col, row):
            return 1
        else:
            return 0