class Wall:
    armor = 10
    height = 5

    # write your code here

    def foritify(self):
        self.armor *= 2


wall1 = Wall()
wall1.foritify()
print(wall1.armor)