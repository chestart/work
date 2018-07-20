class Student(object):
    @property
    def get_score(self):
        return self._score

    @get_score.setter
    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer')
        if value < 0 or value > 100:
            raise ValueError('score must between 0-100')
        self._score = value

a = Student()
a.set_score = 435
print a.get_score

