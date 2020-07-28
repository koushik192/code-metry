"""You can use this class to represent how classy someone
or something is.
"Classy" is interchangable with "fancy".
If you add fancy-looking items, you will increase
your "classiness".
Create a function in "Classy" that takes a string as
input and adds it to the "items" list.
Another method should calculate the "classiness"
value based on the items.
The following items have classiness points associated
with them:
"tophat" = 2
"bowtie" = 4
"monocle" = 5
Everything else has 0 points.
Use the test cases below to guide you!"""

class Classy(object):
    def __init__(self):
        self.items = []
        self.scores={"tophat":2,"bowtie":4,"monocle":5}
   
    def addItem(self,name):
        self.items.append(name)

    def classiness(self):
        score=0
        for i in self.items:
            if i in self.scores:
                score+=self.scores[i]
        return score