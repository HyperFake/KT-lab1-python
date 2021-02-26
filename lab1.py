class File_Reader:
    def __init__(self, file_Name):
        self.__file_Name = file_Name

    def read(self):
        with open(self.__file_Name) as f:
            lines = f.read().splitlines()
            return lines

class File_Writer:
    def __init__(self, file_Name):
        self.__file_Name = file_Name

    def write(self, numbers):
        f = open(self.__file_Name,"w")
        for i in numbers:
            f.write(i+"\n")
        f.close()


class Squares_Calculator:
    def __init__(self, lines):
        self.lines = lines

    def get_length(self, number):
        __value = 9
        for i in range(number // 2 - 1):
            __value = __value * 10 + 9
        return __value

    def squares_finder(self, number):
        __squares = []
        __length = self.get_length(int(number))
        for first in range(__length+1):
            for second in range(__length+1):
                __number = pow(first + second, 2)
                __result = int(str(first) + str(second))
                if (len(str(first))+len(str(second))) == int(number) : 
                    if __number == __result :
                        __squares.append(str(first)+str(second))
            
                second += 1
            first += 1
        return __squares        

    def find_numbers(self):
        arr = []
        for i in lines:
            __temp = self.squares_finder(i)
            for j in __temp:
                arr.append(j)
        return arr
    

Reader = File_Reader("lab1.txt")
lines = Reader.read()

Square = Squares_Calculator(lines)
numbers = Square.find_numbers()

Writer = File_Writer("lab1_results.txt")
Writer.write(numbers)