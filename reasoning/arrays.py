class Arrays:
    def __init__(self):
        self.list = []

    def check_elements(self):
        return len(self.list)
    
    def add_elements(self, value):
        self.list.append(value)
        return self.list

    def delete_element(self, value):
        if self.list == None:
            return f'list is empty'
        else:
            self.list.remove(value)
        return self.list

check = Arrays()
print(check.add_elements(8))
print(check.check_elements())
print(check.delete_element(87))
print(check.check_elements())

       