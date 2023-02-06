# The "while" loop continues as long as the condition is true
counter = 8
while counter > 0:
  if counter == 4:
      counter -= 1
      continue
  print(counter)
  counter -= 1

print('The loop has ended')
