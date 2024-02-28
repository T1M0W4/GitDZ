import math

def calculate_tank_volume(diameter, height):
    radius = diameter / 2
    
    volume_cubic_meters = math.pi * radius ** 2 * height
    
    volume_liters = volume_cubic_meters * 1000
    
    return volume_liters


diameter = float(input("Введите диаметр бака в метрах: "))
height = float(input("Введите высоту бака в метрах: "))

tank_volume_liters = calculate_tank_volume(diameter, height)
print("Объем бака в литрах:", tank_volume_liters)