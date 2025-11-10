import re


class Lesson:
    def __init__(self, code, name, teacher, unit):
        self.code = code
        self.name = name
        self.teacher = teacher
        self.unit = unit



    def is_valid(self):
        if not re.match("^[0-9]{1,4}$",str(self.code)):
            raise ValueError("Invalid lesson code!!!")

        if not re.match("^[a-zA-Z\s]{3,30}$",self.name):
            raise ValueError("invalid lesson name!!!")

        if not re.match("^[a-zA-Z\s]{3,30}$", self.teacher):
            raise ValueError("invalid teacher name!!!")

        if not (type(self.unit) == int and self.unit in [1,2,3,5]):
            raise ValueError("invalid unit!!!")

        return True

    def to_tuple(self):
        return tuple((self.code, self.name, self.teacher, self.unit))

