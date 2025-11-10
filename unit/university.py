class SumUnit:
    def __init__(self, lesson_id):
        self.lesson_id = lesson_id
        self.lesson_list = []

    def add_unit(self, lesson):
        self.lesson_list.append(lesson)

    def total_unit(self):
        if not self.lesson_list:
            raise ValueError("Empty")

        total = 0
        for lesson in self.lesson_list:
            total += lesson.unit
        return total