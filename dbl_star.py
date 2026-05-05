''' '**' double star also called as keyword argument, Inside the function, kwargs is always a dict.
Each keyword argument you pass becomes a key–value pair in that dict
Called the “double splat operator”.

Collects keyword arguments into a dictionary (**kwargs).

Also used to unpack dictionaries when calling functions:'''

def demo(**kwargs):
    print(kwargs)

demo(name="Nitesh", age=22)
# Output: {'name': 'Nitesh', 'age': 22}
