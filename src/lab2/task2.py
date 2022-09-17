from typing import Tuple


class Rational:
    def __init__(self, numerator: int = 1, denominator: int = 1) -> None:
        self._numerator, self._denominator = self.compute_fractions(numerator, denominator)

    def compute_fractions(self, numerator: int, denominator: int) -> Tuple[int, int]:
        max_value = max(numerator, denominator)
        for common_divisor in reversed(range(max_value)):
            if numerator % common_divisor == 0 and denominator % common_divisor == 0:
                return int(numerator / common_divisor), int(denominator / common_divisor)
        return numerator, denominator

    def __str__(self) -> str:
        return f"{self._numerator}/{self._denominator}"
    
    def convert2float(self) -> float:
        return self._numerator / self._denominator


if __name__ == "__main__":
    fraction = Rational(2, 4)
    print(fraction)
    print(fraction.convert2float())