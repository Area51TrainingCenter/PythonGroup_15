class Fraction:

    def __init__(self, num, den):
        self.den = den
        self.num = num

    def to_decimal(self):
        dec = self.num / self.den
        return "{:.3f}".format(dec)

    def get_reduced_shape(self):
        gcd = self._gcd2(self.num, self.den)
        num = self.num // gcd
        den = self.den // gcd
        return Fraction(num, den)

    def _gcd(self, a, b):
        if a < b:
            a, b = b, a
        if b == 0:
            return a
        return self.gcd(b, a - b)

    def _gcd2(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a % b)

    def product(self, other):
        num = self.num * other.num
        den = self.den * other.den
        return Fraction(num, den)

    def __mul__(self, other):
        num = self.num * other.num
        den = self.den * other.den
        return Fraction(num, den)

    def addition(self, other):
        num = self.num * other.den + other.num * self.den
        den = self.den * other.den
        return Fraction(num, den)

    def __add__(self, other):
        num = self.num * other.den + other.num * self.den
        den = self.den * other.den
        return Fraction(num, den)

    def __lt__(self, other):
        return self.num * other.den < self.den * other.num

    def show(self):
        print("{}/{}".format(self.num, self.den))

    def __str__(self):
        return "{}/{}".format(self.num, self.den)

    def __repr__(self):
        return self.__str__()


fraction1 = Fraction(5, 10)
fraction1.show()
print(fraction1.to_decimal())
fraction2 = fraction1.get_reduced_shape()
fraction2.show()
# fraction3 = fraction2.product(fraction1)
fraction3 = fraction2 * fraction1
fraction3.show()
# fraction4 = fraction2.addition(fraction1)
fraction4 = fraction2 + fraction1
fraction4.show()
print(fraction4)
lf = [fraction1, fraction2, fraction3, fraction4]
print(list(map(lambda f: f.to_decimal(), lf)))
lf.sort()
print(list(map(lambda f: f.to_decimal(), lf)))
