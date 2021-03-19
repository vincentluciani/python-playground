from design_patterns.observer_pattern.observer import AbstractObserver


class BObserver(AbstractObserver):
    info_1 = -1
    info_2 = -2

    def __init__(self, subject):
        self._subject = subject
        subject.attach(self)

    # called by the subject with the notify function
    def update(self):
        self.info_1 = self._subject.info_1
        self.info_2 = self._subject.info_2
        self.display()

    def display(self):
        print('b information 1:'+ str(self.info_1))
        print('b information 2:'+ str(self.info_2))

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._subject.detach(self)
