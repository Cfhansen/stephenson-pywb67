###solution to problem 67 from ben stephenson's "the python workbook".
###i make things simpler by assuming zoo visitors are at most 1000 years old.

def get_age():
  print("Enter the age of the visitor:")
  result = input()
  if result != '':
    return float(result)
  else:
    return -1

age = get_age()

costs_by_age = {  3:  0,
                  12: 14,
                  64: 23,
                  1000: 18, }

ages = costs_by_age.keys()
total_cost = 0

while age != -1:
  m = 0
  for i in ages:
    if age < i and m == 0:
      total_cost += costs_by_age[i]
      m = 1
  age = get_age()

print(f'The total cost is {total_cost:.2f}.')
