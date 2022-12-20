class ParameterObject:
    def __init__(self):
        self.category = None
        self.productName = None
        self.availability = None
        self.sortResult = False

    def create_parameter_object(self, cat, name, avail, sort):
        self.category = cat
        self.productName = name
        self.availability = avail
        self.sortResult = sort
