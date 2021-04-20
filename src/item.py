class Item:
    def __init__(self, typex: str, description: str, size: str, brand: str, color: str, sex: str):
        #self.favorite = favorite
        self.type = typex
        self.description = description
        #self.in_out_use = in_out_use
        self.size = size
        self.brand = brand
        self.color = color
        self.sex = sex
        #self.condition = condition
        #self.washed = washed
        #self.other_comments = other_comments

# vaatteen tai tavaran riviolio
# pylint approves only 6 attributes >> have to do sub-classes if want to have more
