# Object Types / Data types

--Number : 1234, 3.1445, 3+6j, 0b111, Decimal(), Fraction()

- String : 'spam', "bob's", b'a\x01c', u'sp\xc4m'
- list : [1,2, 'three', 4.5], list(range(10))
-Tuple : (1, 'spam', 4, 'U'), tuple('spam'), namedtuple
- dictionary : {'food' : 'spam', 'taste' : 'yum'}, dict(hours = 10)

- Set : set('abc'), {'a', 'b' 'c'}

- file : open('eggs.txt'), open(r'c:ham.bin', 'wb')

notes

Here's a list of common **Python data types** classified as **mutable** or **immutable**:

---

### 🔒 **Immutable Data Types**

These **cannot be changed** after creation:

| Data Type   | Example             |
| ----------- | ------------------- |
| `int`       | `5`, `-10`, `0`     |
| `float`     | `3.14`, `-2.0`      |
| `bool`      | `True`, `False`     |
| `str`       | `"hello"`, `'a'`    |
| `tuple`     | `(1, 2, 3)`         |
| `frozenset` | `frozenset([1, 2])` |
| `bytes`     | `b"abc"`            |
| `NoneType`  | `None`              |

---

### 🔄 **Mutable Data Types**

These **can be changed** after creation:

| Data Type                | Example                                  |
| ------------------------ | ---------------------------------------- |
| `list`                   | `[1, 2, 3]`                              |
| `dict`                   | `{"a": 1, "b": 2}`                       |
| `set`                    | `{1, 2, 3}`                              |
| `bytearray`              | `bytearray(b"abc")`                      |
| `custom class instances` | Usually mutable unless defined otherwise |

---

### 🧠 Quick Tip to Remember:

* **Mutable = Changeable**
* **Immutable = Unchangeable**

Would you like a small Python code example demonstrating the difference?

# list example understanding
>>> h2 = h1
>>> h2 = h1[:]
>>> h1
[1, 2, 3]
>>> h2   
[1, 2, 3]
>>> h1[0]
1   
>>> h1[0] = 100
>>> h1
[100, 2, 3]
>>> 

[100, 2, 3]
>>> h2     
[100, 2, 3]
>>> h1 == h2   // == comparison krta h 
True
>>> h1 is h2   // is keyword reference check krta h 
False
>>>  