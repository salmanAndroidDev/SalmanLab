class Structure:
    def __init__(self, height, width):
        self.__height = height
        self.__width = width

    def set_height_and_width(self, height, width):
        self.__height = height
        self.__width = width

    def getHieght(self):
        return self.__height

    def getWidth(self):
        return self.__width



