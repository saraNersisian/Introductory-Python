def pyramid_volume(base_length, base_width, Pyramid_height):
    base_area = base_length * base_width 
    Volume = base_area * Pyramid_height * 1/3
    return Volume



base_length = int(input("length: "))
base_width =  int(input("Width: "))
Pyramid_height = int(input("Height: "))


volume=pyramid_volume(base_length, base_width, Pyramid_height)
print("\nVolume= %.2f"%(volume))
    