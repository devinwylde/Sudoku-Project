""" COP 3502c -- Project 4: Sudoku
---> GROUP 102 <---
Created by: Harper Fuchs, Blake Wood, Devin Wylde, and Maddy Wirbel
Due Date: December 6th, 2022 """

class ColorClass:
    # a class full of colors to make it easier to call a specific color value
    @property
    def White(self):
        return 255, 255, 255

    @property
    def Light_Gray(self):
        return 240, 232, 240

    @property
    def Dark_Gray(self):
        return 40, 32, 40

    @property
    def Black(self):
        return 0, 0, 0

    @property
    def Dark_Red(self):
        return 100, 0, 0
    # for example, the following lines save the color coordinates for light red
    @property
    def Light_Red(self):
        return 200, 100, 100

    @property
    def Light_Orange(self):
        return 214, 153, 88

    @property
    def Light_Yellow(self):
        return 237, 225, 116

    @property
    def Light_Green(self):
        return 100, 200, 100

    @property
    def Light_Blue(self):
        return 100, 100, 200
    # the following lines save the color coordinates for a purple/blue color
    @property
    def Purple_Blue(self):
        return 120, 104, 212

    @property
    def Light_Purple(self):
        return 237, 212, 240

    @property
    def Pink(self):
        return 247, 158, 199

    @property
    def Gray_Pink(self):
        return 209, 151, 177

    # Overlay "combines" two colors
    def Overlay(self, color, color2):
        result = [color[0], color[1], color[2]]
        for i in range(0, 3):
            result[i] -= (255 - color2[i])
        return result[0], result[1], result[2]

    def Darken(self, color):
        return color[0] - (255-color[0]) * 0.1, color[1] - (255-color[1]) * 0.1, color[2] - (255-color[2]) * 0.1

    def Lighten(self, color):
        return color[0] + (255-color[0]) * 0.1, color[1] + (255-color[1]) * 0.1, color[2] + (255-color[2]) * 0.1