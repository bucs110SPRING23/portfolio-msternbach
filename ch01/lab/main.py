#Part B
import random
random_list = [1,"test",2000,.008,8.9]
result = random.choice(random_list)
print(result)


#Part A
weeks = 16
classes = 5
tuition = 6000
cost_per_week = ((tuition / classes) / weeks)
print(cost_per_week, type(cost_per_week))
print("Cost per week:", cost_per_week)
classes_per_week = (classes/weeks)
print(classes_per_week, type(classes_per_week))
cost_per_class = (cost_per_week/classes_per_week)
print(cost_per_class, type(cost_per_class))
print("Cost per class:", cost_per_class)
