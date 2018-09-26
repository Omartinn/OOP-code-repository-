from animal_class import *

class Sheep(Animal):
    """A Sheep simulation"""

    #constructor
    def __init__(self):
        #call the parent class constructor with default values for sheep
        #growth rate = 1; food need = 3; water need = 6
        super().__init__(1,3,6)
        self._type = "Sheep"

    #overide grow method for subclass
    def grow(self,food,water):
        if food >= self._food_need and water >= self._water_need:
            if self._status == "baby" and water > self._water_need:
                self._weight += self._growth_rate * 1.5
            elif self._status == "child" and water > self._water_need:
                self._weight += self._growth_rate * 1.25
            else:
                self._weight += self._growth_rate
        #incriment days growing
        self._days_growing += 1
        #update status
        self._update_status()
        
            
            

def main():
    #create new sheep
    sheep_animal = Sheep()
    print(Sheep_animal.report())
    #manually grow the sheep
    manual_grow(sheep_animal)
    print(sheep_animal.report())
    manual_grow(sheep_animal)
    print(sheep_animal.report())

if __name__ == "__main__":
    main()
