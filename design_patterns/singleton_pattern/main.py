from design_patterns.singleton_pattern.my_singleton import MySingleton

test_singleton = MySingleton('hello')

test_singleton.display_text('world')

test_singleton_2 = MySingleton('bye bye')

test_singleton_2.display_text('world')
