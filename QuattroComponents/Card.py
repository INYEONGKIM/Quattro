class Card:
    card_type = ['red', 'blue', 'yellow', 'green', 'zero']

    def __init__(self, color, number, isOpen):
        if 0 <= number <= 6 and color in self.card_type and isOpen in (True, False):
            self.color = color
            self.number = number
            self.isOpen = isOpen
        else:
            raise AssertionError("None Correct Type Card Input")

    def __str__(self):
        return f'{self.color} {self.number} {self.isOpen}'
