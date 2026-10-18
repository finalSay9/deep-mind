class Arrays:
    def __init__(self):
        self.list = []

    def check_elements(self):
        return len(self.list)
    
    def add_elements(self):
        while True:
            self.value = int(input('add element: '))
            self.list.append(self.value)
            if self.value == 0:
                break
        return self.list




    def delete_element(self, value):
        for _ in range(len(self.list)):
            if len(self.list) == None:
                return f'list is empty'
            if value not in self.list:
                return f'{value} not available'
            else:
                self.list.remove(value)
        return self.list

check = Arrays()
print(check.add_elements())
print(check.check_elements())
print(check.delete_element(8))
print(check.check_elements())

       