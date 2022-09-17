class Rectangle:
    MAX_SIZE = 20

    def __init__(self) -> None:
        self._length = 1
        self._width = 1

    @property
    def length(self) -> int | float:
        return self._length

    @length.setter
    def length(self, new_length: int | float) -> None:
        if new_length > 0 and new_length < self.MAX_SIZE:
            self._length = new_length
        raise ValueError(f"Error: length have to be greater than 0 and less than {self.MAX_SIZE}.")

    @property
    def width(self) -> int | float:
        return self._width

    @width.setter
    def width(self, new_width: int | float) -> int | float: 
        if new_width > 0 and new_width < self.MAX_SIZE:
            self._width = new_width
        raise ValueError(f"Error: width have to be greater than 0 and less than {self.MAX_SIZE}.")

    @property
    def perimeter(self) -> int | float:
        return 2 * (self._length + self._width)

    @property
    def area(self) -> int | float:
        return self._length * self._width