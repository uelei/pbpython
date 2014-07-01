#!/usr/bin/python
# -*- coding: utf-8 -*-
#Arquivo: entrada.py

import pygtk
pygtk.require("2.0")
import gtk
import gtk.glade
from conbd import con
import datetime
import time
from datetime import datetime

ano, mes, dia, hora, minuto, segundo, semana, juliano, verao= time.localtime()

class entrada: 
   #GLADE_FILE= "vendagtk.glade"
   def __init__(self):
    
#Carrega a interface a partir do arquivo glade
     aw = gtk.glade.XML('entrada.glade')
     #aw = gtk.Builder()
     #aw.add_from_file(self.__class__.GLADE_FILE)

#carrega os widgets 
#janela venda
     self.javenda = aw.get_widget('janelavenda')
     self.eddata= aw.get_widget('eddata')     
     self.ednumvendedor= aw.get_widget('ednumvendedor')
     self.ednumerovenda=aw.get_widget('ednumvenda')
     self.edgrad= aw.get_widget('entry4')
     self.cbgrad = aw.get_widget('combobox1')
     self.btnovavend = aw.get_widget('btnovavend')
     self.btsair = aw.get_widget('btsair')
     self.labelcod = aw.get_widget('label12')
     self.labelqtd = aw.get_widget('labelqtd')
     self.edcod = aw.get_widget('edcod')
     self.edqtd = aw.get_widget('entry1')
     self.labelpreco = aw.get_widget('labelpv')
     self.edpreco = aw.get_widget('entry2')
     self.btinseri = aw.get_widget('btinseri')
     self.btapaga = aw.get_widget('btapaga')
     self.eddescp = aw.get_widget('eddescp')
     self.listaprodutosvendidos = aw.get_widget('listaprodutosvendidos')
     self.labeltotal =aw.get_widget('label16')
     self.edtotal = aw.get_widget('edtotal')
     self.btfinalizar = aw.get_widget('btfinalizar')
     self.edgrade = aw.get_widget('edgrade')
     self.edcodigo = aw.get_widget('entry3')
     self.lgrade = aw.get_widget('lgrade')
     self.edpc=aw.get_widget('entry5')
     self.codmov=aw.get_widget('entry6')
     self.eddpv= aw.get_widget('entry7')
     self.scrow = aw.get_widget('scrolledwindow1')
     self.edcsellista = aw.get_widget('entry8')


#janela fecha venda
     self.janelafechavenda = aw.get_widget('janelafechavenda')
     self.edtota = aw.get_widget('edtota')
     self.eddin = aw.get_widget('eddin')
     self.edcar = aw.get_widget('edcar')
     self.edche = aw.get_widget('edche')
     self.btfechavenda = aw.get_widget('btfechavenda')
     self.cbfp = aw.get_widget('cbfp')
     self.chnt = aw.get_widget('chnt')
     self.ednnt = aw.get_widget('ednnt')


#janela de calendario 
     self.janelacalendario = aw.get_widget('janelacalendario')
     self.caljanela = aw.get_widget('caljanela')    
     

#seta valores aos widgets 
     data=str(dia)+"/"+str(mes)+"/"+str(ano)
     self.eddata.set_text(data)
     self.ednumvendedor.grab_focus()
     self.exibegrade('')
     self.i = 0
     self.cppp = []
     self.scrow.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
#Conecta todos os Sinais aos Callbacks
     #aw.connect_signals(self)
     aw.signal_autoconnect(self)
#Exibe janela principalpb
     
     self.javenda.show_all()
#Inicia o loop principal de eventos (GTK MainLoop)
     gtk.main()

   def ednventer(self,widget,event):
      
      if event.keyval ==65293 or event.keyval == 65421 :
         self.novavenda(self)
   
   def gipvendido(self,widget):
      cdp = self.edcodigo.get_text()
      if cdp != "":
         self.gpvendido(self)
      else: 
         print "produto invalido"

   
   def gpvendido(self,widget):
      numvenda = self.ednumerovenda.get_text()
      cdp = self.edcodigo.get_text()
      selcv=con.cursor()
      grd= self.edgrad.get_text()
      if grd == " ":
         print "nao ta selecionado"
      else:
         selcv.execute("SELECT * FROM tb_cv WHERE cv='"+numvenda+"'")
         npcv=int(selcv.rowcount)
         if npcv < 1:
            print "erro de logica venda nao existe"
         else :
            
            cg= self.cbgrad.get_active_text()
            ns= str(cg)
            #print ns
            if ns != "None":
               #print "true" 
               nl= ns.split(' = ')
               grade = str(nl[0])
            
            else: 
                grade=" "
                #print "nao "
            lcv = selcv.fetchone()
            cvvtc= lcv[3] #cv total de custo 
            cvvtv= lcv[4] #cv total de venda 
            selpv=con.cursor()
            selpv.execute("SELECT * FROM tb_mov_merc WHERE n_not_int='"+numvenda+"' AND cod_prod='"+cdp+"' AND grade_sel='"+grade+"' ")
            npv = int(selpv.rowcount)
            if npv == 1 :
               print "ja vendeu acrescentar"
               linvenda = selpv.fetchone()
               iv = linvenda[0]
               pc_ua= linvenda[4]
               pv_ua= linvenda[5]
               qtda=linvenda[3]
               pc_sa= linvenda[6]
               pv_sa= linvenda[7]
               pc_u =float(self.edpc.get_text())
               pv_u = float(self.edpreco.get_text())
               qtd = float(self.edqtd.get_text())
               stc = pc_u * qtd
               stv = pv_u * qtd
               qtdf= qtd + qtda 
               
               pvsas=pv_sa+stv 
               pcsas=pc_u * qtdf
               v_des = linvenda[15]
               v1 = self.apv * qtdf - pvsas
               if pv_u != self.apv :
                  print "tem desconto" 
               


               #preco de custo sem alteracoes 
               if qtdf < 0 :
                  pvuax=pvsas / qtdf 
                  uppv=con.cursor()
                  uppv.execute("UPDATE tb_mov_merc SET qtd_prod='"+str(qtdf)+"',pv_u='"+str(pvuax)+"',pc_s='"+str(pcsas)+"',pv_s='"+str(pvsas)+"',cod_mov='991' WHERE n_not_int='"+numvenda+"' AND cod_prod='"+cdp+"' AND grade_sel='"+grade+"' ")
               else: 
                  if qtdf == 0 : 
                      rem=con.cursor()
                      rem.execute("DELETE FROM tb_mov_merc WHERE i='"+str(iv)+"' LIMIT 1") # deleta registro 
                      print "produto " +cdp+ " foi removido !"




                  else:
                     pvuax=pvsas / qtdf 
                     uppv=con.cursor()
                     print "produto " +cdp+ " qtd modificada !"
                     uppv.execute("UPDATE tb_mov_merc SET qtd_prod='"+str(qtdf)+"',pv_u='"+str(pvuax)+"',pc_s='"+str(pcsas)+"',pv_s='"+str(pvsas)+"',cod_mov='"+str(self.codmov.get_text())+"' WHERE n_not_int='"+numvenda+"' AND cod_prod='"+cdp+"' AND grade_sel='"+grade+"' ")
                 
               upcv=con.cursor()
              # cvvtc= lcv[3] #cv total de custo 
              # cvvtv= lcv[4] #cv total de venda 
               cvvtc_stc = cvvtc + stc
               cvvtv_stv = cvvtv + stv               


               upcv.execute("UPDATE tb_cv SET vtc='"+str(cvvtc_stc)+"',vtv='"+str(cvvtv_stv)+"' WHERE cv='"+numvenda+"' ")
               self.listarprodutosvendidos()

            else:
               print "produto " +cdp+ " foi inserido !"
               inspv=con.cursor()
               pc_u =float(self.edpc.get_text())
               pv_u = float(self.edpreco.get_text())
               qtd = float(self.edqtd.get_text())
               stc = pc_u * qtd
               stv = pv_u * qtd
               stvd = self.apv
               data= self.dataget()
               nw=datetime.now()
               no=str(nw)
               nn = no[11:]
               nnn = nn[:8]
               dat = str(data)+ " " + nnn    
               now=no[:19]
               de = self.eddpv.get_text()
               if de != "":
                  vde = float(self.eddpv.get_text())*stvd /100 
               else:
                  de =0
                  vde =0
               inspv.execute("INSERT INTO tb_mov_merc (i,n_not_int,cod_prod,qtd_prod,pc_u,pv_u,pc_s,pv_s,grade_sel,cod_mov,n_not_ext,data_sel,data_real,operador,p_des,v_des) VALUES (NULL,'"+numvenda+"','"+cdp+"','"+str(qtd)+"','"+str(pc_u)+"','"+str(pv_u)+"','"+str(stc)+"','"+str(stv)+"','"+grade+"','"+str(self.codmov.get_text())+"','0','"+str(dat)+"','"+now+"','"+str(self.ednumvendedor.get_text())+"','"+str(de)+"','"+str(vde)+"') ")

               self.edgrad.set_text("")
               self.edcod.set_text("") 
               upcv=con.cursor()
               cvvtc_stc = cvvtc + stc
               cvvtv_stv = cvvtv + stv               
               upcv.execute("UPDATE tb_cv SET vtc='"+str(cvvtc_stc)+"',vtv='"+str(cvvtv_stv)+"' WHERE cv='"+numvenda+"' ")
               self.listarprodutosvendidos()


   def abrejanelacalendario(self,widget,data):
      self.janelacalendario.show_all()

   def grad_sel(self,widget):
         selpro=con.cursor()
         codpp= self.edcodigo.get_text()
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
    
   def fechajanelacalendario(self,widget):
      self.janelacalendario.hide()
      data = self.caljanela.get_date()
      ms=data[1]+1
      #mes="0"+str(ms)
      #d=data[2]
      #dia="0"+str(d)
      #dt=str(data[0])+"-"+str(mes[-2:])+"-"+str(dia[-2:])
      dt = str(data[2])+"/"+str(ms)+"/"+str(data[0])
      self.eddata.set_text(dt)
      self.ednumvendedor.grab_focus()
      return True

   def fecharjanelacalendario(self,widget,data):
      self.janelacalendario.hide()
      self.ednumvendedor.grab_focus()
      return True
   
   def dataget(self):
      edd=str(self.eddata.get_text())   
      eedd=edd.split('/')
      eedda= eedd[2]
      eeddm= eedd[1]
      eeddd= eedd[0]
      eddf= eedda+'-'+eeddm+'-'+eeddd
      return eddf
   def edpout(self,widget,dados):
      p = self.edpreco.get_text()
      prec =p.replace(",",".")
      dsp = self.eddpv.get_text()
      pre = float(prec) 
    
      if self.apv != pre : 
         if dsp != " ":
            a = 100 - (pre / self.apv *100)
            self.eddpv.set_text(str(a))
            



   def novavenda(self,widget):
      if self.ednumvendedor.get_text() !="": 
         numvendedor=self.ednumvendedor.get_text()
         try: 
            nuv= int(numvendedor)
         except:
            print "numero do vendedor invalido (letra)"
         else: 
            #n=0
            selvendedor = con.cursor()
            codv=self.ednumvendedor.get_text()
            selvendedor.execute("SELECT * FROM vendedores WHERE codv='"+codv+"'")
            numlinhas = int(selvendedor.rowcount)
            if numlinhas ==1:
               #print "vendedor valido "

               crianovavenda= con.cursor()
               data= self.dataget()
               nw=datetime.now()
               no=str(nw)
               nn = no[11:]
               nnn = nn[:8]
               dat = str(data)+ " " + nnn    
               now=no[:19]
               crianovavenda.execute("INSERT INTO tb_cv (cv,data,vend,vtc,vtv,dpg,aux,n_not_ext,now,cod_mov,v_des) VALUES (NULL,'"+dat+"','"+codv+"','0','0','0','0','0','"+str(now)+"','"+str(self.codmov.get_text())+"','0')")  
               nuv =  int(con.insert_id())
               con.commit()
               #nuv= str(numerovenda)
               nuv = str(nuv)
               self.ednumerovenda.set_text(nuv)
               print "nova venda criada com suscesso !"+nuv
               self.ednumvendedor.set_sensitive(False) 
               self.btnovavend.set_sensitive(False)
               self.eddata.set_sensitive(False)
               self.ednumerovenda.set_sensitive(False)
               self.btsair.set_sensitive(False)
               self.labelcod.set_sensitive(True)
               self.labelqtd.set_sensitive(True)
               self.edcod.set_sensitive(True)
               self.edqtd.set_sensitive(True)
               self.labelpreco.set_sensitive(True)
               self.edpreco.set_sensitive(True)
               self.btinseri.set_sensitive(True)
               #self.labeldescp.set_sensitive(True)
               self.eddescp.set_sensitive(True)
               self.listaprodutosvendidos.set_sensitive(True)
               self.labeltotal.set_sensitive(True)
               self.edtotal.set_sensitive(True)
               self.btfinalizar.set_sensitive(True)
               self.listarprodutosvendidos()
               self.cbfp.set_active(0)



            else:
               print "vendedor inexistente "

      else:
         print "numero de vendedor vazio ! "     

   def procuraproduto (self,widget):
      
      strr= self.edcod.get_text()
      sr= strr.replace(",","")
      srt= sr.replace("'","")
      srtt= srt.replace('"',"")
      self.edcod.set_text(srtt)
      self.btapaga.set_sensitive(False)
      self.edcsellista.set_text("")
      #self.btapaga.set_visible(False)
      
      #self.btapaga.set_sensitive(False)
      strproc = self.edcod.get_text()
      s = strproc.split('-')
      len(s)
      if len(s) == 1: 
          strprocurado = strproc
          self.eddpv.set_text("")
          sqt= float(self.edqtd.get_text())
          if sqt < 0:
               qt = sqt * -1 
          else:
                qt = sqt 
          self.edqtd.set_text(str(qt)) 
          self.codmov.set_text("2")

      if len(s) == 2 :
          if s[0] =="":
             #devolucao
             strprocurado = s[1]
             self.eddpv.set_text("")
             sqt= float(self.edqtd.get_text())
             self.codmov.set_text("991")
             if sqt <0:
                qt= sqt
             else:
                qt = sqt * -1 
             self.edqtd.set_text(str(qt)) 
          else:
             strprocurado = s[0]
             #desconto 
             self.eddpv.set_text(s[1])
             sqt= float(self.edqtd.get_text())
             if sqt < 0:
                qt = sqt * -1 
             else:
                qt = sqt 
             self.edqtd.set_text(str(qt)) 
             self.codmov.set_text("2")
      pcp=con.cursor()
      pcp.execute("SELECT * FROM pbestoreal WHERE codigo='"+strprocurado+"'")
      npe = int(pcp.rowcount)
      if npe ==1:  
        
         self.labelcod.set_text("codigo")
         linp = pcp.fetchone()
         self.eddescp.set_text(str(linp[2]))
         if self.eddpv.get_text() == "":
            self.edpreco.set_text(str(linp[5]))
          
         else : 
            de=float(self.eddpv.get_text())
            vde = float(linp[5]) -(de * float(linp[5]) /100)
            self.edpreco.set_text(str(vde))
         self.apv= linp[5]
         self.edcodigo.set_text(str(linp[0]))
         self.edpc.set_text(str(linp[12]))
         #self.edqr.set_text("qr= "+str(linp[7]))
         self.labelpreco.set_sensitive(True)
         self.labelqtd.set_sensitive(True)
         self.btinseri.set_sensitive(True)
         self.exibegrade(str(linp[0]))

      else:
         pcbp=con.cursor()
         pcbp.execute("SELECT * FROM pbestoreal WHERE codbarras='"+strprocurado+"'")
         npcbe=int(pcbp.rowcount)
         if npcbe ==1:
           
            self.labelcod.set_text("cod barras")
            linpc = pcbp.fetchone()
            self.eddescp.set_text(str(linpc[2]))
            self.edpreco.set_text(str(linpc[5]))
            self.edcodigo.set_text(str(linpc[0]))
            self.labelpreco.set_sensitive(True)
            self.labelqtd.set_sensitive(True)
            self.btinseri.set_sensitive(True)
            grade=str(linpc[14])
            self.edpc.set_text(str(linpc[12]))
            #self.edqr.set_text("qr= "+str(linpc[7]))
            self.exibegrade(str(linp[0]))
            self.apv= linp[5]
            '''if grade == "s":
              
               self.listagrade(linpc[0])
            else :
               self.naopossuigrade()'''
         else:
            self.labelcod.set_text("codigo")
            self.eddescp.set_text("Produto nao encontrado")
            self.edpreco.set_text("0")
            self.edcodigo.set_text('')
            self.edpc.set_text("")
            self.labelpreco.set_sensitive(False)
            self.labelqtd.set_sensitive(False)
            self.btinseri.set_sensitive(False)
            #self.edqr.set_text("")
            self.exibegrade('')
            self.apv= 0
            #self.naopossuigrade()


   def listarprodutosvendidos(self):
      ncolunas = self.listaprodutosvendidos.get_columns()
      for col in ncolunas:
         self.listaprodutosvendidos.remove_column(col)  
      self.tipodetabelavenda = gtk.ListStore(str,str,str,str,str,str,str)
      self.listaprodutosvendidos.set_model(self.tipodetabelavenda)
      self.listaprodutosvendidos.append_column(gtk.TreeViewColumn("codigo",gtk.CellRendererText(), text=0))
      self.listaprodutosvendidos.append_column(gtk.TreeViewColumn("cod barras",gtk.CellRendererText(), text=1))
      self.listaprodutosvendidos.append_column(gtk.TreeViewColumn("descricao",gtk.CellRendererText(), text=2))      
      self.listaprodutosvendidos.append_column(gtk.TreeViewColumn("quantidade",gtk.CellRendererText(), text=3))      
      self.listaprodutosvendidos.append_column(gtk.TreeViewColumn("preco",gtk.CellRendererText(), text=4))      
      self.listaprodutosvendidos.append_column(gtk.TreeViewColumn("subtotal",gtk.CellRendererText(), text=5))
      self.listaprodutosvendidos.append_column(gtk.TreeViewColumn("grade",gtk.CellRendererText(), text=6))
      selnumv =con.cursor()
      numvenda = self.ednumerovenda.get_text()
      
      selnumv.execute("SELECT * FROM tb_cv WHERE cv='"+numvenda+"'")
      lin = selnumv.fetchone()
      self.edtotal.set_text(str(lin[4]))
      self.totalreal = float(lin[4])
      
      selpvendidos=con.cursor()
      selpvendidos.execute("SELECT * FROM tb_mov_merc WHERE n_not_int='"+numvenda+"'")
      pvend = selpvendidos.fetchall()
      it =0
      self.cppp ={}
     
      for pdv in pvend:
         selpro=con.cursor()
         selpro.execute("SELECT * FROM pbestoreal WHERE codigo='"+str(pdv[2])+"'")	
         linp = selpro.fetchone()
         dp = linp[2]
         cb=linp[1]
         self.cppp[it]= str(pdv[2])+ "_" + pdv[8]
         it +=1
         self.tipodetabelavenda.append([pdv[2],cb,dp,pdv[3],pdv[5],pdv[7],pdv[8]])
      self.edcod.set_text('')
      self.edqtd.set_text("1")
      self.eddescp.set_text('')
      self.edpreco.set_text('')
      self.edcod.grab_focus()


   def exibegrade(self,strr):
      codprod = strr
      lgrad=con.cursor()
      #print "codifo = " + codprod
      lgrad.execute("SELECT * FROM tb_grad WHERE codprod='"+codprod+"'")
      self.npg = int(lgrad.rowcount)
      #print "npg = " + str(npg) 
      if self.npg > 0: 
         ##self.bb
         self.lgrade.set_sensitive(True)
         pgr = lgrad.fetchall()
         self.edgrad.set_text(" ")
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
         self.edgrad.set_text("--")
         self.lgrade.set_sensitive(False)



   def edqtdpress(self,widget,event):
      if event.keyval == 65293 or event.keyval == 65421 :
         self.edpreco.grab_focus()
         strr= self.edqtd.get_text()
         sr= strr.replace(",",".")
         srt= sr.replace("'","")
         srtt= srt.replace('"',"")
         srtt = str(float(srtt))
         self.edqtd.set_text(srtt)

   def edqtdout(self,widget,event):
         strr= self.edqtd.get_text()
         sr= strr.replace(",",".")
         srt= sr.replace("'","")
         srtt= srt.replace('"',"")
         srtt = str(float(srtt))
         self.edqtd.set_text(srtt)
      
   def edprecopress(self,widget,event):
     if event.keyval == 65293 or event.keyval == 65421 :
        if self.npg > 0 :
          self.cbgrad.grab_focus()
          self.cbgrad.popup()
        else :
          self.btinseri.grab_focus()


   def cbpress(self,widget,event):
     if event.keyval == 65293 or event.keyval == 65421 :
          self.btinseri.grab_focus()


   def listasel(self,widget):
      ii= self.listaprodutosvendidos.get_cursor() 
      f=ii[0][0]
      self.btapaga.set_sensitive(True)
      self.edcsellista.set_text(str(self.cppp[f]))
  
   def codfocus(self,widget,outro):
      self.btapaga.set_sensitive(False)
      
 
   def removeproduto(self,widget):
      auxae = self.edcsellista.get_text()
      codpre= auxae.split('_')
      codpr=codpre[0]
      gradpr=codpre[1]
      numvenda = self.ednumerovenda.get_text()
      selcv = con.cursor()
      # seleciona a venda 
      selcv.execute("SELECT * FROM tb_cv WHERE cv='"+numvenda+"'")
      npcv=int(selcv.rowcount)
      if npcv < 1:
         print "erro de logica venda nao existe"
      else :
         lcv = selcv.fetchone()
         cvvtc= lcv[3] #cv total de custo 
         cvvtv= lcv[4] #cv total de venda 
         selpv=con.cursor() 
         # seleciona o produto 
         selpv.execute("SELECT * FROM tb_mov_merc WHERE n_not_int='"+numvenda+"' AND cod_prod='"+codpr+"' AND grade_sel='"+gradpr+"' ")
         npv = int(selpv.rowcount)
         if npv == 1 :
               #existe produto a deletar 
               linvenda = selpv.fetchone()
               pc_sa= linvenda[6] # preco subtotal custo do produto
               pv_sa= linvenda[7] # preco subtotal venda do produto
               itbmovmerc = linvenda[0] # i do produto na tabela tb_mov_merc
               rem=con.cursor()
               rem.execute("DELETE FROM tb_mov_merc WHERE i='"+str(itbmovmerc)+"' LIMIT 1") # deleta registro 
               upcv=con.cursor()
               cvvtc_stc = cvvtc - pc_sa
               cvvtv_stv = cvvtv - pv_sa 
               # atualiza valores totais da venda               
               upcv.execute("UPDATE tb_cv SET vtc='"+str(cvvtc_stc)+"',vtv='"+str(cvvtv_stv)+"' WHERE cv='"+numvenda+"' ")
               self.listarprodutosvendidos()
               print "produto "+ codpr+ " foi removido !"

   def abrejanelafechavenda(self,widget):
      self.janelafechavenda.show_all()
      self.edtota.set_text(self.edtotal.get_text())
      self.edtota.grab_focus()

   def codenter(self,widget,event):
      print event.keyval
      if event.keyval ==65293 or event.keyval == 65421 :
          if self.npg > 0: 
             self.cbgrad.grab_focus()
             self.cbgrad.popup()
          else:
             self.gipvendido(self)
      if event.keyval ==65472:
         self.abrejanelafechavenda(self)
   

#funcoes da janela fecha venda 
   def edtotaenter(self,widget,event):
      if event.keyval == 65293 or event.keyval == 65421 :
         self.eddin.grab_focus()
         #tota=self.edtota.get_text()
         #tota= tota.replace(",",".")
         #self.edtota.set_text(tota)
      if event.keyval == 65476:
         #self.chnt.grab_focus()
         self.chnt.clicked()
         self.chnota(self)

   def edtotaout(self,widget,event):
      #self.eddin.grab_focus()
      tota=self.edtota.get_text()
      tota= tota.replace(",",".")
      self.edtota.set_text(tota)
      self.edtotal.set_text(tota)

   def eddinenter(self,widget,event):
      if event.keyval == 65293 or event.keyval == 65421:
         tota = self.edtota.get_text()
         tota = tota.replace(",",".")
         din = self.eddin.get_text()
         din = din.replace(",",".")         
         self.edtotal.set_text(tota)
         self.eddin.set_text(din)
         ftota = float(tota)
         fdin = float(din)
         if ftota ==  fdin:
            self.btfechavenda.grab_focus()
         else:
            self.edcar.grab_focus()
   def eddinout(self,widget,data):
         tota = self.edtota.get_text()
         tota = tota.replace(",",".")
         din = self.eddin.get_text()
         din = din.replace(",",".")         
         self.edtotal.set_text(tota)
         self.eddin.set_text(din)



   def edcarenter(self,widget,event):
      if event.keyval == 65293 or event.keyval == 65421:
         self.cbfp.grab_focus()

   def edcarout(self,widget,data):
      tota = self.edtota.get_text() 
      din = self.eddin.get_text()
      car = self.edcar.get_text()
      car = car.replace(",",".")
      self.edcar.set_text(car)
      fcar = float(car)
      ftota = float(tota)
      fdin = float(din)
      t=fcar + fdin 

   def edcheenter(self,widget,event):
      if event.keyval == 65293 or event.keyval == 65421:
         self.btfechavenda.grab_focus()
         che = self.edche.get_text()
         che = che.replace(",",".")
         self.edche.set_text(che)

   def edcheout(self,widget,data):
      che = self.edche.get_text()
      che = che.replace(",",".")
      self.edche.set_text(che)



   def cbfpenter(self,widget,event):
      if event.keyval == 65293 or event.keyval == 65421: 
         tota = self.edtota.get_text() 
         din = self.eddin.get_text()
         car = self.edcar.get_text()
         car = car.replace(",",".")
         self.edcar.set_text(car)
         fcar = float(car)
         ftota = float(tota)
         fdin = float(din)
         t=fcar + fdin 
         print self.cbfp.get_active_text()
         if t == ftota:
            self.btfechavenda.grab_focus()
         else:      
            self.edche.grab_focus()

   def chnota(self,widget):
     
      if self.chnt.get_active() == True:
         self.ednnt.set_sensitive(True)
         self.ednnt.grab_focus()
      else:
         self.ednnt.set_sensitive(False)
         self.ednnt.set_text("0")

   def ednntpress (self,widget,event):
      if event.keyval == 65293 or event.keyval == 65421: 
         self.eddin.grab_focus()
         

   def fechajanelafechavenda(self,widget):
      self.janelafechavenda.hide()
      self.edcod.grab_focus()



   def fechavenda(self,widget):
      numvenda = self.ednumerovenda.get_text()
      tota = self.edtota.get_text() 
      din = self.eddin.get_text()
      car = self.edcar.get_text()
      che = self.edche.get_text()
      fcar = float(car)
      ftota = float(tota)
      fdin = float(din)
      fche = float(che)
      t= fcar + fche + fdin
      data= self.dataget()
      nw=datetime.now()
      no=str(nw)
      nn = no[11:]
      nnn = nn[:8]
      dat = str(data)+ " " + nnn    
      now=no[:19]
      if t == ftota:
         data = self.caljanela.get_date()
         ms=data[1]+1
         mes="0"+str(ms)
         d=data[2]
         dia="0"+str(d)
         dt=str(dia[-2:])+"/"+str(mes[-2:])+"/"+str(data[0])
         #dt=str(data[0])+"-"+str(mes[-2:])+"-"+str(dia[-2:])
         '''if fdin != 0:
            insv = con.cursor()
            insv.execute("INSERT INTO tb_vendas (idcodv,codvend,valorv,fpag,datav,numop,cod_pg,datatime) VALUES (NULL,'"+self.ednumvendedor.get_text()+"','"+str(fdin)+"','dinheiro','"+dt+"','"+str(numvenda)+"','1','"+now+"')")
            print "dinheiro " + str(fdin)
         ddcar = self.cbfp.get_active()
         if ddcar == 0: 
            fccc=0
         if ddcar == 1: 
            fccc=2.45
         if ddcar == 2: 
            fccc=3.4
         if ddcar == 3: 
            fccc=4.4
         if ddcar == 4: 
            fccc=2.5
         if ddcar == 5: 
            fccc=3.5
         if ddcar == 6: 
            fccc=4.5
         if ddcar == 7: 
            fccc=0                     
         dcar = fcar*fccc/100
         if fcar !=0:
            insv = con.cursor()
            insv.execute("INSERT INTO tb_vendas (idcodv,codvend,valorv,fpag,datav,numop,cod_pg,datatime) VALUES (NULL,'"+self.ednumvendedor.get_text()+"','"+str(fcar)+"','cartao','"+dt+"','"+str(numvenda)+"','2-"+str(ddcar)+"','"+now+"')")
            print "cartao " + str(fcar)
         if fche !=0:
            insv = con.cursor()
            insv.execute("INSERT INTO tb_vendas (idcodv,codvend,valorv,fpag,datav,numop,cod_pg,datatime) VALUES (NULL,'"+self.ednumvendedor.get_text()+"','"+str(fche)+"','cheque','"+dt+"','"+str(numvenda)+"','3','"+now+"')")
            print "cheque " + str(fche)
         '''
         fevenda =con.cursor()
         if float(ftota) != float(self.totalreal):
                print "desconto final aplicado"
                vdeff = float(self.totalreal) - float(ftota) 
         else: 
                vdeff=0;
         #print "juros cartao = "+ str(dcar)
         # depois adicionas a contas a pagar 
         fcar =0
         fdin =0 
         fche = 0
         dcar =0
         if self.chnt.get_active() == True:#nota tirou
            
            
            upnot = con.cursor()
            upnot.execute("UPDATE tb_mov_merc SET cod_mov='777',n_not_ext='"+self.ednnt.get_text() +"' WHERE n_not_int='"+numvenda+"' ")
            fevenda.execute("UPDATE tb_cv SET vtv='"+str(ftota)+"',dpg='"+str(dcar)+"',aux='"+"d="+str(fdin)+"-c="+str(fcar)+"-h="+str(fche)+"',n_not_ext='"+self.ednnt.get_text()  +"',cod_mov='777',v_des='"+str(vdeff)+"',now='"+now+"' WHERE cv='"+numvenda+"'")
            inss=con.cursor()
            inss.execute("INSERT INTO `notasentrada` (`NUMERONF`, `SERIE`, `MODELO`, `VENDEDOR`, `FORNECEDOR`, `OPERACAO`, `EMISSAO`, `FRETE`, `SEGURO`, `DESPESAS`, `VOLUMES`, `ESPECIE`, `MARCA`, `TRANSPORTA`, `FRETE12`, `SAIDAH`, `SAIDAD`, `DUPLICATAS`, `BASEICM`, `ICMS`, `ICMSSUBSTI`, `BASESUBSTI`, `ALIQUOTA`, `ISS`, `IPI`, `TOTAL`, `MERCADORIA`, `COMPLEMEN1`, `COMPLEMEN2`, `COMPLEMEN3`, `COMPLEMEN4`, `EMITIDA`, `SERVICOS`, `DESCRICAO1`, `DESCRICAO2`, `DESCRICAO3`, `PESOBRUTO`, `PESOLIQUI`, `DESCPROD`, `CODIGOBASE`) VALUES ('"+self.ednnt.get_text()+"', ' ', ' ', ' ', 'ffornecedor', 'Compra para comercialização', '"+self.dataget()+"', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '', '"+str(ftota)+"', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '', ' ', ' ', ' ');")


         else :
            fevenda.execute("UPDATE tb_cv SET vtv='"+str(ftota)+"',dpg='"+str(dcar)+"',aux='"+"d="+str(fdin)+"-c="+str(fcar)+"-h="+str(fche)+"',n_not_ext='"+self.ednnt.get_text()  +"',v_des='"+str(vdeff)+"',now='"+now+"' WHERE cv='"+numvenda+"'")


         ncolunas = self.listaprodutosvendidos.get_columns()
         for col in ncolunas:
            self.listaprodutosvendidos.remove_column(col)  
         self.tipodetabelavenda = gtk.ListStore(str,str,str,str,str,str,str)
         self.listaprodutosvendidos.set_model(self.tipodetabelavenda)
         self.listaprodutosvendidos.append_column(gtk.TreeViewColumn("codigo",gtk.CellRendererText(), text=0))
         self.listaprodutosvendidos.append_column(gtk.TreeViewColumn("cod barras",gtk.CellRendererText(), text=1))
         self.listaprodutosvendidos.append_column(gtk.TreeViewColumn("descricao",gtk.CellRendererText(), text=2))      
         self.listaprodutosvendidos.append_column(gtk.TreeViewColumn("quantidade",gtk.CellRendererText(), text=3))      
         self.listaprodutosvendidos.append_column(gtk.TreeViewColumn("preco",gtk.CellRendererText(), text=4))      
         self.listaprodutosvendidos.append_column(gtk.TreeViewColumn("subtotal",gtk.CellRendererText(), text=5))
         self.listaprodutosvendidos.append_column(gtk.TreeViewColumn("tam",gtk.CellRendererText(), text=6))
         
         selpvendidos = con.cursor()
         selpvendidos.execute("SELECT * FROM tb_mov_merc WHERE n_not_int='"+numvenda+"'")
         pvend = selpvendidos.fetchall()
         for pdv in pvend:
             selpro=con.cursor()
             selpro.execute("SELECT * FROM pbestoreal WHERE codigo='"+str(pdv[2])+"'")
	     linp = selpro.fetchone()
             qr=float(linp[7])
	     ql = float(linp[8])
	     qv = float(pdv[3])
             qlt= ql + qv 
             if str(pdv[9]) == "777":
                qrt = qr + qv
             else:
                qrt = qr
             upprod=con.cursor()
	     upprod.execute("UPDATE pbestoreal SET qtdautalest='"+str(qrt)+"',qestlj1='"+str(qlt)+"' WHERE codigo='"+str(pdv[2])+"'")
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
                   qtdgt=  qtdgrad + qv
                   upgrade=con.cursor()
                   upgrade.execute("UPDATE tb_grad SET qta_grade='"+str(qtdgt)+"' WHERE igrad='"+str(ig)+"'")

         print "venda "+self.ednumerovenda.get_text()+" finalizada !"
         self.janelafechavenda.hide()
         self.ednumvendedor.set_sensitive(True) 
         self.btnovavend.set_sensitive(True)
         self.eddata.set_sensitive(True)
         self.ednumerovenda.set_sensitive(True)
         self.btsair.set_sensitive(True)
         self.labelcod.set_sensitive(False)
         self.labelqtd.set_sensitive(False)
         self.edcod.set_sensitive(False)
         self.edqtd.set_sensitive(False)
         self.labelpreco.set_sensitive(False)
         self.edpreco.set_sensitive(False)
         self.btinseri.set_sensitive(False)
         #self.labeldescp.set_sensitive(False)
         self.eddescp.set_sensitive(False)
         self.listaprodutosvendidos.set_sensitive(False)
         self.labeltotal.set_sensitive(False)
         self.edtotal.set_sensitive(False)
         self.btfinalizar.set_sensitive(False)
         self.ednumvendedor.set_text("")
         self.ednumerovenda.set_text("")
         self.edtotal.set_text("")
         self.eddin.set_text("0")
         self.edcar.set_text("0")
         self.edche.set_text("0")
         self.ednnt.set_text("0")
         self.chnt.set_active(False)
         self.ednumvendedor.grab_focus()
         self.cbfp.set_active(0)
         print "-------------------------------------------------------------------------"
               
      else: 
         print "total invalido"
         self.edtota.grab_focus()

   def btsairvenda(self,widget):
      if __name__ == "__main__":
         con.close()   
         gtk.main_quit()
         exit(0)
      else:    
         self.javenda.hide()
         return True
   def fecharjanelavendas(self,widget,data):
      if __name__ == "__main__":
         con.close()   
         gtk.main_quit()
         exit(0)
      else:    
         self.javenda.hide()
         return True
    
#Callbacks = acoes
if __name__ == "__main__":
  entrada()

