def calcular_division_segura(a,b):#creo una funcion
    try:#pongo try para que se ejecute el codigo 
        division=(a/b)
    except ZeroDivisionError:#puse el except por si se divide por 0 va a mostrar este mensaje
        print("no se puede dividir por 0")
    else:#y un else para que si se ejecuta el codigo que  muestre este mensaje 
        print("la respuesta es ",division)
        return division
        
