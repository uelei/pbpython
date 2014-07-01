#!/usr/bin/python
# -*- coding: utf-8 -*-
#Arquivo: pbbd.py

import pygtk
pygtk.require("2.0")
import gtk
import gtk.glade
from conbd import con
import datetime
import time
from datetime import datetime
'''
n = datetime.now()
ns = str(n)
nl= ns.split('-')
ano = nl[0]
mes = nl[1]
'''
ano, mes, dia, hora, minuto, segundo, semana, juliano, verao= time.localtime()

class addpro:
   def __init__(self):

#Carrega a interface a partir do arquivo glade
     aw = gtk.glade.XML('addprodtroca.glade')
#carrega os widgets 
#janela principal
     self.jaddprod = aw.get_widget('window1')
     #self.listaprodutosvendidos = aw.get_widget('treeview1')
     #self.listaprodutosvendidosdois = aw.get_widget('treeview2')
     self.edent= aw.get_widget('entry2')
     self.edcod= aw.get_widget('entry3')
     self.eddes= aw.get_widget('entry1')
     self.edqtd= aw.get_widget('entry4')
     self.edpc = aw.get_widget('entry5') 
     self.eddatasel = aw.get_widget('entry6')
     self.bgrava = aw.get_widget('button1')
     self.cbmov = aw.get_widget('combobox1')
     self.codmov = aw.get_widget('entry7')
     self.edci = aw.get_widget('entry8')
     self.edgrad = aw.get_widget('entry9')
     self.cbgrad = aw.get_widget('combobox2')
     nw = datetime.now()
     now = str(nw)[:19]
     self.eddatasel.set_text(now)
     cmov=con.cursor()
     cmov.execute("SELECT * FROM t_mov ")
     lmov = cmov.fetchall()
     modelo = gtk.ListStore(str,str)
     modelo1 = gtk.ListStore(str)
     self.cbmov.set_model(modelo)
     self.cbgrad.set_model(modelo1)
     self.moo ={}
     
     i =0
      
     for llmov in lmov:

#          stt= llmov[0]
 #        dss=llmov[1] 
         
         # print str(dss) + "stt = "+ str(stt)
          #modelo.append([llmov[1],llmov[0]])
          
          self.cbmov.append_text(str(llmov[1]))    
          self.moo[i]= llmov[0]
          i +=1 
     #self.cbmov.set_model(modelo)
          #comboHoras.append_text(str(i))

     self.edqtd.set_text('1')
     
     
#Conecta todos os Sinais aos Callbacks
     aw.signal_autoconnect(self)

#Exibe janela principalpb
     self.jaddprod.show_all()
     coa = open('consulta.t','r')
     co = coa.read()
     if co == "1":
         print "operando no servidor secundario somente consulta"
        
         self.bgrava.set_sensitive(False)
#Inicia o loop principal de eventos (GTK MainLoop)
     
     gtk.main()
   def gravaadd(self,widget):
    coa = open('consulta.t','r')
    co = coa.read()
    if co == "1":
        print "operando no servidor secundario somente consulta"
        
        self.bgrava.set_sensitive(False)
    else:
      nww=datetime.now()
      noo=str(nww)
      nw=noo[:19]
      if self.codmov.get_text() == "":
         print "nao tem mov "
      else :
         if self.edcod.get_text() == "":
            print "nao tem produto"
         else :
             novcv= con.cursor()
             #print nw 
             novcv.execute("INSERT INTO tb_cv (cv,data,vend,vtc,vtv,dpg,aux,n_not_ext,now,cod_mov,v_des,cod_cli) VALUES (NULL,'"+ str(self.eddatasel.get_text()) + "','0','"+str(self.edpc.get_text())+"','0','0','cor','0','"+nw+"','"+str(self.codmov.get_text())+ "','0','0')") 
             icv =  int(con.insert_id())
             improd =con.cursor()
             stc= float(self.edpc.get_text()) * float(self.edqtd.get_text())
             cg= self.cbgrad.get_active_text()
             ns= str(cg)
             #print cg
             nl= ns.split(' = ')
             grade = str(nl[0])
             improd.execute("INSERT INTO tb_mov_merc (i,n_not_int,cod_prod,qtd_prod,pc_u,pv_u,pc_s,pv_s,grade_sel,cod_mov,n_not_ext,data_sel,data_real,operador,p_des,v_des) VALUES (NULL,'"+str(icv)+"','"+str(self.edci.get_text())+"','"+str(self.edqtd.get_text())+"','"+str(self.edpc.get_text())+"','0','"+str(stc)+"','0','"+grade+"','"+str(self.codmov.get_text())+"','0','"+str(self.eddatasel.get_text())+"','"+nw+"','0','0','0') ")
 
             selpvendidos = con.cursor()
             selpvendidos.execute("SELECT * FROM tb_mov_merc WHERE n_not_int='"+str(icv)+"'")
             pvend = selpvendidos.fetchall()
             for pdv in pvend:
                selpro=con.cursor()
                selpro.execute("SELECT * FROM pbestoreal WHERE codigo='"+str(pdv[2])+"'")
	        linp = selpro.fetchone()
                qr=float(linp[7])
                ql = float(linp[8])
	        qv = float(pdv[3])
                qk = float(linp[9])
                traf = con.cursor()
                traf.execute("SELECT * FROM t_mov WHERE cit='"+str(pdv[9])+"'")
                ltraf = traf.fetchone()
                self.vlj = ltraf[2]
                vlj = ltraf[2]
                vrc = ltraf[3]
                vpk = ltraf[4]
                qlt= ql + (vlj * qv)
                qrc = qr + (vrc * qv)
                qpkt = qk + (vpk * qv)
                   
                upprod=con.cursor()
	        upprod.execute("UPDATE pbestoreal SET qtdautalest='"+str(qrc)+"',qestlj1='"+str(qlt)+"',qestl2='"+str(qpkt)+"' WHERE codigo='"+str(pdv[2])+"'")
             #dar baixa na grade 
             #print pdv[8]
             grad = pdv[8]
             if grad != "":
                selgrade=con.cursor()
                selgrade.execute("SELECT * FROM tb_grad WHERE codprod='"+str(pdv[2])+"'AND des_grade='"+str(grad)+"' ")
                ng = int(selgrade.rowcount)
                if ng > 0 :
                   lg = selgrade.fetchone()
                   qtdgrad= float(lg[2])
                   ig = lg[0]
                   qtdgt=  qtdgrad + (qv * self.vlj)
                   upgrade=con.cursor()
                   upgrade.execute("UPDATE tb_grad SET qta_grade='"+str(qtdgt)+"' WHERE igrad='"+str(ig)+"'")

































             con.commit()
             self.eddes.set_text("")
             self.edcod.set_text("")
    	     self.edpc.set_text("")
             #self.cbmov.set_active(0)
             self.edent.set_text("")
             if __name__== "__main__":
                gtk.main_quit()
                exit(1)
             else : 
                self.jaddprod.hide()


   def sair (self,widget):
     if __name__== "__main__":
       gtk.main_quit()
       con.close()   
       exit(1)
     else :
        self.jaddprod.hide()

   def grad_sel(self,widget):
         selpro=con.cursor()
         codpp= self.edci.get_text()
         cg= self.cbgrad.get_active_text()
         ns= str(cg)
         #print cg
         nl= ns.split(' = ')
         #print str(nl[0])
         selpro.execute("SELECT * FROM tb_grad WHERE codprod='"+str(codpp)+"' AND des_grade= '"+ str(nl[0])+ "'")	
         numlinhas = int(selpro.rowcount)
         if numlinhas ==1:
            linp = selpro.fetchone()
            cigrade=  linp[0]   
            self.edgrad.set_text(str(cigrade))
         


   def mov_selecionado(self,widget):
      cimov = self.cbmov.get_active()
      #print cimov
      mo=str(self.moo[cimov])
      #print "com= " + mo
      
      self.codmov.set_text(str(mo))
      self.edent.grab_focus()
   def exibeproduto (self,strp):

      lprod=con.cursor()
      strprocurado = strp
      lprod.execute("SELECT * FROM pbestoreal WHERE codbarras='"+strprocurado+"'")
      npe = int(lprod.rowcount)
      if npe ==1:
         llprod = lprod.fetchone()  
         self.eddes.set_text(str(llprod[2]))
         self.edcod.set_text(str(llprod[0]))
         #self.edun.set_text(str(llprod[4]))
         #self.edqt.set_text(str(llprod[7]))
         #self.edpv.set_text(str(llprod[5]))
         self.edpc.set_text(str(llprod[12]))
         self.edci.set_text(str(llprod[0]))
         self.exibegrade(str(llprod[0]))
      else: 
         lprod.execute("SELECT * FROM pbestoreal WHERE codigo='"+strprocurado+"'")
         npee = int(lprod.rowcount)
         if npee ==1:
                    llprod = lprod.fetchone()
     		    self.eddes.set_text(str(llprod[2]))
    		    self.edcod.set_text(str(llprod[1]))
    		    #self.edun.set_text(str(llprod[4]))
  		    #self.edqt.set_text(str(llprod[7]))
  		    #self.edpv.set_text(str(llprod[5]))
  	 	    self.edpc.set_text(str(llprod[12]))
                    self.edci.set_text(str(llprod[0]))
                    self.exibegrade(str(llprod[0]))
         else : 
     		    self.eddes.set_text("")
    		    self.edcod.set_text("")
    		    #self.edun.set_text(str(llprod[4]))
  		    #self.edqt.set_text(str(llprod[7]))
  		    #self.edpv.set_text(str(llprod[5]))
  	 	    self.edpc.set_text("")
        
   def exibegrade(self,strr):
      codprod = strr
      lgrad=con.cursor()
      #print "codifo = " + codprod
      lgrad.execute("SELECT * FROM tb_grad WHERE codprod='"+codprod+"'")
      npg = int(lgrad.rowcount)
      #print "npg = " + str(npg) 
      if npg > 0: 
         ##self.bb
         pgr = lgrad.fetchall()
         for pg in pgr:
            #self.cbgrad.append_text("---")
            tex= str(pg[3]) + " = " + str(pg[2])
            self.cbgrad.append_text(tex) 
            
            #print pg[3] 
             

      else: 
         #  print "nao tem grade"
         self.cbgrad.remove_text(0)
         self.cbgrad.remove_text(0)
         self.cbgrad.remove_text(0)
         self.cbgrad.remove_text(0)
         self.cbgrad.remove_text(0)
         self.cbgrad.remove_text(0)
         self.cbgrad.remove_text(0)
         self.cbgrad.remove_text(0)
         self.cbgrad.remove_text(0)
         self.cbgrad.remove_text(0)
         self.cbgrad.remove_text(0)
         self.cbgrad.remove_text(0)
         self.edgrad.set_text(" ")

   def pexibeproduto (self,strp):

    
      strp = self.edent.get_text()
      self.exibeproduto(strp)
      

    
#Callbacks = acoes
if __name__ == "__main__":
  addpro()

