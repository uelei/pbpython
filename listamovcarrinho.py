#!/usr/bin/python
# -*- coding: utf-8 -*-
#Arquivo: pbbd.py

import pygtk
pygtk.require("2.0")
import gtk
import gtk.glade
from conbd import con
import datetime
from datetime import datetime
from addprodtroca import addpro

n = datetime.now()
ns = str(n)
nl= ns.split('-')
ano = nl[0]
mes = nl[1]



class listamovcarrinho:
   def __init__(self):

#Carrega a interface a partir do arquivo glade
     aw = gtk.glade.XML('listamovcarrinho.glade')
#carrega os widgets 
#janela principal
     self.jamovcarrinho = aw.get_widget('jlistamovcarrinho')
     self.listaprodutosvendidos = aw.get_widget('treeview1')
     self.listaprodutosvendidosdois = aw.get_widget('treeview2')
     self.dataipb= aw.get_widget('entry1')
     self.datafpb= aw.get_widget('entry2')
     self.dataipk= aw.get_widget('entry4')
     self.datafpk= aw.get_widget('entry5')
     self.edmes = aw.get_widget('entry7') 
     self.tpb = aw.get_widget('entry3')
     self.tpk = aw.get_widget('entry6')

#Conecta todos os Sinais aos Callbacks
     aw.signal_autoconnect(self)

#Exibe janela principalpb
     self.jamovcarrinho.show_all()

#Inicia o loop principal de eventos (GTK MainLoop)
     
     gtk.main()

   def inicio(self,widget):
      me = "01-" + mes +"-" + ano
      mf =  "31-" +mes + "-" + ano 
      self.dataipb.set_text(me)
      self.datafpb.set_text(mf)
      self.dataipk.set_text(me)
      self.datafpk.set_text(mf)
      self.listarprodutosvendidos(self)

   def addprod(self,widget):
      addpro()      



   def listarprodutosvendidos(self,data):
      ncolunas = self.listaprodutosvendidos.get_columns()
      tpb= 0
      tpk =0 
      cdipb = self.dataipb.get_text()
      cdipb_c = cdipb[3:]
      cdipb_s = cdipb_c.split('-')
      mesipb = cdipb_s[0]
      anoipb = cdipb_s[1]

      cdfpb = self.datafpb.get_text()
      cdfpb_c = cdfpb[3:]
      cdfpb_s = cdfpb_c.split('-')
      mesfpb = cdfpb_s[0]
      anofpb = cdfpb_s[1]

      cdipk = self.dataipk.get_text()
      cdipk_c = cdipk[3:]
      cdipk_s = cdipk_c.split('-')
      mesipk = cdipk_s[0]
      anoipk = cdipk_s[1]

      cdfpk = self.datafpk.get_text()
      cdfpk_c = cdfpk[3:]
      cdfpk_s = cdfpk_c.split('-')
      mesfpk = cdfpk_s[0]
      anofpk = cdfpk_s[1]

      for col in ncolunas:
         self.listaprodutosvendidos.remove_column(col)  
      self.tipodetabelavenda = gtk.ListStore(str,str,str,str,str,str,str,str)
      self.listaprodutosvendidos.set_model(self.tipodetabelavenda)
      self.listaprodutosvendidos.append_column(gtk.TreeViewColumn("n_not_int",gtk.CellRendererText(), text=0))
      self.listaprodutosvendidos.append_column(gtk.TreeViewColumn("cod_prod",gtk.CellRendererText(), text=1))
      self.listaprodutosvendidos.append_column(gtk.TreeViewColumn("descricao",gtk.CellRendererText(), text=2))      
      self.listaprodutosvendidos.append_column(gtk.TreeViewColumn("quantidade",gtk.CellRendererText(), text=3))      
      self.listaprodutosvendidos.append_column(gtk.TreeViewColumn("preco_c",gtk.CellRendererText(), text=4))      
      self.listaprodutosvendidos.append_column(gtk.TreeViewColumn("pc_s",gtk.CellRendererText(), text=5))
      self.listaprodutosvendidos.append_column(gtk.TreeViewColumn("grade_sel",gtk.CellRendererText(), text=6))
      self.listaprodutosvendidos.append_column(gtk.TreeViewColumn("data_sel",gtk.CellRendererText(), text=7))
      cod_mov = "102"
      selpvendidos=con.cursor()
      selpvendidos.execute("SELECT * FROM tb_mov_merc WHERE cod_mov='"+cod_mov+"' AND data_sel > '"+anoipb+"-"+mesipb+"-01 00:00:00' AND data_sel < '"+anofpb+"-"+mesfpb+"-31 00:00:00'")
      pvend = selpvendidos.fetchall()
      for pdv in pvend:
         selpro=con.cursor()
         selpro.execute("SELECT * FROM pbestoreal WHERE codigo='"+str(pdv[2])+"'")	
         linp = selpro.fetchone()
         dp = linp[2]
         cb=linp[1]
         self.tipodetabelavenda.append([pdv[1],pdv[2],dp,pdv[3],pdv[4],pdv[6],pdv[8],pdv[11]])
         tpb = tpb + pdv[6]
      self.tpb.set_text(str(tpb))
     
      


      ncolunas = self.listaprodutosvendidosdois.get_columns()
      for col in ncolunas:
         self.listaprodutosvendidosdois.remove_column(col)  
      self.tipodetabelavenda = gtk.ListStore(str,str,str,str,str,str,str,str)
      self.listaprodutosvendidosdois.set_model(self.tipodetabelavenda)
      self.listaprodutosvendidosdois.append_column(gtk.TreeViewColumn("n_not_int",gtk.CellRendererText(), text=0))
      self.listaprodutosvendidosdois.append_column(gtk.TreeViewColumn("cod_prod",gtk.CellRendererText(), text=1))
      self.listaprodutosvendidosdois.append_column(gtk.TreeViewColumn("descricao",gtk.CellRendererText(), text=2))      
      self.listaprodutosvendidosdois.append_column(gtk.TreeViewColumn("quantidade",gtk.CellRendererText(), text=3))      
      self.listaprodutosvendidosdois.append_column(gtk.TreeViewColumn("preco_c",gtk.CellRendererText(), text=4))      
      self.listaprodutosvendidosdois.append_column(gtk.TreeViewColumn("pc_s",gtk.CellRendererText(), text=5))
      self.listaprodutosvendidosdois.append_column(gtk.TreeViewColumn("grade_sel",gtk.CellRendererText(), text=6))
      self.listaprodutosvendidosdois.append_column(gtk.TreeViewColumn("data_sel",gtk.CellRendererText(), text=7))
      cod_mov = "201"
      selpvendidos=con.cursor()
      selpvendidos.execute("SELECT * FROM tb_mov_merc WHERE cod_mov='"+cod_mov+"' AND data_sel > '"+anoipk+"-"+mesipk+"-01 00:00:00' AND data_sel < '"+anofpk+"-"+mesfpk+"-31 00:00:00'")
      pvend = selpvendidos.fetchall()
      for pdv in pvend:
         selpro=con.cursor()
         selpro.execute("SELECT * FROM pbestoreal WHERE codigo='"+str(pdv[2])+"'")	
         linp = selpro.fetchone()
         dp = linp[2]
         cb=linp[1]
         self.tipodetabelavenda.append([pdv[1],pdv[2],dp,pdv[3],pdv[4],pdv[6],pdv[8],pdv[11]])
         tpk = tpk + pdv[6]
      self.tpk.set_text(str(tpk))
      

    
#Callbacks = acoes
if __name__ == "__main__":
  listamovcarrinho()

