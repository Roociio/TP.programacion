#Ejercicio 1
class Empleado:#creo una clase empleado
    
    def __init__(self,nombre,salario,años_antiguedad):#le doy estos atributos
     self.nombre=nombre
     self.salario=salario
     self.años_antiguedad =años_antiguedad
        
        
    def calcular_bono(self):#creo un metodo para calcular el bono
        bono=(self.salario)*0.05*(self.años_antiguedad)#creo una variable donde se multiplica el salario,año de antiguedad y el 5%
        return bono
    
    def info_del_empleado(self):
        bono=self.calcular_bono()#llamo al metodo  y despues muestro la info.
        print(f"la persona {self.nombre} tiene {self.años_antiguedad} años de antiguedad y su salario es {self.salario}")
        print(f"su bono sera de {bono}")
        
empleado=Empleado("Carlos",5000,3)
empleado.info_del_empleado()

#Ejercicio 2
from datetime import datetime

class Base_producto:#creo la clase padre
    def __init__(self,nombre,precio,fecha):#pongo los atributos
        self.nombre=nombre
        self.precio=precio
        self.fecha=fecha
        
    def aplicar_descuento(self):#el primer metodo es para el 10% de descuento
        descuento=self.precio*0.10
        return descuento
        
class Producto_perecedero (Base_producto):#creo la clase hija
    def __init__(self,nombre,precio,fecha):
        super(). __init__(nombre,precio,fecha)#hago referencia a lo que esta en el padre
    
    def aplicar_descuento(self):
     segundo_descuento=self.precio*0.20#hago el descuento del 20%
     dias=(datetime.now() - self.fecha).days#creo una variable donde resto los dias para ver si se paso de 5 dias
        
     if dias > 5 :#hago un if para que si pasaron mas de 5 dias se haga el descuento del 20%
        print("como pasaron los 5 dias se aplico un 20% de descuento quedaria ",segundo_descuento)
     else:print("como no pasaron 5 dias el descuento es de un 10%",self.descuento)#pero si la primer condicion no se cumple que se haga el 10%
    
producto=Producto_perecedero("coca",5000,datetime(18,11,24))
producto.aplicar_descuento()

#Ejercicio 3
from abc import ABC,abstractmethod
from datetime import datetime
class Vehiculo(ABC):#cree la interfaz
    @abstractmethod
    def arrancar(self):
        pass
    
    @abstractmethod
    def detener(self):
        pass
    
class Coche (Vehiculo):
     def arrancar(self):#hice la clase coche
         self.inicio = datetime.now()#pongo datetime para que tome el tiempo cuando inicie
         return "esta arrancando"
     def detener(self):
        fin=datetime.now()#hago otra variable con datetime para cuando termina el tiempo
        duracion=fin-self.inicio#para que despues en esta variable se restan los dos tiempos
        print( "se detuvo,el coche duro",duracion)#y te de el resultado de cuanto tiempo anduvo
        
coche=Coche()
print(coche.arrancar())
print(coche.detener())

class Bicicleta(Vehiculo):#lo mismo hice con la clase bicicleta
    def arrancar(self):
        self.inicio = datetime.now()
        return "arranco andar en bici"
    def detener(self):
        fin=datetime.now()
        duracion=fin-self.inicio
        print( "se detuvo,anduvo en bicicleta",duracion)
bici=Bicicleta()
print(bici.arrancar())
print(bici.detener())

#ejercicio 4 #ARREGLAR
class Cliente:#cree una clase donde le puse los atributos y a saldo indique que puede ser de tipo float
    def __init__(self,nombre,correo,saldo:float):
        self.nombre=nombre
        self.correo=correo
        self.tipo_cliente=None#en tipo_cliente le puse none para indicar que esta vacia y no esta en el constructor porque sino pide que ingreses el tipo_cliente
        self.saldo=saldo
        
        if self.saldo >=5000:#hice un condicional que si el saldo es mayor o igual a 5000 
            self.tipo_cliente = "premium"#seas tipo_cliente premium sino regular
        else:self.tipo_cliente = "regular"#y esto ya se guarda automaticamente en tipo_cliente
        
    def actualizar(self,monto : float):
        self.saldo += monto#cree un metodo donde se le agrema un monto a saldo 
        
        if self.saldo >=5000:#y la misma concion que en el constructor, si el 
            self.tipo_cliente = "premium"#el saldo es mayor a 5000 que sea premium o regular
        else:self.tipo_cliente = "regular"
        
        print( f"el cliente {self.nombre},correo {self.correo} tiene una cuenta {self.tipo_cliente} y saldo {self.saldo}")
        #y que con un print muestre todo
        
cliente=Cliente("rocio","abc",1000)
cliente.actualizar(2000)

#ejercicio 5
from math_utils import calcular_division_segura#importo la calculadora

a=float(input("ingrese un numeros" ))#solicito los numeros
b=float(input("ingrese otro numeros"))

resultado=calcular_division_segura(a,b)
print(resultado)

#ejercicio 6
def procesar_lista_numeros(lista:list [int]):
    for i in lista :
        if i %2 == 0:
         print(i)
         
    return 
         
lista=[2,4,6,7,5,3,9,1,0,5,]
procesar_lista_numeros(lista)

#ejercicio 8
#Un parametro es una variable que se declara adentro de una funcion y sirve para darle un valor cuando se llame a la funcion.
#El tipado de funciones se usa para anotaciones de tipo y es para especificar que tipo de dato tienen que recibir los 
#parametreos y que tipo deberia devolver la función.La sintaxis del tipado es parametreo:tipo y para que lo devuelva ->tipo.
#Ejemplos:
#1.
def suma(a:int,b:int)->int:#al yo especificar que el dato tiene que ser de tipo entero,ayuda a que no haya errores
    return a+b
    
num=suma(2,2)
print(num)

#2.
def area_rectangulo(base:float,altura:float)->float:
    return base*altura

num1=area_rectangulo(6,12)
print(num1)



        