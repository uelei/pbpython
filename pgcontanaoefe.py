#!/usr/bin/python
# -*- coding: utf-8 -*-
#Arquivo: pgconta.py

import pygtk
pygtk.require("2.0")
import gtk
import gtk.glade
from conbd import con
import datetime
import time
from datetime import datetime

ano, mes, dia, hora, minuto, segundo, semana, juliano, verao= time.localtime()

class pgcontaap:
   def __init__(self):
      
#Carrega a interface a partir do arquivo glade
     aw = gtk.glade.XML('pgcontaap.glade')
#carrega os widgets 
#janela principal
     self.japgconta = aw.get_widget('window1')
     self.eddata = aw.get_widget('entry2')
     self.cbconta = aw.get_widget('combobox1')
     self.edvalor = aw.get_widget('entry1')
     self.cbcaixa = aw.get_widget('combobox2')
     self.edcconta = aw.get_widget('entry4')
     self.edccx = aw.get_widget('entry5')
     self.cbforn = aw.get_widget('combobox3')
     self.edcforn = aw.get_widget('entry3')
     self.btgrava = aw.get_widget('button1')
     self.edctpg = aw.get_widget('entry6')
     self.cbtpg = aw.get_widget('combobox4')
     self.edndoc  = aw.get_widget('entry8')
     self.edcond = aw.get_widget('entry7')
     self.var = aw.get_widget('entry9')
     self.cbdcx = aw.get_widget('combobox5')
     self.eddcx = aw.get_widget('entry10')
     self.btnovo = aw.get_widget('button2')
     self.chch = aw.get_widget('chch')
#janela de calendario 
     self.janelacalendario = aw.get_widget('window2')
     self.caljanela = aw.get_widget('calendar1')   

#seta valores 

     di="0"+str(dia)
     dd = di[-2:]
     me = "0"+str(mes)
     mm =  me[-2:]
     self.chch.set_active(True)
     data=str(dd)+"/"+str(mm)+"/"+str(ano)
     self.eddata.set_text(data)
     self.cbconta.grab_focus()
     self.criacbdesmov(self)
     self.lcaixas(self)
     self.cbconta.remove_text(0)
     self.cbcaixa.remove_text(0)
     self.cbcaixa.set_active(0)
     self.edccx.set_text("1")
     self.nfor = 0 
     self.edctpg.set_text("1")
     self.eddcx.set_text("1")
     self.cbtpg.remove_text(0)
     self.ltpg(self)
     self.cbtpg.set_active(0)
     self.cbdcx.remove_text(0)
     self.lcxc(self)
     self.cbdcx.set_active(0)
#Conecta todos os Sinais aos Callbacks
     aw.signal_autoconnect(self)
     coa = open('consulta.t','r')
     co = coa.read()
     if co == "1":
         #print "operando no servidor secundario somente consulta"
        
         self.btgrava.set_sensitive(False)
#Exibe janela principalpb
     self.japgconta.show_all()

#Inicia o loop principal de eventos (GTK MainLoop)
     
     gtk.main()

   def dataget(self):
      edd=str(self.eddata.get_text())   
      eedd=edd.split('/')
      eedda= eedd[2]
      eeddm= eedd[1]
      eeddd= eedd[0]
      eddf= eedda+'-'+eeddm+'-'+eeddd
      eddff= eedda+"/"+eeddm+"/"+eeddd
      return eddf
 
   def abrecal(self,widget,data):
      self.janelacalendario.show_all()
      
 
   def fecharjanelacalendario(self,widget,data):
      self.janelacalendario.hide()
      self.cbconta.grab_focus()
      return True 

  

   def fechajanelacalendario(self,widget):
      self.janelacalendario.hide()
      data = self.caljanela.get_date()
      ms=data[1]+1
      mes="0"+str(ms)
      d=data[2]
      dia="0"+str(d)
      #dt=str(data[0])+"-"+str(mes[-2:])+"-"+str(dia[-2:])
      dt = str(dia[-2:])+"/"+str(mes[-2:])+"/"+str(data[0])
      self.eddata.set_text(dt)
      self.cbconta.grab_focus()


   def cbconta_sel(self,widget):
         selpro=con.cursor()
         cbg= self.cbconta.get_active_text()
         ns= str(cbg)
         selpro.execute("SELECT * FROM tb_desmov WHERE descricaodes='"+ns+"'")	
         numlinhas = int(selpro.rowcount)
         if numlinhas ==1:
            linp = selpro.fetchone()
            codmovv=  linp[0]   
            vv = linp[2]
            self.edcconta.set_text(str(codmovv))
            self.var.set_text(str(vv))
            if codmovv == 29 :
               self.cbdcx.set_sensitive(True)
            else :
               self.cbdcx.set_sensitive(False)


            if codmovv == 10 :
               self.cbforn.set_sensitive(True)
               self.lforn(self)
               self.edcforn.set_text('')
            else :
                self.edcforn.set_text('-')
                while self.nfor >= 0 :
                   
                   self.cbforn.remove_text(0)
                   self.nfor = self.nfor -1                     


   def cbtpg_sel(self,widget):
         selpro=con.cursor()
         cbg= self.cbtpg.get_active_text()
         ns= str(cbg)
         selpro.execute("SELECT * FROM tb_tp_conta WHERE des_tp_conta='"+ns+"'")	
         numlinhas = int(selpro.rowcount)
         if numlinhas ==1:
            linp = selpro.fetchone()
            codmovv=  linp[0]   
            self.edctpg.set_text(str(codmovv))

   def cbcaixa_sel(self,widget):
         selpro=con.cursor()
         cbg= self.cbcaixa.get_active_text()
         ns= str(cbg)
         selpro.execute("SELECT * FROM tb_caixas WHERE des_cx='"+ns+"'")	
         numlinhas = int(selpro.rowcount)
         if numlinhas ==1:
            linp = selpro.fetchone()
            codmovv=  linp[0]   
            self.edccx.set_text(str(codmovv))

   def cbcxc_sel(self,widget):
         selpro=con.cursor()
         cbg= self.cbdcx.get_active_text()
         ns= str(cbg)
         selpro.execute("SELECT * FROM tb_caixas WHERE des_cx='"+ns+"'")	
         numlinhas = int(selpro.rowcount)
         if numlinhas ==1:
            linp = selpro.fetchone()
            codmovv=  linp[0]   
            self.eddcx.set_text(str(codmovv))





   def cbforn_sel(self,widget):
         selpro=con.cursor()
         cbg= self.cbforn.get_active_text()
         ns= str(cbg)
         selpro.execute("SELECT * FROM tb_forn WHERE nome='"+ns+"'")	
         numlinhas = int(selpro.rowcount)
         if numlinhas ==1:
            linp = selpro.fetchone()
            codmovv=  linp[0]   
            self.edcforn.set_text(str(codmovv))

   def gravar(self,widget):
      if self.chch.get_active() == False:
         self.nchegou ="nao"
      else :
         self.nchegou=""
 


      strr= self.edvalor.get_text()
      sr= strr.replace(",",".")
      srt= sr.replace("'","")
      valor= srt.replace('"',"")
      self.edvalor.set_text(valor)
      da = self.dataget()
      nw=datetime.now()
      no=str(nw)
      nn = no[11:]
      nnn = nn[:8]
      d = str(da)+ " " + nnn 
      icx = con.cursor()
      dw = self.var.get_text()
      valo = float(valor) #* float(dw)
      icx.execute("INSERT INTO tb_ctrl_cx (`icx`, `cod_des`, `cod_pg`, `valor`, `cod_for`, `data`, `defe`,`cod_tp_conta`,`cond`,`nundoc`) VALUES (NULL, '"+self.edcconta.get_text()+"', '0', '"+str(valo)+"', '"+self.edcforn.get_text()+"', '"+str(d)+"','"+str(self.nchegou)+"','"+self.edctpg.get_text()+"','"+self.edcond.get_text()+"','"+self.edndoc.get_text()+"');")
      print "conta adicionada ! "
      if self.edcconta.get_text() == "29" :
         print "nao pode ser agendado "
         #val = valo * -1
         #icxx = con.cursor()
         #icxx.execute("INSERT INTO tb_ctrl_cx (`icx`, `cod_des`, `cod_pg`, `valor`, `cod_for`, `data`, `defe`,`cod_tp_conta`,`cond`,`nundoc`) VALUES (NULL, '"+self.edcconta.get_text()+"', '"+self.eddcx.get_text()+"', '"+str(val)+"', '"+self.edcforn.get_text()+"', '"+str(d)+"','','"+self.edctpg.get_text()+"','"+self.edcond.get_text()+"','"+self.edndoc.get_text()+"');")
      dt = self.dataget()
      print dt
      dtt = dt.split('-')
      an= dtt[0]
      m= int(dtt[1]) + 1
      if m > 12 :
         m = m -12 

         an = str(int(dtt[0])+1)
      dd=dtt[2]
      m = "0"+ str(m)
      m = m[-2:]
      date = str(dd) +'/'+ str(m)+'/'+str(an)
      self.eddata.set_text(date)
      edco = self.edcond.get_text()
      edd = edco.split("/")
      eddo = int(edd[0]) + 1 
      edcf = str(eddo) + "/"+ edd[1]
      self.edcond.set_text(edcf)
      self.cbforn.set_sensitive(False)
      self.btnovo.set_sensitive(True)
      self.edvalor.grab_focus()
      self.cbconta.set_sensitive(False)
      self.cbcaixa.set_sensitive(False)
 

       

   def btnovoclick(self,widget):
      self.edcconta.set_text('1')
      self.edccx.set_text('1')
      self.edvalor.set_text('')
      self.edcforn.set_text('')
      self.cbcaixa.set_active(0)
      self.cbconta.set_active(0)
      self.cbconta.grab_focus()
      self.edcond.set_text("1/1")
      self.cbconta.set_sensitive(True)
      self.cbcaixa.set_sensitive(True)


   def edvalor_press(self,widget,event):
     if event.keyval == 65293 or event.keyval == 65421 :
          self.btgrava.grab_focus()

   def cbcaixa_press(self,widget,event):
     if event.keyval == 65293 or event.keyval == 65421 :
          self.edvalor.grab_focus()

   def cbforn_press(self,widget,event):
     if event.keyval == 65293 or event.keyval == 65421 :
          self.cbcaixa.grab_focus()
          #self.edvalor.grab_focus()


   def cbconta_press(self,widget,event):
     if event.keyval == 65293 or event.keyval == 65421 :
          if self.edcforn.get_text() != "-":
             self.cbforn.grab_focus()
          else: 
             self.cbcaixa.grab_focus()
          # self.edvalor.grab_focus()

   def lcxc(self,widget):
      lgrad=con.cursor()
      #print "codifo = " + codprod
      lgrad.execute("SELECT * FROM tb_caixas ")
      self.npg = int(lgrad.rowcount)
      #print "npg = " + str(npg) 
      if self.npg > 0: 

         pgr = lgrad.fetchall()
         #self.edgrad.set_text(" ")
         
         for pg in pgr:
            #self.cbconta.append_text("---")
            tex= str(pg[1])
            self.cbdcx.append_text(tex) 
  
      else: 
         #  print "nao tem grade"
         self.cbdcx.remove_text(0)

   def lcaixas(self,widget):
      lgrad=con.cursor()
      #print "codifo = " + codprod
      lgrad.execute("SELECT * FROM tb_caixas ")
      self.npg = int(lgrad.rowcount)
      #print "npg = " + str(npg) 
      if self.npg > 0: 

         pgr = lgrad.fetchall()
         #self.edgrad.set_text(" ")
         
         for pg in pgr:
            #self.cbconta.append_text("---")
            tex= str(pg[1])
            self.cbcaixa.append_text(tex) 
  
      else: 
         #  print "nao tem grade"
         self.cbcaixa.remove_text(0)

   def ltpg(self,widget):
      lgrad=con.cursor()
      self.nfor = 0 
      #print "codifo = " + codprod
      lgrad.execute("SELECT * FROM tb_tp_conta ")
      self.nfor = int(lgrad.rowcount)
      #print "npg = " + str(npg) 
      if self.nfor > 0: 

         pgr = lgrad.fetchall()
         #self.edgrad.set_text(" ")
         
         for pg in pgr:
            #self.cbconta.append_text("---")
            tex= str(pg[1])
            self.cbtpg.append_text(tex) 
  
      else: 
         #  print "nao tem grade"
         self.cbtpg.remove_text(0)

   def lforn(self,widget):
      lgrad=con.cursor()
      self.nfor = 0 
      #print "codifo = " + codprod
      lgrad.execute("SELECT * FROM tb_forn ")
      self.nfor = int(lgrad.rowcount)
      #print "npg = " + str(npg) 
      if self.nfor > 0: 

         pgr = lgrad.fetchall()
         #self.edgrad.set_text(" ")
         
         for pg in pgr:
            #self.cbconta.append_text("---")
            tex= str(pg[1])
            self.cbforn.append_text(tex) 
  
      else: 
         #  print "nao tem grade"
         self.cbforn.remove_text(0)


   def criacbdesmov(self,widget):
      ltbdesmov=con.cursor()
      #print "codifo = " + codprod
      ltbdesmov.execute("SELECT * FROM tb_desmov ORDER BY descricaodes ASC ")
      npg = int(ltbdesmov.rowcount)
      #print "npg = " + str(npg) 
      if npg > 0: 
         pgr = ltbdesmov.fetchall()
         for pg in pgr:
            tex= str(pg[1])
            self.cbconta.append_text(tex) 
      else: 
         #  print "nao tem grade"
         self.cbconta.remove_text(0)



if __name__ == "__main__":
  pgcontaap()

