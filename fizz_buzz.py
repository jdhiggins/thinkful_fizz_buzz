import sys
  
def fizzbuzz(n):
  printable = str(n)
  print("Fizz buzz counting up to {}".format(printable))
  x = 1
  while x <= n:
        
    if x % 3 == 0 and x % 5 == 0:
        print "fizz buzz"
    elif x % 3 == 0:
        print "fizz"
    elif x % 5 == 0:
        print "buzz"
    else: 
      print x
    x += 1
        
    if x % 3 == 0:
      if x % 5 == 0:
        print "fizz buzz"
      else: 
        print "fizz"
    elif x % 5 == 0:
        print "buzz"
    else: 
      print x
    x += 1

for variablename in some_iterable:
    
    range(10) = [0,1,2,3,4,5,6,7,8,9]
    for i in range(1,n+1): 
    
if len(sys.argv) > 1:
  try:
    limit = int(sys.argv[1])
  except ValueError:
    print "Please run program again with an integer value in argv!"
    sys.exit(1)
  fizzbuzz(limit)
else:
  while True:
    try:  
      limit = int(raw_input("Enter a positive integer: "))
      break
    except ValueError:
      print "That wasn't a positive integer greater than one.  Please try again."
  if limit >= 1:    
    fizzbuzz(limit)
  else:
    print "Must be an integer greater than 1."