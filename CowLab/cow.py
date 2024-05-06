# Lab 07: The Cow Says... (2)

class Cow:
    def __init__(self, name):
        self.cow_name = name
        self.name = None
        self.image = None

    def get_name(self):
        self.name = self.cow_name
        return self.name

    def get_image(self):
        return self.image

    def set_image(self, image):
        pass

    