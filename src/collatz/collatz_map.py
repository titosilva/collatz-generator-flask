from typing import List, Tuple

def collatz_iterate(number: int):
    return int(number/2 if number % 2 == 0 else 3*number + 1)

class CollatzMap:
    __map_values: List[int] = []
    __map_values_pointer: List[int] = [] # Store the indexes of the elements pointed

    def __recursive_add(self, value: int) -> int:
        if value in self.__map_values:
            return self.__map_values.index(value)

        if value == 1:
            self.__map_values.append(1)
            self.__map_values_pointer.append(None)
            return len(self.__map_values) - 1
            
        next_value = collatz_iterate(value)
        pointer = self.__recursive_add(next_value)

        self.__map_values.append(value)
        self.__map_values_pointer.append(pointer)

        return len(self.__map_values) - 1

    def add(self, value: int):
        self.__recursive_add(value)

    def get_elements_pointed_at(self, value: int) -> List[int]:
        idx = self.__map_values.index(value)
        
        result = []
        for i, v in enumerate(self.__map_values):
            if self.__map_values_pointer[i] == idx:
                result.append(v)
        
        return result
