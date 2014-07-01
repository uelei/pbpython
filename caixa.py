#!/usr/bin/python
# -*- coding: utf-8 -*-
#Arquivo: caixa.py

import pygtk
pygtk.require("2.0")
import gtk
import gtk.glade
from conbd import con
import datetime
import time
from datetime import datetime

ano, mes, dia, hora, minuto, segundo, semana, juliano, verao= time.localtime()

class caixa:
   def __init__(self):
      
#Carrega a interface a partir do arquivo glade
     aw = gtk.glade.XML('caixa.glade')
#carrega os widgets 
#janela principal
     self.jacaixa = aw.get_widget('window1')
     self.edcxl = aw.get_widget('entry1')
     self.edpas = aw.get_widget('entry2')
     self.edit = aw.get_widget('entry3')
     self.edbb = aw.get_widget('entry4')
     self.edun = aw.get_widget('entry5')
     self.edch = aw.get_widget('entry6')
     self.btatu = aw.get_widget('button1')
     self.eddata = aw.get_widget('entry7')  
     self.edpai = aw.get_widget('entry8')
     self.rbdia = aw.get_widget('radiobutton1')
     self.rbmes = aw.get_widget('radiobutton2')
     self.listacx = aw.get_widget('treeview1') 
     self.check = aw.get_widget('checkbutton1')

#janela de calendario 
     self.janelacalendario = aw.get_widget('window2')
     self.caljanela = aw.get_widget('calendar1')   









#seta valores 


     self.edcxl.grab_focus()
     d= "0"+str(dia)
     data=str(d[-2:])+"/"+str(mes)+"/"+str(ano)
     self.eddata.set_text(data)

#Conecta todos os Sinais aos Callbacks
     aw.signal_autoconnect(self)

#Exibe janela principalpb
     self.jacaixa.show_all()

#Inicia o loop principal de eventos (GTK MainLoop)
     
     gtk.main()

   def dataget(self):
      edd=str(self.eddata.get_text())   
      eedd=edd.split('/')
      eedda= eedd[2]
      eeddm= eedd[1]
      eeddm = "0"+ eedd[1]
      eeddm = eeddm[-2:]
      
      eeddd= eedd[0]
      eeddd = "0"+ eeddd
      eeddd = eeddd[-2:]
      eddf= eedda+'-'+eeddm+'-'+eeddd
      eddff= eedda+"/"+eeddm+"/"+eeddd
      return eddf
 
   def abrecal(self,widget,data):
      self.janelacalendario.show_all()
      
 
   def fecharjanelacalendario(self,widget,data):
      self.janelacalendario.hide()
      #self.btatu.grab_focus()
      return True 

  

   def fechajanelacalendario(self,widget):
      self.janelacalendario.hide()
      data = self.caljanela.get_date()
      ms=data[1]+1
      mes="0"+str(ms)
      mes= mes[-2:]
      d=data[2]
      dia="0"+str(d)
      #dt=str(data[0])+"-"+str(mes[-2:])+"-"+str(dia[-2:])
      dt = str(dia[-2:])+"/"+str(mes)+"/"+str(data[0])
      self.eddata.set_text(dt)
      #self.btatu.grab_focus()
      self.atualcx(self)


   def resumo(self,widget):
           #campo cx loja
           data = self.dataget()
           selcx=con.cursor()
           da = data.split('-')
           ano = da[0]
           mes = da[1]
           dia = da[2]

           if self.rbdia.get_active():
              #dt=dia[-2:]+"/"+str(mes[-2:])+"/"+str(data[0])
              dt = str(ano) + "-" + str(mes)+"-"+str(dia)
           elif self.rbmes.get_active():
              #dt="/"+str(mes[-2:])+"/"+str(data[0])
              dt = str(ano) + "-" + str(mes)+"-"
           else:
              #dt="/"+str(data[0])
              dt = "20" 
           #criando o grid 
           ncolunas = self.listacx.get_columns()
           for col in ncolunas:
              self.listacx.remove_column(col)  
           self.tipodetabela = gtk.ListStore(str,str,str,str,str,str,str,str,str,str)
           self.listacx.set_model(self.tipodetabela)
           self.listacx.append_column(gtk.TreeViewColumn("desc_mov",gtk.CellRendererText(), text=0))
           self.listacx.append_column(gtk.TreeViewColumn("cx_lj",gtk.CellRendererText(), text=1))
           self.listacx.append_column(gtk.TreeViewColumn("pasta",gtk.CellRendererText(), text=2))      
           self.listacx.append_column(gtk.TreeViewColumn("bb",gtk.CellRendererText(), text=3))      
           self.listacx.append_column(gtk.TreeViewColumn("itau_pb",gtk.CellRendererText(), text=4))      
           self.listacx.append_column(gtk.TreeViewColumn("itau",gtk.CellRendererText(), text=5))
           self.listacx.append_column(gtk.TreeViewColumn("pai",gtk.CellRendererText(), text=6))
           self.listacx.append_column(gtk.TreeViewColumn("cheque",gtk.CellRendererText(), text=7))
           self.listacx.append_column(gtk.TreeViewColumn("data",gtk.CellRendererText(), text=8))
           self.listacx.append_column(gtk.TreeViewColumn("efetivado",gtk.CellRendererText(), text=9))
           din = 0
           ch = 0
           myvd=con.cursor()    
           myvd.execute("SELECT * FROM tb_vendas WHERE  datatime LIKE '%"+str(dt)+"%' AND `cod_pg`='1'")
           rsd= myvd.fetchall()
           for vd in rsd:
              din=din+vd[2]           
           myvd=con.cursor()    
           myvd.execute("SELECT * FROM tb_vendas WHERE  datatime LIKE '%"+str(dt)+"%' AND `cod_pg`='3'")
           rsd= myvd.fetchall()
           for vd in rsd:
              ch=ch+vd[2]
           self.tipodetabela.append(['vendas do dia',din,' ',' ',' ',' ',' ',ch,str(dt),str(dt)])
           seldmov =con.cursor()
           seldmov.execute("SELECT * FROM tb_desmov")
           rsmov = seldmov.fetchall()
 
           for dmov in rsmov:
               codmov = dmov[0]   
               desmov = dmov[1]
               cx = 0
               pa = 0 
               bb= 0 
               un = 0
               it= 0 
               pi =0
               ch = 0
               t=0
               selv = con.cursor()
               
               selv.execute("SELECT * FROM tb_ctrl_cx WHERE `cod_des`='"+str(codmov)+"' AND `defe` LIKE '%"+str(dt)+"%' ")
               rsd= selv.fetchall()
               for va in rsd:
                  cod_pg = int(va[2])
                 
                    
                  if cod_pg ==1:
                      cx = cx + va[3]
                  if cod_pg ==2:
                      pa = pa + va[3]
                  if cod_pg ==3:
                      bb = bb + va[3]
                  if cod_pg ==4:
                      un = un +va[3]
                  if cod_pg ==5:
                      it = it +va[3]
                  if cod_pg ==6:
                      ch =ch + va[3] 
                  if cod_pg ==7:
                      pi = pi +va[3]
               
               t = cx+ pa + bb+ un+ it+ch+pi
               
               #self.tipodetabela.append([desmov,cx,pa,bb,un,it,pi,ch,dt,dt])
               if codmov ==29:
                    self.tipodetabela.append([desmov,cx,pa,bb,un,it,pi,ch,dt,dt])
               else :
                  if t !=0:
                      self.tipodetabela.append([desmov,cx,pa,bb,un,it,pi,ch,dt,dt]) 
    
   def atualcx(self,widget):
           #campo cx loja
           data = self.dataget()
           selcx=con.cursor()
           da = data.split('-')
           ano = da[0]
           mes = da[1]
           dia = da[2]

           if self.rbdia.get_active():
              #dt=dia[-2:]+"/"+str(mes[-2:])+"/"+str(data[0])
              dt = str(ano) + "-" + str(mes)+"-"+str(dia)
           elif self.rbmes.get_active():
              #dt="/"+str(mes[-2:])+"/"+str(data[0])
              dt = str(ano) + "-" + str(mes)+"-"
           else:
              #dt="/"+str(data[0])
              dt = str(ano) + "-" 
           
           selcx.execute("SELECT * FROM tb_ctrl_cx WHERE `cod_pg`='"+str(1)+"' AND `defe` LIKE '%"+str(dt)+"%' ")
           rsd= selcx.fetchall()
           v=0
           din = 0
           ch = 0 
           for va in rsd:
              v=v+va[3]
           myvd=con.cursor()    
           myvd.execute("SELECT * FROM tb_vendas WHERE  datatime LIKE '%"+str(dt)+"%' AND `cod_pg`='1'")
           rsd= myvd.fetchall()
           for vd in rsd:
              din=din+vd[2]
           vf = v+ din

           self.edcxl.set_text(str(vf))
           #campo pasta
           selcx=con.cursor()
           selcx.execute("SELECT * FROM tb_ctrl_cx WHERE cod_pg='"+str(2)+"' AND `defe` LIKE '%"+str(dt)+"%'")
           rsd= selcx.fetchall()
           v=0
           for va in rsd:
              v=v+va[3]
           self.edpas.set_text(str(v))
           #campo itau
           selcx=con.cursor()
           selcx.execute("SELECT * FROM tb_ctrl_cx WHERE cod_pg='"+str(3)+"' AND `defe` LIKE '%"+str(dt)+"%'")
           rsd= selcx.fetchall()
           v=0
           for va in rsd:
              v=v+va[3]
           self.edit.set_text(str(v))
           #campo bb
           selcx=con.cursor()
           selcx.execute("SELECT * FROM tb_ctrl_cx WHERE cod_pg='"+str(4)+"' AND `defe` LIKE '%"+str(dt)+"%'")
           rsd= selcx.fetchall()
           v=0
           for va in rsd:
              v=v+va[3]
           self.edbb.set_text(str(v))
           #campo itau_pb
           selcx=con.cursor()
           selcx.execute("SELECT * FROM tb_ctrl_cx WHERE cod_pg='"+str(5)+"' AND `defe` LIKE '%"+str(dt)+"%'")
           rsd= selcx.fetchall()
           v=0
           for va in rsd:
              v=v+va[3]
           self.edun.set_text(str(v))
           #campo pai
           selcx=con.cursor()
           selcx.execute("SELECT * FROM tb_ctrl_cx WHERE cod_pg='"+str(7)+"' AND `defe` LIKE '%"+str(dt)+"%'")
           rsd= selcx.fetchall()
           v=0
           for va in rsd:
              v=v+va[3]
           self.edpai.set_text(str(v))
           #campo cheque
           selcx=con.cursor()
           selcx.execute("SELECT * FROM tb_ctrl_cx WHERE cod_pg='"+str(6)+"' AND `defe` LIKE '%"+str(dt)+"%'")
           rsd= selcx.fetchall()
           v=0
           for va in rsd:
              v=v+va[3]
           myvd=con.cursor()    
           myvd.execute("SELECT * FROM tb_vendas WHERE  datatime LIKE '%"+str(dt)+"%' AND `cod_pg`='3'")
           rsd= myvd.fetchall()
           for vd in rsd:
              ch=ch+vd[2]
           vf = v+ ch
           self.edch.set_text(str(vf))
           seltudo = con.cursor()
           seltudo.execute("SELECT * FROM tb_ctrl_cx WHERE defe LIKE '%"+str(dt)+"%' OR `data` LIKE '%"+str(dt)+"%' AND cod_pg = '0'  ORDER BY `data` ASC ")
           selt = seltudo.fetchall()
           ncolunas = self.listacx.get_columns()
           for col in ncolunas:
              self.listacx.remove_column(col)  
           self.tipodetabela = gtk.ListStore(str,str,str,str,str,str,str,str,str,str)
           self.listacx.set_model(self.tipodetabela)
           self.listacx.append_column(gtk.TreeViewColumn("desc_mov",gtk.CellRendererText(), text=0))
           self.listacx.append_column(gtk.TreeViewColumn("cx_lj",gtk.CellRendererText(), text=1))
           self.listacx.append_column(gtk.TreeViewColumn("pasta",gtk.CellRendererText(), text=2))      
           self.listacx.append_column(gtk.TreeViewColumn("bb",gtk.CellRendererText(), text=3))      
           self.listacx.append_column(gtk.TreeViewColumn("itau_pb",gtk.CellRendererText(), text=4))      
           self.listacx.append_column(gtk.TreeViewColumn("itau",gtk.CellRendererText(), text=5))
           self.listacx.append_column(gtk.TreeViewColumn("pai",gtk.CellRendererText(), text=6))
           self.listacx.append_column(gtk.TreeViewColumn("cheque",gtk.CellRendererText(), text=7))
           self.listacx.append_column(gtk.TreeViewColumn("data",gtk.CellRendererText(), text=8))
           self.listacx.append_column(gtk.TreeViewColumn("efetivado",gtk.CellRendererText(), text=9))
           self.tipodetabela.append(['vendas do dia',din,' ',' ',' ',' ',' ',ch,str(dt),str(dt)])
           for tdo in selt:
              codpg = tdo[2] 
              codmov = tdo[1]
              valor = tdo[3]
              data = tdo[5]
              defe = tdo[6]
              seldmov =con.cursor()
              seldmov.execute("SELECT * FROM tb_desmov WHERE si='"+str(codmov)+"'")
              lin = seldmov.fetchone()
              descmov = str(lin[1])

              if defe != "":
                 if defe =="nao":
                    defe = "nao recebido !"
                 else:
                    defe ="ok"
              else : 
                 defe = "pendende "

              if codpg == 1 :
                 self.tipodetabela.append([descmov,valor,' ',' ',' ',' ',' ',' ',data,defe])
              if codpg == 2 :
                 self.tipodetabela.append([descmov,' ',valor,' ',' ',' ',' ',' ',data,defe])
              if codpg == 3 :
                 self.tipodetabela.append([descmov,' ',' ',valor,' ',' ',' ',' ',data,defe])
              if codpg == 4 :
                 self.tipodetabela.append([descmov,' ',' ',' ',valor,' ',' ',' ',data,defe])
              if codpg == 5 :
                 self.tipodetabela.append([descmov,' ',' ',' ',' ',valor,' ',' ',data,defe])
              if codpg == 6 :
                 self.tipodetabela.append([descmov,' ',' ',' ',' ',' ',' ',valor,data,defe])
              if codpg == 7 :
                 self.tipodetabela.append([descmov,' ',' ',' ',' ',' ',valor,' ',data,defe])
              if codpg == 0 :
                 self.tipodetabela.append([descmov,valor,' ',' ',' ',' ',' ',' ',data,defe])
              # self.tipodetabelavenda.append([pdv[2],cb,dp,pdv[3],pdv[5],pdv[7],pdv[8]])
           

 
           

if __name__ == "__main__":
   caixa()

