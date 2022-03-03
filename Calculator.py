n = input(("Enter a number: "))
m = input(("Enter your second number: "))
o = input(('''Please write the operation you want to perform: (!Please write the operation in lower case only|
              Note that the first number will be divided by the second number in case of division.
              Note this too that the first number will be subtracted by the second number in case of subtraction.)
add
subtract
multiply
divide
___________________________________________________
'''))
if o == "divide":
    print(n+" divided by", m+" is", int(n)/int(m))
    input(("Please press ENTER to close this program/App."))
    
if o == "multiply":
    print(int(n)*int(m))
    input(("Please press ENTER to close this program/App."))
    
if o == "subtract":
    print(int(n)-int(m))
    input(("Please press ENTER to close this program/App."))

if o == "add":
    print(int(n)+int(m))
    input(("Please press ENTER to close this program/App."))