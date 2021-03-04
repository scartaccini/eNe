from django.http import HttpResponse
import random

#variable para controlar que si hay un ganador en la partida, los otros que sigan
#acertando, no tengan contador
ganador=[2]
partida=0
numeros_guardados=[]
lista_resultados=[]
##clase para registrar numeros para adivinar
class n:
    def iniciar(self,num1,num2,num3,num4):
        self.num1=num1
        self.num2=num2
        self.num3=num3
        self.num4=num4
    
    #def imprimir(self):
        #print("el numero es: ", self.num1)
        
number=n()

### primer paso, ingresar los numeros para adivinar en la instancia number
def ingresar(request,num1,num2,num3,num4):
### controla que no se ingrese un nuevo numero secreto mientras se esta jugando
### cuando se aciertan los cuatro numeros_guardados queda en 0 entonces se puede ingresar numero secreto
### solo se puede ingresar un nuevo numero secreto sise reinicia el servidor o si no se empezo a jugar(/ene/x/x/x/x)
    if len(numeros_guardados)==0:
        
        if num1>=0 and num1<10 and num2>=0 and num2<10 and num3>=0 and num3<10 and num4>=0 and num4<10:
            if num1 != num2 and num1!=num3 and num1!=num4 and num2!=num3 and num2!=num4 and num3!=num4:
                number.iniciar(num1,num2,num3,num4)
                
                ganador[0]=1
                ###contador de partidas
                global partida
                partida=partida+1
                #number.imprimir()
                #return HttpResponse(" %s " %number.num1)
                return HttpResponse(" Se ingreso el número secreto correctamente!, número de partida: %s " %partida)
            return HttpResponse(" Los números tienen que ser distintos entre sí ")
        return HttpResponse(" Los números tienen que ser del 0 al 9 ")
    else:
        print("Ya existe un número secreto ingresado")
        return HttpResponse("Ya existe un número secreto ingresado")

### segundo paso, ingresar los numeros para inetnatr adivinar los numeros del primer paso
def numeros(request,numero1,numero2,numero3,numero4):
    if numero1>=0 and numero1<10 and numero2>=0 and numero2<10 and numero3>=0 and numero3<10 and numero4>=0 and numero4<10:
        if numero1 != numero2 and numero1!=numero3 and numero1!=numero4 and numero2!=numero3 and numero2!=numero4 and numero3!=numero4:
          
            
            #val1=2
            #val2=4
            #val3=6
            #val4=8
### guarda en val1,2,3 y 4 los valores guardados previeamente en el objeto number(secreto)            
### se captura error cuando no se ingresan los numeros para adivinar y se ingresan los numeros para intentar adivinar
            print(ganador)
            try:
                val1=number.num1
                val2=number.num2
                val3=number.num3
                val4=number.num4
                acertados="NADA"
                n1="NADA"
                n2="NADA"
                n3="NADA"
                n4="NADA"
### castea a sttring los 4 num ingresados, los concatena y los guarada en "numeros_strings"            
### "numeros_strings" se va a ir agregando a la lista "numeros_guardados"                
                nume1=str(numero1)
                nume2=str(numero2)
                nume3=str(numero3)
                nume4=str(numero4)
                numeros_strings=nume1+nume2+nume3+nume4
                
                numeros_guardados.append(numeros_strings)
                print(numeros_guardados)
                
                #ganador=True
    ### compara numeros ingresados con numeros objeto(secreto)
                if val1==numero1:
                    #return HttpResponse("Hola %s" %numero)
                    n1="ACERTASTE"
                if val2==numero2:
                    #return HttpResponse("Hola %s" %numero)
                    n2="ACERTASTE"
                    #return HttpResponse(" %s " %acertados)
                if val3==numero3:
                    #return HttpResponse("Hola %s" %numero)
                    n3="ACERTASTE"
                    #return HttpResponse(" %s " %acertados)   
                if val4==numero4:
                    #return HttpResponse("Hola %s" %numero)
                    n4="ACERTASTE"
                    #return HttpResponse(" %s " %acertados)
                    
                    
                if val1==numero2:
                    #return HttpResponse("Hola %s" %numero)
                    n2="CASI"
                    #return HttpResponse(" %s " %acertados)
                if val2==numero1:
                    #return HttpResponse("Hola %s" %numero)
                    n1="CASI"
                    #return HttpResponse(" %s " %acertados)
                if val3==numero1:
                    #return HttpResponse("Hola %s" %numero)
                    n1="CASI"
                    #return HttpResponse(" %s " %acertados)
                if val4==numero1:
                    #return HttpResponse("Hola %s" %numero)
                    n1="CASI"
                    #return HttpResponse(" %s " %acertados)
                if val1==numero3:
                    #return HttpResponse("Hola %s" %numero)
                    n3="CASI"
                    #return HttpResponse(" %s " %acertados)
                if val2==numero3:
                    #return HttpResponse("Hola %s" %numero)
                    n3="CASI"
                    #return HttpResponse(" %s " %acertados)
                if val3==numero2:
                    #return HttpResponse("Hola %s" %numero)
                    n2="CASI"
                    #return HttpResponse(" %s " %acertados)
                if val4==numero2:
                    #return HttpResponse("Hola %s" %numero)
                    n2="CASI"
                    #return HttpResponse(" %s " %acertados)
                if val4==numero3:
                    #return HttpResponse("Hola %s" %numero)
                    n3="CASI"
                    #return HttpResponse(" %s " %acertados)
                if val1==numero4:
                    #return HttpResponse("Hola %s" %numero)
                    n4="CASI"
                    #return HttpResponse(" %s " %acertados)
                if val2==numero4:
                    #return HttpResponse("Hola %s" %numero)
                    n4="CASI"
                    #return HttpResponse(" %s " %acertados)
                if val3==numero4:
                    #return HttpResponse("Hola %s" %numero)
                    n4="CASI"
                    #return HttpResponse(" %s " %acertados)
    ### si todos son ACERTASTE, guarda en intentos el numero de la lista, luego elimina la lista numeros_guardados y lista_resultados
                #cuando el primero acierta tiene contador, los otros que acierten no
                if n1=="ACERTASTE" and n2=="ACERTASTE" and n3=="ACERTASTE" and n4=="ACERTASTE":
                    if ganador[0]==1:
                        ganador[0]=3
                        #ganador=False
                        intentos=len(numeros_guardados)
                        del numeros_guardados[:]
                        del lista_resultados[:]
                        #number.iniciar(None,None,None,None)
                        print(ganador)
                        print(intentos)
                        print(numeros_guardados)
                        print(lista_resultados)
                        ### pintamos html con los numeros ACERTASTE, numero de partida y la cantidad de intentos
                        return HttpResponse("<html><body><br>ACERTASTE EL NÚMERO: %s-%s-%s-%s </br><br>EN: %s INTENTOS</br><br>PARTIDA NÚMERO: %s</br>#######################################</body></html>" % (numero1,numero2,numero3,numero4,intentos,partida))
                        #return HttpResponse("<html><body><br>ACERTASTE LOS CUATRO en %s INTENTOS</br>###########</body></html>" % len(numeros_guardados))    
                    else:

                        intentos=len(numeros_guardados)
                        del numeros_guardados[:]
                        del lista_resultados[:]
                        
                        print(ganador)
                        print(intentos)
                        print(numeros_guardados)
                        print(lista_resultados)
                        ### pintamos html con los numeros ACERTASTE, numero de partida y la cantidad de intentos
                        return HttpResponse("<html><body><br>ACERTASTE EL NÚMERO: %s-%s-%s-%s </br>FUÉ ACERTADO ANTES,NO HAY CONTADOR DE INTENTOS<br></br><br>PARTIDA NÚMERO: %s</br>#######################################</body></html>" % (numero1,numero2,numero3,numero4,partida))
                        
                        return HttpResponse("DDDDDD")
                acertados=n1 + "-" + n2 + "-" + n3 + "-" + n4
                acertados2=n1 + "-" + n2 + "-" + n4 + "-" + n3
                acertados3=n1 + "-" + n3 + "-" + n2 + "-" + n4
                acertados4=n1 + "-" + n3 + "-" + n4 + "-" + n2
                acertados5=n1 + "-" + n4 + "-" + n2 + "-" + n3
                acertados6=n1 + "-" + n4 + "-" + n3 + "-" + n2
                
                acertados7=n2 + "-" + n1 + "-" + n3 + "-" + n4
                acertados8=n2 + "-" + n1 + "-" + n4 + "-" + n3
                acertados9=n2 + "-" + n3 + "-" + n4 + "-" + n1
                acertados10=n2 + "-" + n3 + "-" + n1 + "-" + n4
                acertados11=n2 + "-" + n4 + "-" + n1 + "-" + n3
                acertados12=n2 + "-" + n4 + "-" + n3 + "-" + n1
                
                acertados13=n3 + "-" + n1 + "-" + n2 + "-" + n4
                acertados14=n3 + "-" + n1 + "-" + n4 + "-" + n2
                acertados15=n3 + "-" + n2 + "-" + n1 + "-" + n4
                acertados16=n3 + "-" + n2 + "-" + n4 + "-" + n1
                acertados17=n3 + "-" + n4 + "-" + n1 + "-" + n2
                acertados18=n3 + "-" + n4 + "-" + n2 + "-" + n1
                
                acertados19=n4 + "-" + n1 + "-" + n2 + "-" + n3
                acertados20=n4 + "-" + n1 + "-" + n3 + "-" + n2
                acertados21=n4 + "-" + n2 + "-" + n1 + "-" + n3
                acertados22=n4 + "-" + n2 + "-" + n3 + "-" + n1
                acertados23=n4 + "-" + n3 + "-" + n1 + "-" + n2
                acertados24=n4 + "-" + n3 + "-" + n2 + "-" + n1
                
                #acertados=random.choice(["n1,n2,n3"])
    ### en resultado se guarda lista de acertados con todas las combinaciones y aplicando una eleccion aleatoria
    ### de esta forma evitamos que las columnas(resultado-numero) coincida, puede coincidir o no
                resultado=random.choice([acertados,acertados2,acertados3,acertados4,acertados5,acertados6,acertados7,
                acertados8,acertados9,acertados10,acertados11,acertados12,acertados13,acertados14,acertados15,
                acertados16,acertados17,acertados18,acertados19,acertados20,acertados21,acertados22,acertados23,acertados24])
    ### el resultado se va almacenando en ista_resultados
                lista_resultados.append(resultado)
### se enumeran lista_resultados y numeros_guardados, se muestran en html  
            except:
                #print(number)
                print("HAY QUE INGRESAR NÚMERO SECRETO PRIMERO,/INGRESO/X/X/X/X")
                return HttpResponse("<html><body><br>HAY QUE INGRESAR NÚMERO SECRETO PRIMERO: </br><br>IR A : /INGRESO/X/X/X/X</br></body></html>")
            return HttpResponse("<html><body><br>%s </br>###########PARTIDA: %s<br>%s </br></body></html>" %(list(enumerate(lista_resultados)),partida,list(enumerate(numeros_guardados))))
        return HttpResponse(" Los números tienen que ser distintos entre sí ")
    return HttpResponse(" Los números tienen que ser del 0 al 9 ")
    
   