class Horse:
    x_distance = 0
    sound = 'Frrr'
    def run(self, dx):
        self.dx = dx
        x_distance = self.x_distance + dx
        return x_distance
class Eagle:
    y_distance = 0
    sound = 'I train, eat, sleep, and repeat'
    def fly(self, dy):
        self.dy = dy
        y_distance = self.y_distance + dy
        return y_distance
class Pegasus(Eagle, Horse):
    def move(self, dx, dy):
        self.x_distance = super().run(dx)
        self.y_distance = super().fly(dy)
    def get_pos(self):
        return self.x_distance, self.y_distance
    def voice(self):
        print(self.sound)


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()