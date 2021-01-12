def calculate():
     def nextInt():
         return int(input())
     def getOperator():
         if token == "+":
             return lambda x, y: x + y
         if token == "-":
             return lambda x, y: x - y
         if token == "*":
             return lambda x, y: x * y
         if token == "/":
             return lambda x, y: x / y
         raise ValueError(f"Wrong operator: {token}")
     stack = []
     stack.append(nextInt())
     stack.append(nextInt())
     while stack[1:]:
         token = input()
         result = None
         if token.isnumeric():
             result = int(token)
         elif token in ("+", "-", "*", "/",):
             result = getOperator()(stack.pop(), stack.pop())
         else:
             raise ValueError(f"Wrong token: {token}")
         stack.append(result)
     return stack.pop()
print(calculate())
