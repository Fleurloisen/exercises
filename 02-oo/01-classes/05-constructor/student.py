class Wall():
    def __init__(self, depth, height, width, volume):
        self.depth = depth
        self.height = height
        self.width = width
        self.volume = self.width * self.height * self.depth

    
wall1 = Wall( 5, 9, 4,'')
print(wall1.volume)
