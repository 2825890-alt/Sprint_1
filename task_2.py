class Tester:

    def __init__(self, name, has_deadline=True):
        self.name = name
        self.deadline = has_deadline

    def work_hard(self):
        if self.deadline:
            print(f'{self.name}, Что ж, ещё часок поработаю!')
        else:
            print(f'{self.name}, Можно отдыхать')

tester_1 = Tester(name='tester_1', has_deadline=False)
tester_1.work_hard()  # 'tester_1 Можно отдыхать'
tester_2 = Tester(name='tester_2', has_deadline=True)
tester_2.work_hard()  # 'tester_2 Что ж, ещё часок поработаю!' 