#  text_warp _example.py

sample_text = """
    The textwarp module can be used to format text for output in
    situations where pretty-printing is desired. It offers
    programmatic functionality similar to the paragragh wrapping 
    or filling features found in many text editors.
"""
import textwrap

print(textwrap.fill(sample_text,width=50))


class fruit:
    """
    Def a class fruit
    """
    def __init__(self,name):
        self.name = name
    def shape(self):
        pass 

class apple(fruit):
    
    def __init__(self,name):
        self.name = name
        # self.shape = shape
    def __add__(self,other):
        return apple(self.name + other.name)
a = apple("Oppo")
b = apple("BooK")
print(a.name)
print(b.name)
print(a + b)

