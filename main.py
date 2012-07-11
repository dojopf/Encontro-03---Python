# -*- coding: UTF-8 -*-

from lampadas import Lampadas

def main():
  while True:
    while True:
      try:
        idas = int(input("Numero de idas: "))
        numeroLampadas = int(input("Numero de lampadas: "))
        divisor = int(input("Divisor: "))        
        #idas = 3
        #numeroLampadas = 10
        #divisor = 2
        break
        
      except:
        print("Sua mula!!")
        
    joao = Lampadas(numeroLampadas, divisor, idas)
    
    joao.inicializaVetor()
    joao.percorreCorredor()
  
if __name__ == "__main__":
  main()
    
