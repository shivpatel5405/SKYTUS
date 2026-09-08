# Simulate a traffic light : Red = Stop, Yellow = Slow down, Green = Go
light = input("Enter the traffic light color (Red, Yellow, Green): ")
if light == "Red":
    print(f"The traffic light is {light}. You must stop.")
elif light == "Yellow":
    print(f"The traffic light is {light}. You should slow down.")
elif light == "Green":
    print(f"The traffic light is {light}. You can go.")
    