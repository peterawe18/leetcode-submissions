class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity # storing capcity of arr
        self.size = 0 # assume size(length) is zero, no values yet
        self.arr = [0] * capacity # creating arr of size capacity


    def get(self, i: int) -> int:
        return self.arr[i] # return value at index i

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n # assign val at index i to n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity: # if length equals capacity then resize
            self.resize()
        
        self.arr[self.size] = n # assign value n to end of arr
        self.size +=1 # increasing size cause we are at end

    def popback(self) -> int:
        if self.size > 0: # if length does not equal 0 then remove the last value
            self.size -=1
        return self.arr[self.size] # here we are returning the popped element
 

    def resize(self) -> None:
        self.capacity = self.capacity * 2 # double the capacity 
        new_arr = [0] * self.capacity # creating temp new arr to hold bigger size

        for i in range(self.size): # loop through old arr to store in new arr
            new_arr[i] = self.arr[i]
        self.arr = new_arr # assign new arr to old arr

    def getSize(self) -> int:
        return self.size # we already have size from start so we can just call it 
    
    def getCapacity(self) -> int:
        return self.capacity # we already have capacity from start so we can just call it
