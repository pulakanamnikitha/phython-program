def do_stuff(input):
	s, op, n = [s for s in input.split(" ")]
	if op == '/':
		print(int(s) / int(n))
	else:
		print(int(s) % int(n))
while True:
  try:
    value = raw_input()
    do_stuff(value.rstrip()) 
  except (EOFError):
    break 
