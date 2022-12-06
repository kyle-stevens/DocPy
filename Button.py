import pygame

class Button:
    button_area : pygame.Rect
    button_position : (int, int)

    def __init__(self, button_area, button_position):
        self.button_position = button_position
        self.button_area = button_area

    def detect(self, event_location : (int, int)):
        return self.button_area.collidepoint(event_location)

class ToggleButton(Button):
    selected : bool = False
    selected_sprite : str
    unselected_sprite : str

    def __init__(self, button_area, button_position):
        super.__init__(button_area, button_position)

    def detect(self, event_location : (int, int)):
        if super.detect(event_location):
            self.selected = not self.selected


    def get_status(self):
        return self.selected
