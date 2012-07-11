# -*- coding: UTF-8 -*-
class Lampadas:
  nLampadas = 0
  vLampadas = 0
  ioLampadas = 0
  i = 0
  idas = 0
  def __init__(self, nLampadas, i, idas):
    self.nLampadas = nLampadas
    self.i = i
    self.idas = idas
    print("Objeto Lampadas instanciado")
    
  def inicializaVetor (self):
    self.vLampadas = range(1, self.nLampadas+1)  # Quantidade de Lâmpadas
    self.ioLampadas = range(1, self.nLampadas+1) # Lampadas que estao Ligadas Desligadas
    
    for lampada in self.vLampadas:
      self.ioLampadas[lampada-1] = False      # Todas as lampadas desligadas
    
    print("Todas as lampadas estão desligadas")
    
  def percorreCorredor(self):
    for ida in range(1, self.idas+1):
      if ida != self.i:
        for ioLampada in self.vLampadas:
          if self.vLampadas[ioLampada-1] == False:
            self.vLampadas[ioLampada-1] = True
          else:
            self.vLampadas[ioLampada-1] = False
      else:
        for ioLampada in self.vLampadas:
          if self.vLampadas[ioLampada-1] % self.i == 0:
            if self.vLampadas[ioLampada-1] == False:
              self.vLampadas[ioLampada-1] = True
            else:
              self.vLampadas[ioLampada-1] = False
            print("Alterado a posição %s") % self.i
            
    print self.ioLampadas
      
