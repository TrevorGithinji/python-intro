from functools import reduce


def add_two_numbers(a, b, ):
    return a + b

print(add_two_numbers(1, 2, ))

add_two = lambda a, b, : a + b

print(add_two(5,6 ))

scores = [{"eng": 56, "mat": 60},
         {"eng": 68, "mat": 34},
         {"eng": 53, "mat": 24},
         {"eng": 96, "mat": 57},
         {"eng": 78, "mat": 78},
         {"eng": 23, "mat": 91}]

sorted_by_math = sorted(scores, key=lambda s: s["mat"])

print(sorted_by_math)

def get_eng_score(score):
    return score["eng"]

sorted_by_eng = sorted(scores, key=get_eng_score)

print(sorted_by_eng)

ages = [25, 35, 45, 50, 34, 64, 74, 34, 12,  75, 24, 75 , 32]

total_age = reduce( lambda x, y: x + y, ages, 0 )
print(total_age)

new_ages = map(lambda x: x+1, ages )
print(list(new_ages))

above_40 = filter(lambda age: age > 40, ages)
print(list(above_40))



