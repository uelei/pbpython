#!/usr/bin/python
# -*- coding: utf-8 -*-
#Arquivo: apagar.py

import pygtk
pygtk.require("2.0")
import gtk
import gtk.glade
from conbd import con
import datetime
import time
from datetime import datetime

ano, mes, dia, hora, minuto, segundo, semana, juliano, verao= time.localtime()

class apagar:
   def __init__(self):
      
#Carrega a interface a partir do arquivo glade
     aw = gtk.glade.XML('apagar.glade')
#carrega os widgets 
#janela principal
     self.jacaixa = aw.get_widget('window1')
     self.edconta = aw.get_widget('entry1')
     self.edforn = aw.get_widget('entry2')
     self.edtpc = aw.get_widget('entry3')
     self.edcond = aw.get_widget('entry4')
     self.edndoc = aw.get_widget('entry5')
     self.edpg = aw.get_widget('entry6')
     self.btpagar = aw.get_widget('button1')
     self.eddata = aw.get_widget('entry7')  
     self.edvar = aw.get_widget('entry8')
     self.rbdia = aw.get_widget('radiobutton1')
     self.rbmes = aw.get_widget('radiobutton2')
     self.listacx = aw.get_widget('treeview1') 
     self.coddp = aw.get_widget('entry9')
     self.cbtpc = aw.get_widget('combobox1')
     self.cbpg = aw.get_widget('combobox2')
     self.edtota = aw.get_widget('entry10')
     self.dtnow = aw.get_widget('entry11')
     self.btedpg = aw.get_widget('button2')
#janela de calendario 
     self.janelacalendario = aw.get_widget('window2')
     self.caljanela = aw.get_widget('calendar1')   









#seta valores 

     self.btedpg.set_sensitive(False)
     #self.edcxl.grab_focus()
     d = "0"+str(dia)
     d = d[-2:]
     
     data=str(d)+"/"+str(mes)+"/"+str(ano)
     self.eddata.set_text(data)
     self.dtnow.set_text(data)
     self.cbtpc.remove_text(0)
     self.cbpg.remove_text(0)   
#Conecta todos os Sinais aos Callbacks
     aw.signal_autoconnect(self)
     coa = open('consulta.t','r')
     co = coa.read()
     if co == "1":
         print "operando no servidor secundario somente consulta"
         self.cbtpc.set_sensitive(False)
         self.cbpg.set_sensitive(False)
         self.btpagar.set_sensitive(False)
         self.edcond.set_sensitive(False)
         self.edvar.set_sensitive(False)
         self.edndoc.set_sensitive(False)
        
#Exibe janela principalpb
     self.jacaixa.show_all()
     
#Inicia o loop principal de eventos (GTK MainLoop)
     
     gtk.main()

   def dataget(self):
      edd=str(self.eddata.get_text())   
      eedd=edd.split('/')
      eedda= eedd[2]
      #eeddm= eedd[1]
      eeddm = "0"+ eedd[1]
      eeddm = eeddm[-2:]
      #eeddd= eedd[0]
      eeddd= "0"+ eedd[0]
      eeddd= eeddd[-2:]
      
      eddf= eedda+'-'+eeddm+'-'+eeddd
      eddff= eedda+"/"+eeddm+"/"+eeddd

      return eddf

   def dtget(self):
      edd=str(self.dtnow.get_text())   
      eedd=edd.split('/')
      eedda= eedd[2]
      eeddm = "0"+ eedd[1]
      eeddm = eeddm[-2:]
      eeddd= "0"+ eedd[0]
      eeddd= eeddd[-2:]
      eddf= eedda+'-'+eeddm+'-'+eeddd


      return eddf
  

   def abrecal(self,widget,data):
      self.janelacalendario.show_all()
      
 
   def fecharjanelacalendario(self,widget,data):
      self.janelacalendario.hide()
      self.btatu.grab_focus()
      return True 

   def listadp(self,widget):
              self.cbtpc.remove_text(0)
              self.cbpg.remove_text(0)       
              self.cbtpc.remove_text(0)
              self.cbpg.remove_text(0)
              self.cbtpc.remove_text(0)
              self.cbpg.remove_text(0)
              self.cbtpc.remove_text(0)
              self.cbpg.remove_text(0)  
              self.cbtpc.remove_text(0)
              self.cbpg.remove_text(0)
              self.cbtpc.remove_text(0)
              self.cbpg.remove_text(0) 
              self.cbtpc.remove_text(0)
              self.cbpg.remove_text(0)
              self.cbtpc.remove_text(0)
              self.cbpg.remove_text(0) 
              self.cbtpc.remove_text(0)
              self.cbpg.remove_text(0)
              self.cbtpc.remove_text(0)
              self.cbpg.remove_text(0) 
              coddp = self.coddp.get_text()
              seltbcx =con.cursor()
              seltbcx.execute("SELECT * FROM tb_ctrl_cx WHERE icx='"+coddp+"'")
              lin = seltbcx.fetchone()
              cod_des = lin[1]
              valor = lin[3]
              cod_for = lin[4]
              cod_tp_ct = lin[7]
              cond = lin[8]
              numdoc = lin[9]
              defe = lin[6]
              seldesconta = con.cursor()
              seldesconta.execute("SELECT * FROM tb_desmov WHERE si='"+str(cod_des)+"'")
              ldcnta = seldesconta.fetchone()
              desconta = ldcnta[1]
              self.edconta.set_text(desconta)
              if cod_for == "-":
                 desfor = "-"
              else :
                 selforn = con.cursor()
                 selforn.execute("SELECT * FROM tb_forn WHERE codfor='"+str(cod_for)+"'")
                 lfor = selforn.fetchone()
                 if lfor != None :
                    desfor = lfor[1]
                 else : 
                    desfor = "-"
              self.edforn.set_text(desfor)   
		
              lgrad = con.cursor()
              self.nfor = 0 
              lgrad.execute("SELECT * FROM tb_tp_conta ")
              self.nfor = int(lgrad.rowcount)
              if self.nfor > 0: 
                 pgr = lgrad.fetchall()
                 for pg in pgr:
                    tex= str(pg[1])
                    self.cbtpc.append_text(tex) 
              self.cbtpc.set_active(int(cod_tp_ct)-1)
              lgradcx=con.cursor()
              lgradcx.execute("SELECT * FROM tb_caixas ")
              self.npgcx = int(lgradcx.rowcount)
              if self.npgcx > 0: 
                 pgrcx = lgradcx.fetchall()
                 for pgcx in pgrcx:
                   tex= str(pgcx[1])
                   self.cbpg.append_text(tex) 
              self.cbpg.set_active(0)
              self.edpg.set_text('1')

              self.edtpc.set_text(str(cod_tp_ct))
              self.edcond.set_text(cond)
              self.edndoc.set_text(numdoc) 
              self.edvar.set_text(str(valor))
              self.edvar.grab_focus()
              self.btpagar.set_sensitive(True)
              if defe == "nao":
                 self.btedpg.set_sensitive(True)
              else :
                 self.btedpg.set_sensitive(False)
   def pagar(self,widget):

      strr= self.edvar.get_text()
      sr= strr.replace(",",".")
      srt= sr.replace("'","")
      valr= srt.replace('"',"")
      valor = float(valr) * -1
      datasel = self.dataget()
      #print datasel
      dataatual = self.dtget()
      nw=datetime.now()
      no=str(nw)
      nn = no[11:]
      nnn = nn[:8]
      dat = str(datasel)+ " " + nnn 
      dattu = str(dataatual)+" "+nnn 
      uppg = con.cursor()
      uppg.execute("UPDATE tb_ctrl_cx SET `cod_pg` = '"+self.edpg.get_text()+"',cod_tp_conta='"+self.edtpc.get_text()+"',cond='"+self.edcond.get_text()+"',nundoc='"+self.edndoc.get_text()+"',defe='"+dattu+"',valor='"+str(valor)+"' WHERE icx ='"+self.coddp.get_text()+"' LIMIT 1 ;")
      self.atualcx(self)
      self.coddp.set_text('')
      #self.listadp(self)
      self.edvar.set_text('')
      self.edconta.set_text('')
      self.edforn.set_text('')
      self.edtpc.set_text('')
      self.edpg.set_text('')
      self.edcond.set_text('')
      self.edndoc.set_text('')
      self.edpg.set_text('')
      self.btpagar.set_sensitive(False)
   def editar(self,widget):

      strr= self.edvar.get_text()
      sr= strr.replace(",",".")
      srt= sr.replace("'","")
      valr= srt.replace('"',"")
      valor = float(valr) * -1
      datasel = self.dataget()
      #print datasel
      dataatual = self.dtget()
      nw=datetime.now()
      no=str(nw)
      nn = no[11:]
      nnn = nn[:8]
      dat = str(datasel)+ " " + nnn 
      dattu = str(dataatual)+" "+nnn 
      uppg = con.cursor()
      uppg.execute("UPDATE tb_ctrl_cx SET `cod_pg` = '0',cod_tp_conta='"+self.edtpc.get_text()+"',cond='"+self.edcond.get_text()+"',nundoc='"+self.edndoc.get_text()+"',defe='',valor='"+str(valr)+"' WHERE icx ='"+self.coddp.get_text()+"' LIMIT 1 ;")
      self.atualcx(self)
      self.coddp.set_text('')
      #self.listadp(self)
      self.edvar.set_text('')
      self.edconta.set_text('')
      self.edforn.set_text('')
      self.edtpc.set_text('')
      self.edpg.set_text('')
      self.edcond.set_text('')
      self.edndoc.set_text('')
      self.edpg.set_text('')
      self.btpagar.set_sensitive(False)
   def cbpg_sel(self,widget):
         selpro=con.cursor()
         cbg= self.cbpg.get_active_text()
         ns= str(cbg)
         selpro.execute("SELECT * FROM tb_caixas WHERE des_cx='"+ns+"'")	
         numlinhas = int(selpro.rowcount)
         if numlinhas ==1:
            linp = selpro.fetchone()
            codmovv=  linp[0]   
            self.edpg.set_text(str(codmovv)) 

   def fechajanelacalendario(self,widget):
      self.janelacalendario.hide()
      data = self.caljanela.get_date()
      ms=data[1]+1
      mes="0"+str(ms)
      mes= mes[-2:]
      d=data[2]
      #print d
      da="0"+str(d)
      #dt=str(data[0])+"-"+str(mes[-2:])+"-"+str(dia[-2:])
      dt = str(da[-2:])+"/"+str(mes)+"/"+str(data[0])
      self.eddata.set_text(dt)
      #print dt
     # self.btatu.grab_focus()
      self.atualcx(self)

   def cbtpg_sel(self,widget):
         selpro=con.cursor()
         cbg= self.cbtpc.get_active_text()
         ns= str(cbg)
         selpro.execute("SELECT * FROM tb_tp_conta WHERE des_tp_conta='"+ns+"'")	
         numlinhas = int(selpro.rowcount)
         if numlinhas ==1:
            linp = selpro.fetchone()
            codmovv=  linp[0]   
            self.edtpc.set_text(str(codmovv))

   def atualcx(self,widget):
           #campo cx loja
           data = self.dataget()
           selcx=con.cursor()
           da = data.split('-')
           ano = da[0]
           mes = da[1]
           dia = da[2]
           va = 0 
           #print da
           if self.rbdia.get_active():
              #dt=dia[-2:]+"/"+str(mes[-2:])+"/"+str(data[0])
              dt = str(ano) + "-" + str(mes)+"-"+str(dia)
           elif self.rbmes.get_active():
              #dt="/"+str(mes[-2:])+"/"+str(data[0])
              dt = str(ano) + "-" + str(mes)+"-"
           else:
              #dt="/"+str(data[0])
              dt = "20" 
           
           i=0
           self.a={}
           seltudo = con.cursor()
           seltudo.execute("SELECT * FROM tb_ctrl_cx WHERE data LIKE '%"+str(dt)+"%' ORDER BY data ASC ")
           selt = seltudo.fetchall()
           ncolunas = self.listacx.get_columns()
           for col in ncolunas:
              self.listacx.remove_column(col)  
           self.tipodetabela = gtk.ListStore(str,str,str,str,str,str)#,str,str,str,str
           self.listacx.set_model(self.tipodetabela)
           self.listacx.append_column(gtk.TreeViewColumn("data",gtk.CellRendererText(), text=0))
           self.listacx.append_column(gtk.TreeViewColumn("doc",gtk.CellRendererText(), text=1))
           self.listacx.append_column(gtk.TreeViewColumn("tdoc",gtk.CellRendererText(), text=2))
           self.listacx.append_column(gtk.TreeViewColumn("descricao",gtk.CellRendererText(), text=3))      
           self.listacx.append_column(gtk.TreeViewColumn("valor",gtk.CellRendererText(), text=4))      
           #self.listacx.append_column(gtk.TreeViewColumn("uni",gtk.CellRendererText(), text=4))      
           #self.listacx.append_column(gtk.TreeViewColumn("itau",gtk.CellRendererText(), text=5))
           #self.listacx.append_column(gtk.TreeViewColumn("pai",gtk.CellRendererText(), text=6))
           #self.listacx.append_column(gtk.TreeViewColumn("cheque",gtk.CellRendererText(), text=7))
           
           self.listacx.append_column(gtk.TreeViewColumn("efetivado",gtk.CellRendererText(), text=5))
          # self.tipodetabela.append(['vendas do dia',din,' ',' ',' ',' ',' ',ch,str(dt),str(dt)])
           for tdo in selt:
              icx = tdo[0]
              codpg = tdo[2] 
              codmov = tdo[1]
              cod_for = tdo[4]
              valor = tdo[3]
              dataa = tdo[5]
              defe = tdo[6]
              ctp = tdo[7]


              if cod_for == "-":
                 desfor = "-"
              else :
                 selforn = con.cursor()
                 selforn.execute("SELECT * FROM tb_forn WHERE codfor='"+str(cod_for)+"'")
                 lfor = selforn.fetchone()
                 if lfor != None :
                    desfor = lfor[1]
                 else : 
                    desfor = "-"
                






              lgrad = con.cursor()
              lgrad.execute("SELECT * FROM tb_tp_conta WHERE icod_tp_conta='"+str(ctp)+"'")
              pgr = lgrad.fetchone()
              tpc= str(pgr[1])
              
              
              seldmov =con.cursor()
              seldmov.execute("SELECT * FROM tb_desmov WHERE si='"+str(codmov)+"'")
              lin = seldmov.fetchone()
              if lin != None :
                 descmov = str(lin[1])
       
              if defe == "nao":
                 defe = "nao_recebida"
              else : 
                 defe = "pendende "
              if codpg == 0 : 
                 #print dataa
                 self.tipodetabela.append([str(dataa),descmov,tpc,desfor,valor,defe])
                 #self.tipodetabela.append([descmov,valor,tpc,des_for,' ',' ',' ',' ',data,defe])
                 self.a[i]=icx 
                 i = i + 1 
                 va = va + valor
              # self.tipodetabelavenda.append([pdv[2],cb,dp,pdv[3],pdv[5],pdv[7],pdv[8]]
              self.edtota.set_text(str(va))
   def listasel(self,widget):
      ii= self.listacx.get_cursor() 
      f=ii[0][0]
      #  self.btapaga.set_sensitive(True)
      #self.btnn.set_sensitive(True)
      #self.edcsellista.set_text(str(self.cppp[f]))
      self.coddp.set_text(str(self.a[f])) 
      self.listadp(self)
      coa = open('consulta.t','r')
      co = coa.read()
      if co == "1":
         #print "operando no servidor secundario somente consulta"
         self.cbtpc.set_sensitive(False)
         self.cbpg.set_sensitive(False)
         self.btpagar.set_sensitive(False)
         self.edcond.set_sensitive(False)
         self.edvar.set_sensitive(False)
         self.edndoc.set_sensitive(False)

if __name__ == "__main__":
   apagar()

