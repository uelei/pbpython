#!/usr/bin/python
# -*- coding: utf-8 -*-
#Arquivo: main.py
try:
   import pygtk
   pygtk.require("2.0")
except:
   pass
try:
   print "importando GTK"
   import gtk
   print "importando GTK + glade"
   import gtk.glade
   print "importando MYSQL"
   from conbd import con
   print "importando sistema"
   import sys
   print "importando data"
   import datetime
   print "importando hora"
   from datetime import datetime
 
except:
   print "impossivel carregar as bibliotecas "
   exit(1)







class pbprin:
   def __init__(self):
#Carrega a interface a partir do arquivo glade
    aw = gtk.glade.XML('pbprinc.glade')
#carrega os widgets 
#janela principal
    janelaprincipal = aw.get_widget('window1')
    button = aw.get_widget('button1')
#Conecta todos os Sinais aos Callbacks
    aw.signal_autoconnect(self)
#Exibe janela principalpb
    janelaprincipal.show_all()
#Inicia o loop principal de eventos (GTK MainLoop)
    gtk.main()
    
   def abrejamovcarrinho(self,widget):
     print "importando janela carrinho mov "
     from listamovcarrinho import listamovcarrinho
     listamovcarrinho()

   def sair(self,widget,data):
    con.close()   
    #print "sair"
    gtk.main_quit()
    exit(0)

   def sairr(self,widget):
    con.close()   
    #print "sairr"
    gtk.main_quit()
    exit(0)
    
   def abrejanelaproduto(self,widget):
     print "importando produto"
     from prod import japroduto
     self.a = japroduto()
   def abrevenda(self,widget):
     print "importando janela venda "
     from vendag import venda 
     self.b = venda()
   def abrecx(self,widget):
      print "importando janela caixa "
      from caixa import caixa
      self.e = caixa()
   def abrepgc(self,widget):
      print "importando janela pg conta"
      from pgconta import pgconta
      self.f = pgconta()
  
   def abratotalv(self,widget):
      print "importando janela total de venda "
      from totalvendas import total
      self.c = total()
   def abreentra(self,widget):
      print "importando janela entrada "
      from entrada import entrada
      self.d = entrada()
   def abrepgap(self,widget):
      print "importando janela contas a pagar"
      from pgcontanaoefe import pgcontaap
      self.g = pgcontaap()
   def dpnpg(self,widget):
     print "importando janela pagar duplicatas em aberto"
     from apagar import apagar
     self.h = apagar()

#Callbacks = acoes
if __name__ == "__main__":
   
   pbprin()


print "programa pb finalizado. "

