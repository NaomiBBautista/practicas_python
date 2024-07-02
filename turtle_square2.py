import turtle

#Instancias
window = turtle.Screen()
tortuga = turtle.Turtle()

#Cuadrado
def cuadrado(a, b):
    grados = 15
    for y in range (3):
        tortuga.left(grados)
        for x in range (0,4):
            tortuga.forward(a)
            tortuga.left(b)    
   
cuadradito = cuadrado(100,90)   

window.mainloop()

