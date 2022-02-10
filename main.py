import random

#Part A
weeks = 16
classes = 5
tuition = 6000
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week)

classes_per_week = 3
cost_per_class = (cost_per_week/classes_per_week)
print("Cost per class:", cost_per_class)

print()
print("classes_per_week:", classes_per_week, type(classes_per_week))
print("cost_per_class:", cost_per_class, type(cost_per_class))

#Part B
fruit = ["apple", "orange", "pear", "persimmon", "banana"]
fruit_choice = random.choice(fruit)

print()
print(fruit_choice)