# Welcome to **neon**

## Warning

**neon** is an entirely experimental library consisting largely of decorators I think will be useful to me.
I may be very wrong.  **neon** comes with no warranty.

## Basic philosophy

1. Per function logging
2. Distinguish between mutable and immutable
3. Fix code quickly


## @normalize_fields

```
@normalize_fields(bar=lambda x: x.lower())
@normalize_fields(foo=lambda x: x.lower(), quux=lambda x: x.upper())
def myfunction(foo, bar="PET", quux="motor"):
    x = 5
    print(foo, bar, quux)
    

myfunction("my", "PIGEON", "Pie")
myfunction("MY")
myfunction("MY", "CAT")
myfunction("my", "CAT")
myfunction("MY", "dog")
```

## @memoize

WARNING: Do not use this if you are using objects that are hashable but not immutable

```
@memoize
def fib(a):
    if a < 2:
        return 1
    return fib(a-1) + fib(a-2)
```
