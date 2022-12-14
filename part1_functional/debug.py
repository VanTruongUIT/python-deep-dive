numbers1 = frozenset([1, 2, 3, 4, 5])
numbers2 = frozenset([2, 3, 4, 5])
numbers3 = frozenset([6, 7])

# Combining both of them using "|" operator
# You can also use union() method
combined = numbers1 | numbers2
print("Combined set:", combined)

# Selecting common elements using "&" operator
# You can also use intersection() method
intersect = numbers1 & numbers2
print("Intersected set:", intersect)


# Selecting elements which are not common using "-" operator
# You can also use difference() method
difference = numbers1 - numbers2
print("Difference set:", difference)


# It returns True if sets (frozenset) have no common items otherwise False
Disjoint = numbers1.isdisjoint(numbers2)
print("Disjoint:", Disjoint)

numbers1
numbers2
numbers3


# It returns True if sets (frozenset) have no common items otherwise False
Disjoint = numbers1.isdisjoint(numbers3)
print("Disjoint:", Disjoint)


# It returns True if all the items of a set (frozenset) are common in another set (frozenset)
Subset = numbers1.issubset(numbers2)
print("Subset:", Subset)


# It returns True if all the items of a set (frozenset) are common in another set (frozenset)
Subset = numbers2.issubset(numbers1)
print("Subset:", Subset)


# It returns True if a set (frozenset) has all items present in another set (frozenset)
Superset = numbers1.issuperset(numbers2)
print("Superset:", Superset)


# It returns True if all the items of a set (frozenset) are common in another set (frozenset)
Superset = numbers2.issuperset(numbers1)
print("Superset:", Superset)

my_list = [1, 2]
my_set = {"key1", "key2"}

my_dict = dict(zip(my_set, my_list))
my_dict


first_number = 10
second_number = 10
third_number = second_number

print((hex(id(first_number)) == hex(id(second_number))))
print((hex(id(second_number)) == hex(id(third_number))))
print((hex(id(first_number)) == hex(id(third_number))))