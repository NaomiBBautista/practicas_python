import turtle

#Instancias
window = turtle.Screen()
tortuga = turtle.Turtle()

#Cuadrado
def cuadrado(a, b): 
    for y in range (0,4):
        tortuga.forward(a)
        tortuga.left(b)    
        
#Triángulo        
def triangulo(a,b):
    for y in range (0,3):
        tortuga.forward(a)
        tortuga.left(b)
        
#Pentágono        
def pentagono(a,b):
    for y in range (0,5):
        tortuga.forward(a)
        tortuga.left(b)
   
cuadradito = cuadrado(100,90)
triangulito = triangulo(100,120)
pentagonito = pentagono(100,72)    

window.mainloop()

