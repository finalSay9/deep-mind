class LetsSort:
    def __init__(self):
        self.list = []

    #add elements randoly to the list, not in order
    def add_elements(self):
        while True:
            self.element = int(input('add element: '))
            self.list.append(self.element)
            if self.element == 0:
                break
        return self.list
    
    def sortElements(self):
        for _ in self.list:
            for i in range(len(self.list) -1):
                if self.list[i] > self.list[i+1]:
                    self.list[i], self.list[i+1] = self.list[i+1], self.list[i]
        return self.list


test = LetsSort()
print('unsorted list:' ,test.add_elements())
print('sorted list:' ,test.sortElements())
        