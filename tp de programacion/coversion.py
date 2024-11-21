from dolar import dolar  
from euro import euro

#te voy a ser sincera me costo un poco hacer el menu porque no sabia 
#como llamar a las funciones y vi varios videos y lo hacian asi ,entonces dije bueno intento hacerlo asi y funciono entonces quedo asi :)

moneda=input("elija que moneda quire usar (euro/dolar)")#creo una variable donde se ingresa que tipo de moneda quiere usar
if moneda =="euro":#hice un condicional donde si elije euro o dolar 
    accion=input("queres (comprar/vender)")
    pesos=input("cuantos pesos queres ingresar")
    if accion=="comprar":#y adentro de un condicional hice otro pero este para la opcion compra o venta
        compra,venta=euro.euro(pesos)#aca con esto se llama a la funcion
        print(f"compraste {compra} euros ")
    elif accion=="vender":
        compra,venta=euro.euro(pesos)
        print(f"vendiste {venta} euros ")
    else:print("volver a intentar")
elif moneda == "dolar":#y lo volvi a repetir para la parte de dolar
    accion=input("queres (comprar/vender)")
    pesos=float(input("cuantos pesos queres ingresar"))
    if accion=="comprar":
        compra,venta=dolar.dolar(pesos)
        print(f"compraste {compra} dolares ")
    elif accion=="vender":
        compra,venta  =dolar.dolar(pesos)
        print(f"vendiste {venta} dolares ")
    else:print("volve a intentar")
else:print("volve a intentar profe")