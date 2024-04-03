#!/usr/bin/python3


class Square:
    def __init__(self, size=0, position=(0, 0)):
        if self.__validate_size(size):
            self.__size = size
        if self.__validate_pos(position):
            self.__position = position
    def size(self):
        return self.__size
    def size(self, value):
        if self.__validate_size(value):
            self.__size = value
    def position(self):
        return self.__position
    def position(self, value):
        if self.__validate_pos(value):
            self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        i = 0
        if self.__size == 0:
            print()
            return
        for i in range(0, self.__position[1]):
            print()
        i = 0
        for i in range(0, self.__size):
            j = 0
            x_pad = 0
            for x_pad in range(0, self.__position[0]):
                print(" ", end='')
            for j in range(0, self.__size):
                print("#", end='')
            print()

    def __validate_size(self, size):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            return True
        return False

    def __validate_pos(self, position):
        if not isinstance(position, type((0, 0))):
            raise TypeError("position must be a tuple of 2 positive integers")
            return False
        return True
