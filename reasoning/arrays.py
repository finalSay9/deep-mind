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
            elif value in self.list:
                self.list.remove(value)
           
        return self.list

check = Arrays()
print('original list', check.add_elements())
print('orignal length', check.check_elements())
print('after deletion remained list', check.delete_element(8))
print('left legth', check.check_elements())

       