import time
import threading
rango= 1000
hilo1 = 0
hilo2 = 0
acumulador = 0
protected = threading.Lock()
def restador(t,operacion):
    global acumulador
    global hilo1
    global hilo2
    global rango
    estado = True 
    while estado:
           
             
            
            if(rango <= 0):
               print("fin")
               print(f"hilo1= {hilo1} ; hilo2= {hilo2}")
               estado = False
            else:  
                if t=="1":
                    hilo1 +=1
                else:
                    hilo2 +=1
                with protected:
                    if operacion == "suma":
                        acumulador += 1
                        print(f"Soy el hilo {t} y estoy sumando")
                    else:
                        acumulador -= 1
                        print(f"Soy el hilo {t} y estoy restando")
                
                
                rango -= 1
         
            print(f"rango = {rango}")
           
   


momento_arranque = time.perf_counter()
t1= "1"
t2 = "2"
operacion1 = "suma"
operacion2 = "resta"
thr1 = threading.Thread(target=restador, args=(t1,operacion1))

thr2 = threading.Thread(target=restador, args=(t2,operacion2))
thr2.start()
thr1.start()


thr1.join()
thr2.join()
momento_parada = time.perf_counter()

print(f'El valor final es: {acumulador}')
print(f'Tomó {momento_parada - momento_arranque:0.5f} segundos')
print(f'cantidad de th1 =  {hilo1} ;  cantidad de th2 = {hilo2}')
