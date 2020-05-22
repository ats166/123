print(__name__)

class woman():

    def create(name, height, weight, iq):
        person = woman()
        person.name = name
        person.weight = weight
        person.height = height
        person.iq = iq

        return person

    def eat(self):
        self.weight += 3

        print("{} After Eat, Weight = {}kg Height = {}cm IQ = {} ".format(self.name, self.weight, self.height, self.iq))

    def sleep(self):
        self.height += 1

        print("{} After Eat, Weight = {}kg Height = {}cm IQ = {}".format(self.name,self.weight, self.height, self.iq))

    def study(self):
        self.iq += 5

        print("{} After Eat, Weight = {}kg Height = {}cm IQ = {} ".format(self.name, self.weight, self.height, self.iq))