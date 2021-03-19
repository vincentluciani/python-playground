from design_patterns.observer_pattern.a_observer import AObserver
from design_patterns.observer_pattern.b_observer import BObserver
from design_patterns.observer_pattern.my_subject import MySubject

my_subject = MySubject() # subject ( source of information )
a_observer = AObserver(my_subject) # a subscribes to the source of information,
                                    # a_observer can be used to take off a from the subscribers
b_observer = BObserver(my_subject) # b subscribes to the source of information

my_subject.set_attributes(1,2) # information added to the source of information
my_subject.set_attributes(3,4)
my_subject.set_attributes(5,6)

my_subject.detach(a_observer) # take off a from the list of subscribers
print("===detachment====")
my_subject.set_attributes(7,8)