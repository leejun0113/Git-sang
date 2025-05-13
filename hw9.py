class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle():
    def __init__(self, x1, x2, y1, y2):
        self.__lt = Point(x1, x2)
        self.__rb = Point(y1, y2)

    def show(self):
        print(f'좌측 상단 꼭지점이 ({self.__lt.x}, {self.__lt.y})이고 우측 하단 꼭지점이 ({self.__rb.x}, {self.__rb.y})인 사각형입니다.', end='')

    def getWidth(self):
        return self.__rb.x - self.__lt.x

    def getHeight(self):
        return self.__rb.y - self.__lt.y

    def getArea(self):
        return self.getWidth() * self.getHeight()

    def getPerimeter(self):
        return 2 * (self.getWidth() + self.getHeight())

r1 = Rectangle(5, 5, 20, 10)
a = r1.getArea()
p = r1.getPerimeter()
r1.show()
print(f'\n넓이는 {a}, 둘레는 {p}')