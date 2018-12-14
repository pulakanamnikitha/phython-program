def do_stuff(input):
	s,n = [int(y) for y in input.split(" ")]
	print(n-s)
while True:
  try:
    value = raw_input()
    do_stuff(value.rstrip()) 
  except (EOFError):
    break 
