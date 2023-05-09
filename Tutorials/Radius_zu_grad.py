#converts radius to gradiant
import math 
radius = input ("Gib den Radius an: ")
print(float(radius))
ergebniss = float(radius) * 180 / math.pi
print (str((round(ergebniss, 2))))

