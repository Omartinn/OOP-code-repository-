class Crop:
    """A generic food crop"""

    def __init__(self,growth_rate, light_need, water_need):

        self._growth = 0
        self._days_growing = 0
        self._growth_rate = growth_rate
        self._light_need = light_need
        self._water_need = water_need
        self._status = "seed"
        self._type = "generic"

def main():
    new_crop = Crop(1,4,3)
    print(new_crop._status)
    print(new_crop._light_need)
    print(new_crop._water_need)
    new_crop2 = Crop(1,3,2)
    print(new_crop._status)
    print(new_crop._light_need)
    print(new_crop._water_need)
    

if __name__ == "__main__":
    main()


