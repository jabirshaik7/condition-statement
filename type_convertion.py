# Demonstrating Python type conversions with explanations

# 1. Integer conversions
a = 10
print("Integer a =", a)
print("float(a) ->", float(a))   # int → float works
print("str(a) ->", str(a))       # int → string works
# list(a) -> error because int is not iterable
print("list([a]) ->", list([a])) #  wrap inside iterable
print("tuple([a]) ->", tuple([a]))
print("set([a]) ->", set([a]))
print("dict([[a, a*a]]) ->", dict([[a, a*a]]))  # needs key-value pairs
print("bool(a) ->", bool(a))     # nonzero int → True

print("-"*40)

# 2. Float conversions
b = 10.3
print("Float b =", b)
print("int(b) ->", int(b))       # float → int truncates decimal
print("str(b) ->", str(b))       # float → string
# list(b) -> error, float not iterable
print("list([b]) ->", list([b])) #  wrap inside iterable
print("bool(b) ->", bool(b))     # nonzero float → True

print("-"*40)

# 3. String conversions
s = "python"
print("String s =", s)
# int(s) -> error unless string is numeric
# float(s) -> error unless string is numeric
print("list(s) ->", list(s))     # string is iterable → list of chars
print("tuple(s) ->", tuple(s))   # tuple of chars
print("set(s) ->", set(s))       # set of unique chars
# dict(s) -> error, needs pairs
print("bool(s) ->", bool(s))     # non-empty string → True

# Numeric string example
s = "10"
print("int('10') ->", int(s))    #  converts to integer
print("float('10') ->", float(s))#  converts to float

print("-"*40)

# 4. List conversions
l = [1, 2, 3, 4]
print("List l =", l)
# int(l) -> error, list not directly convertible
# float(l) -> error
print("str(l) ->", str(l))       # list → string representation
print("tuple(l) ->", tuple(l))   # list → tuple
print("set(l) ->", set(l))       # list → set
# dict(l) -> error unless list contains pairs
print("bool(l) ->", bool(l))     # non-empty list → True

print("-"*40)

# 5. Tuple conversions
t = (1, 2, 3, 4)
print("Tuple t =", t)
print("str(t) ->", str(t))       # tuple → string
print("list(t) ->", list(t))     # tuple → list
print("set(t) ->", set(t))       # tuple → set
# dict(t) -> error unless tuple contains pairs
print("bool(t) ->", bool(t))     # non-empty tuple → True

print("-"*40)

# 6. Set conversions
s = {1, 2, 3, 4}
print("Set s =", s)
print("str(s) ->", str(s))       # set → string
print("list(s) ->", list(s))     # set → list
print("tuple(s) ->", tuple(s))   # set → tuple
# dict(s) -> error unless set contains pairs
print("bool(s) ->", bool(s))     # non-empty set → True

print("-"*40)

# 7. Dictionary conversions
d = {1:1, 2:4, 3:9, 4:16}
print("Dict d =", d)
print("str(d) ->", str(d))       # dict → string
print("list(d) ->", list(d))     # dict → list of keys
print("tuple(d) ->", tuple(d))   # dict → tuple of keys
print("set(d) ->", set(d))       # dict → set of keys
print("bool(d) ->", bool(d))     # non-empty dict → True

print("-"*40)

# 8. Boolean conversions
a = True
print("Boolean a =", a)
print("int(a) ->", int(a))       # True → 1
print("float(a) ->", float(a))   # True → 1.0
print("str(a) ->", str(a))       # True → "True"
# list(a) -> error, bool not iterable
print("list([a]) ->", list([a])) #  wrap inside iterable
print("set([a]) ->", set([a]))
print("tuple([a]) ->", tuple([a]))
# dict(a) -> error, needs pairs
print("complex(a) ->", complex(a)) # True → (1+0j)
