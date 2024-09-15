choice = input("Enter your choice (input or output): ")

if choice == 'input':
  num = int(input("Enter a number: "))
  reversed_num = 0
  while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10
  print("Reversed number:", reversed_num)

elif choice == 'output':
  start = int(input("Enter the starting number: "))
  end = int(input("Enter the ending number: "))
  step = int(input("Enter the step value: "))
  direction = input("Enter the direction (forward or backward): ")
  orientation = input("Enter the orientation (horizontal or vertical): ")

  if direction == 'forward':
    range_func = range(start, end + 1, step)
  else:
    range_func = range(start, end - 1, -step)

  if orientation == 'horizontal':
    for num in range_func:
      reversed_num = 0
      while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
      print(reversed_num, end=' ')
  else:
    for num in range_func:
      reversed_num = 0
      while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
      print(reversed_num)

else:
  print("Invalid choice. Please enter 'input' or 'output'.")