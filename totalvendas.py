#!/usr/bin/python
# -*- coding: utf-8 -*-
#Arquivo: totalvendas.py

import pygtk
import gtk
import gtk.glade
from conbd import con

class total :
   def __init__(self):

    aw = gtk.glade.XML('totalvendas.glade')

    self.janelatotalvendas = aw.get_widget('janelatotalvendas')

    self.tabelatotalvendas= aw.get_widget('treeview')
    self.calendar = aw.get_widget('calendar1')
    self.rbdia = aw.get_widget('rdtotaldia')
    self.rbmes = aw.get_widget('rdtotalmes')
    self.rbano = aw.get_widget('rdtotalano')

#Conecta todos os Sinais aos Callbacks
    aw.signal_autoconnect(self)

#Exibe janela principalpb
    self.janelatotalvendas.show_all()

#Inicia o loop principal de eventos (GTK MainLoop)
    gtk.main()

   def fechartotalvendas(self,widget,data):
      self.janelatotalvendas.hide()
      return True
   def abrejanelacalendario(self,widget,data):
      self.janelacalendario.show_all()
 
      
      
   def fecharjanelavendas(self,widget,data):
      self.janelavenda.hide()
      return True
   def fecharjanelacalendario(self,widget,data):
      self.janelacalendario.hide()
      self.ednumvendedor.grab_focus()
      return True
   def fechajanelacalendario(self,widget):
      self.janelacalendario.hide()
      data = self.caljanela.get_date()
      ms=data[1]+1
      mes="0"+str(ms)
      d=data[2]
      dia="0"+str(d)
      dt=str(data[0])+"-"+str(mes[-2:])+"-"+str(dia[-2:])
      self.eddata.set_text(dt)
      self.ednumvendedor.grab_focus()
      return True
   def somatotalvendas(self,widget):
    ncol = self.tabelatotalvendas.get_columns()
    for col in ncol:
     self.tabelatotalvendas.remove_column(col) 
    self.tipodetabela = gtk.ListStore(str,str,str,str,str,str)
    self.tabelatotalvendas.set_model(self.tipodetabela)
    self.tabelatotalvendas.append_column(gtk.TreeViewColumn("vendedor",gtk.CellRendererText(), text=0))
    self.tabelatotalvendas.append_column(gtk.TreeViewColumn("pecas",gtk.CellRendererText(), text=1))
    self.tabelatotalvendas.append_column(gtk.TreeViewColumn("diheiro",gtk.CellRendererText(), text=2))
    self.tabelatotalvendas.append_column(gtk.TreeViewColumn("cartao",gtk.CellRendererText(), text=3))
    self.tabelatotalvendas.append_column(gtk.TreeViewColumn("cheque",gtk.CellRendererText(), text=4))
    self.tabelatotalvendas.append_column(gtk.TreeViewColumn("total",gtk.CellRendererText(), text=5))

    dint=0
    cart=0
    chet=0
    ttt=0
    tpc=0
    myvor= con.cursor()
    myvor.execute("SELECT * FROM vendedores")
    tt=0
    myrvor= myvor.fetchall()
    for vendedor in myrvor:
     din=0
     car=0
     che=0
     tt=0
     pc=0
     ven= vendedor[0]
     data = self.calendar.get_date()
     ms=data[1]+1
     mes="0"+str(ms)
     d=data[2]
     dia="0"+str(d)
     if self.rbdia.get_active():
        dt=dia[-2:]+"/"+str(mes[-2:])+"/"+str(data[0])
       #dt = str(data[0]) + "-" + str(mes[-2:])+"-"+dia[-2:]
     elif self.rbmes.get_active():
        dt="/"+str(mes[-2:])+"/"+str(data[0])
       #dt = str(data[0]) + "-" + str(mes[-2:])+"-"
     else:
        dt="/"+str(data[0])
       #dt = str(data[0]) + "-" 
     myvd=con.cursor()    
     myvd.execute("SELECT * FROM tb_vendas WHERE codvend='"+str(ven)+"' AND datav LIKE '%"+str(dt)+"%' AND `cod_pg`='1'")
     rsd= myvd.fetchall()
     for vd in rsd:
        din=din+vd[2]
        pc=pc+vd[8]
     myvc=con.cursor()
     myvc.execute("SELECT * FROM tb_vendas WHERE codvend='"+str(ven)+"' AND datav LIKE '%"+str(dt)+"%' AND `cod_pg` LIKE '%2%'")
     rsc= myvc.fetchall()
     for vc in rsc:
        car=car+vc[2]
        pc=pc+vc[8]
     myvh=con.cursor()
     myvh.execute("SELECT * FROM tb_vendas WHERE codvend='"+str(ven)+"' AND datav LIKE '%"+str(dt)+"%' AND `cod_pg`='3'")
     rsh= myvh.fetchall()
     for vh in rsh:
        che=che+vh[2]
        pc=pc+vh[8]
     tt=din+car+che
     self.tipodetabela.append([ven,pc,din,car,che,tt])
     dint=dint+din
     cart=cart+car
     chet = chet + che
     tpc=tpc+pc
     ttt=ttt+tt 
    self.tipodetabela.append(["subtotal",tpc,dint,cart,chet,ttt])
   def soma(self,widget):
     self.somatotalvendas()
   def fechatotal(self,widget,dados):
      if __name__=="__main__":
         con.close()   
         gtk.main_quit()
         exit(0)

if __name__ == "__main__":
   total()
