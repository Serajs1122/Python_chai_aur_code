'''
 🧮 Python Numbers – Cheat Sheet

### 1. **Types of Numbers in Python**

| Type      | Description                      | Example         |
| --------- | -------------------------------- | --------------- |
| `int`     | Integer numbers                  | `10`, `-5`, `0` |
| `float`   | Decimal numbers (floating-point) | `3.14`, `-0.5`  |
| `complex` | Complex numbers                  | `2 + 3j`        |

---

### 2. **Type Checking**

Use `type()` to check data type:

```python
x = 5
print(type(x))  # <class 'int'>
```

---

### 3. **Type Conversion**

Convert between types using:

```python
int(3.5)     # 3
float(5)     # 5.0
complex(2)   # (2+0j)
```

---

### 4. **Basic Arithmetic Operators**

| Operator | Description         | Example (`a=5`, `b=2`) | Result |
| -------- | ------------------- | ---------------------- | ------ |
| `+`      | Addition            | `a + b`                | `7`    |
| `-`      | Subtraction         | `a - b`                | `3`    |
| `*`      | Multiplication      | `a * b`                | `10`   |
| `/`      | Division (float)    | `a / b`                | `2.5`  |
| `//`     | Floor Division      | `a // b`               | `2`    |
| `%`      | Modulus (remainder) | `a % b`                | `1`    |
| `**`     | Exponentiation      | `a ** b`               | `25`   |

---

### 5. **Math Functions** (using `import math`)

```python
import math

math.sqrt(16)      # 4.0
math.pow(2, 3)     # 8.0
math.floor(3.9)    # 3
math.ceil(3.1)     # 4
math.pi            # 3.141592653...
```

---

### 6. **Random Numbers** (using `import random`)

```python
import random

random.randint(1, 10)   # Random int between 1 and 10
random.random()         # Random float between 0 and 1
'''



x = 2 
y = 3 
z =  4 
print(x + y)
print((x + y) * z)

# comparison operator 

print(x>y)
print(x<y)
print(x== y)

print(x<y and y<z)  # // and dono statement true hona chahiye to result true hoga 
print(x<y or y<z)  # // or main koi v ek statement true hona chahiye to result true hoga

import math
print(math.floor(3.5))   #// floor round-off value deta h
print(math.floor(-4.5))

print(math.trunc(2.5))  # trunc jo h wo hamesha number k towords jata h jaise ki 2.5 ka 2 output dega or -2.5 ka -2 output dega
print(math.trunc(-2.5))  


#notes - 
# (1) - 0o20 - ye octal value h
# (2) - 0xFF - ye Hexal value h
# (1) - 0b1000 - ye Binary value h

print(0o20) # octal Value
print(0xFF) # hexal Value
print(0b1000) # Binary Value

# how to convert NUMBER TO OCTAL VALUE , NUMBER TO HEXAL VALUE AND NUMBER TO BINARY VALUE

print(oct(52))  # output is 0o64
print(hex(52))  # output is ox34
print(bin(52))  # ouput is 0b110100



