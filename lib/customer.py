class Customer:
    def __init__(self,name):
        self.name =name
    @property
    def name(self):
        return self._name  
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or 1 < value > 15:
            raise Exception('Name must be string betwwen 1 to 15 letters')  