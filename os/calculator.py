run = True
while run:
  print("calculator \n to exit 'exit'")
  data = input(">:> ")
  if data == 'exit':
    run = False
  print(eval(data))
