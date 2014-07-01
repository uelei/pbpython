#!/usr/bin/python
# -*- coding: utf-8 -*-
#Arquivo: venda.py

import pygtk
pygtk.require("2.0")
import gtk
import gtk.glade
from conbd import con
import datetime
import time
from datetime import datetime
import gobject



ano, mes, dia, hora, minuto, segundo, semana, juliano, verao= time.localtime()

class venda: 
   #GLADE_FILE= "vendagtk.glade"
   def __init__(self):
    
#Carrega a interface a partir do arquivo glade
     aw = gtk.glade.XML('venda.glade')
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
     self.btnn = aw.get_widget('buttonn')
     self.edqrc = aw.get_widget('entry10')
     self.bcolor = aw.get_widget('image1')
     self.entryitens=aw.get_widget('entry11')
     self.breopen=aw.get_widget('buttonropen')
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
     self.ednni = aw.get_widget('entry9')
     self.it=0.0
#janela de calendario 
     self.janelacalendario = aw.get_widget('janelacalendario')
     self.caljanela = aw.get_widget('caljanela')    
     

#seta valores aos widgets 
     di="0"+str(dia)
     dd = di[-2:]
     me = "0"+str(mes)
     mm =  me[-2:]
   
     data=str(dd)+"/"+str(mm)+"/"+str(ano)
     self.eddata.set_text(data)
     self.ednumvendedor.grab_focus()
     self.exibegrade('')
     self.i = 0
     self.cppp = []
     self.inoi = []
#Conecta todos os Sinais aos Callbacks
     #aw.connect_signals(self)
     aw.signal_autoconnect(self)
#Exibe janela principalpb
     coa = open('consulta.t','r')
     co = coa.read()
     if co == "1":
        print "operando no servidor secundario somente consulta"
        self.btnovavend.set_sensitive(False)
        #self.ednumvendedor.set_sensitive(False)


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
      self.bcolor.set_from_file("image/bag_white.png")
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
               self.it= self.it + qtd
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
               self.it= self.it + qtd            
               upcv.execute("UPDATE tb_cv SET vtc='"+str(cvvtc_stc)+"',vtv='"+str(cvvtv_stv)+"' WHERE cv='"+numvenda+"' ")
               self.listarprodutosvendidos()


   def abrejanelacalendario(self,widget,data):
      self.janelacalendario.show_all()

   def show_verify_dialog(self,str):
     verdialog = gtk.MessageDialog(type=gtk.MESSAGE_QUESTION,buttons=gtk.BUTTONS_YES_NO,message_format=str)
     verd = verdialog.run()
     verdialog.destroy()
     if verd == gtk.RESPONSE_YES:
         return True
     else:
         return False

   def reopenv(self,widget):
      #rotinas de reopen 
      #1 apagar vendas com cod da venda tb vendas
      #2 devolver produtos as quantidades respectivas ... seguindo o cod do mov 
      selvenda= con.cursor()
      numerovenda = self.ednumerovenda.get_text() 
      selvenda.execute("SELECT * FROM tb_cv WHERE cv='"+str(numerovenda)+"' ")
      npv = int(selvenda.rowcount)
      if npv >= 1:
         #print "venda achada cpm suscesso "
         if self.show_verify_dialog("abrir venda") :
               print "-------------------------------------------------------------------------"
               linp = selvenda.fetchone()
               codv= linp[2]
               datasel= str(linp[1])
               codmov = str(linp[9])
               #datas = datasel[10:]
               #edd=str(self.eddata.get_text())   
               eedd=datasel.split(' ')
               dataax= eedd[0]
               dx = dataax.split('-')
               dt = str(dx[2])+"/"+str(dx[1])+"/"+str(dx[0])
               self.eddata.set_text(dt)

               print dataax
               self.codmov.set_text(codmov)
               self.breopen.set_sensitive(False)

               nuv=str(numerovenda)
               print "venda re aberta com suscesso !"+ nuv 
               print "vendedor : "+str(codv)
               self.ednumerovenda.set_text(nuv)
               
               self.ednumvendedor.set_sensitive(False) 
               self.ednumvendedor.set_text(str(codv))
               self.btnovavend.set_sensitive(False)
               self.eddata.set_sensitive(False)
               self.ednumerovenda.set_sensitive(False)
               #self.eddata.set_text()
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

               
               selpvendidos = con.cursor()
               selpvendidos.execute("SELECT * FROM tb_mov_merc WHERE n_not_int='"+nuv+"'")
               pvend = selpvendidos.fetchall()
               for pdv in pvend:
                  selpro=con.cursor()
                  selpro.execute("SELECT * FROM pbestoreal WHERE codigo='"+str(pdv[2])+"'")
                  linp = selpro.fetchone()
                  qr=float(linp[7])
                  ql = float(linp[8])
                  qv = float(pdv[3])
                  qlt= ql + qv 
                  
                  if str(pdv[9]) == "898":
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
                        
               
               selpvendidos = con.cursor()
               selpvendidos.execute("DELETE FROM tb_vendas WHERE numop ='"+nuv+"'")
               print "valores na tabela vendas apagodos"
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
             
         else: 
             #print "nao abrir"
             self.ednumerovenda.grab_focus()

         
      if npv == 0:
                print "nao achada "
                self.jnela = gtk.Window(gtk.WINDOW_POPUP)
                self.jnela.set_resizable(False)
                #self.janela.connect("destroy", self.fechaplash)
                self.jnela.set_title("Barra de Progresso")
                self.jnela.set_border_width(0)
                self.jnela.set_position(gtk.WIN_POS_CENTER)
                #self.tempo = gobject.timeout_add(5, self.desenhar_progresso, self.barra_progresso)
                # Cria uma caixa vertical
                vbox = gtk.VBox(False, 5)
                vbox.set_border_width(10)
                self.jnela.add(vbox)

                # Cria uma barra de progresso
                #self.barra_progresso = gtk.ProgressBar()
                #vbox.pack_start(self.barra_progresso, False, False, 0)
                
                # Chamar o método desenhar_progresso a da 5 milisegundos
                self.tempo = gobject.timeout_add(1000, self.fechasplash)
                #print "tempogobjet"
                # Cria uma separador


                # Cria uma etiqueta
                self.etiqueta= gtk.Label()
                self.etiqueta.set_label("Venda Não encontrada !")
                vbox.pack_start(self.etiqueta, False, False, 0)
                separador = gtk.HSeparator()
                vbox.pack_start(separador, False, False, 0)
                # Mostra todas os widgets adicionados na janela
                self.jnela.show_all()

   def fechasplash(self):

      #print "tempo exedido"
      gobject.source_remove(self.tempo)
      self.jnela.destroy()



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
      me="0"+str(ms)
      me= me[-2:]
      d=data[2]
      da="0"+str(d)
      da=da[-2:]
      #dt=str(data[0])+"-"+str(mes[-2:])+"-"+str(dia[-2:])
      dt = str(da)+"/"+str(me)+"/"+str(data[0])
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
      #eeddm= eedd[1]
      eeddm = "0"+str(eedd[1])
      eeddm = eeddm[-2:]
      #eeddd= eedd[0]
      eeddd = "0"+str(eedd[0])
      eeddd= eeddd[-2:]

      eddf= eedda+'-'+eeddm+'-'+eeddd
      return eddf
   def edpout(self,widget,dados):
      p = self.edpreco.get_text()
      prec =p.replace(",",".")
      dsp = self.eddpv.get_text()
      pre = float(prec) 
      self.edpreco.set_text(prec)

      if self.apv != pre : 
         if dsp != " ":
            a = 100 - (pre / self.apv *100)
            self.eddpv.set_text(str(a))
            



   def novavenda(self,widget):
      coa = open('consulta.t','r')
      co = coa.read()
      if co == "1":
        print "modo somente consulta"
        self.btnovavend.set_sensitive(False)
      else :
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
               self.it=0.0
               crianovavenda.execute("INSERT INTO tb_cv (cv,data,vend,vtc,vtv,dpg,aux,n_not_ext,now,cod_mov,v_des,cod_cli) VALUES (NULL,'"+dat+"','"+codv+"','0','0','0','0','0','"+str(now)+"','"+str(self.codmov.get_text())+"','0','1')")  
               nuv =  int(con.insert_id())
               con.commit()
               #nuv= str(numerovenda)
               nuv = str(nuv)
               self.ednumerovenda.set_text(nuv)
               print "nova venda criada com suscesso !"+nuv 
               print "vendedor : "+str(codv)
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
               self.breopen.set_sensitive(False)
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
      self.btnn.set_sensitive(False)
      self.edcsellista.set_text("")

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
          self.codmov.set_text("109")

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
             self.codmov.set_text("109")
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
         self.edqrc.set_text(str(linp[7]))
         #self.edqr.set_text("qr= "+str(linp[7]))
         self.labelpreco.set_sensitive(True)
         self.labelqtd.set_sensitive(True)
         self.btinseri.set_sensitive(True)
         self.exibegrade(str(linp[0]))
         if linp[13] == 100 :
            self.bcolor.set_from_file("image/bag_green.png")
            if linp[7] < linp[8] : 
               self.bcolor.set_from_file("image/bag_black.png")
            if linp[7] == 0 : 
               self.bcolor.set_from_file("image/alert.png")
              
         else :
            self.bcolor.set_from_file("image/bag_white.png")
                     
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
            self.edqrc.set_text(str(linp[7]))
            #self.edqr.set_text("qr= "+str(linpc[7]))
            self.exibegrade(str(linp[0]))
            self.apv= linp[5]
            if linp[13] == 100 :
               self.bcolor.set_from_file("image/bag_green.png")
               if linp[7] < linp[8] : 
                  self.bcolor.set_from_file("image/bag_black.png")
               if linp[7] == 0 : 
                  self.bcolor.set_from_file("image/alert.png")
              
            else :
               self.bcolor.set_from_file("image/bag_white.png")
             
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
      #self.listaprodutosvendidos.clear ()
      self.qtdconta = 0.0
      ncolunas = self.listaprodutosvendidos.get_columns()
      for col in ncolunas:
         self.listaprodutosvendidos.remove_column(col)  

      # definicicao do object MODEL ao qual meu TREEVIEW esta conectado.
      # Toda altarecao no modelo  seguinda pelo objecto visual .
      self.modelo = gtk.ListStore(
            gobject.TYPE_UINT,
            gobject.TYPE_STRING,
            gobject.TYPE_STRING,
            gobject.TYPE_STRING,
            gobject.TYPE_STRING, 
            gobject.TYPE_STRING,
            gobject.TYPE_STRING,gobject.TYPE_STRING,gobject.TYPE_STRING,gobject.TYPE_STRING,gobject.TYPE_STRING)
      ##self.modelo = gtk.TreeStore(str,str,str,str,str,str)
      self.listaprodutosvendidos.set_model(self.modelo)
      #Uso 3 argumentos do Column
      # 1 - Primeiroargumento  o tulo
      # 2 - tipo da coluna, como  mostrada
      # 3 -  posicao do dado(text) no modelo.
      #  4 ... n  - Outras propriedades
      #Coluna 1
      renderer1 = gtk.CellRendererText()
      #renderer1.set_property("background", "white") # Cor do foreground como propriedade
      renderer1.set_property("foreground", "green") # Cor do foreground como propriedade
      #renderer1.set_property('editable', True) # A primeira coluan  editvel
      column = gtk.TreeViewColumn("codigo", renderer1,text=0)
      column.set_sort_column_id(0)
      self.listaprodutosvendidos.append_column(column)
      # Abaixo  adicionada a coluna 2, com a cor definida pelo meu dado, onde foreground=3 indica que
      # a cor de fundo esta na quarta coluna do liststore.
      # e outra maneira de se setar as propriedadesda de cor  da  coluna.
      #Coluna 2
      renderer2 = gtk.CellRendererText()
      #renderer1.set_property("background", "white") # Cor do foreground como propriedade
      renderer2.set_property("foreground", "blue") # Cor do foreground como propriedade
      #renderer1.set_property('editable', True) # A primeira coluan  editvel
      column = gtk.TreeViewColumn("cod barras", renderer2,text=1)
      #column.set_sort_column_id(1)
      self.listaprodutosvendidos.append_column(column)
      column = gtk.TreeViewColumn("descricao",gtk.CellRendererText(), text=2,background=10)     
      column.set_sort_column_id(2)
      self.listaprodutosvendidos.append_column(column)  
      column = gtk.TreeViewColumn('quantidade', gtk.CellRendererText(), text=3,foreground=7,background=8)
      #column.set_sort_column_id(2)
      self.listaprodutosvendidos.append_column(column)
      self.listaprodutosvendidos.append_column(gtk.TreeViewColumn("preco",gtk.CellRendererText(), text=4,foreground=9))      
      self.listaprodutosvendidos.append_column(gtk.TreeViewColumn("subtotal",gtk.CellRendererText(), text=5,foreground=9))
      self.listaprodutosvendidos.append_column(gtk.TreeViewColumn("grade",gtk.CellRendererText(), text=6))
      selnumv =con.cursor()
      numvenda = self.ednumerovenda.get_text()
      
      selnumv.execute("SELECT * FROM tb_cv WHERE cv='"+numvenda+"'")
      lin = selnumv.fetchone()
      self.edtotal.set_text(str(lin[4]))
      self.totalreal = float(lin[4])
      
      selpvendidos=con.cursor()
      selpvendidos.execute("SELECT * FROM tb_mov_merc WHERE n_not_int='"+numvenda+"' ORDER BY i DESC")
      pvend = selpvendidos.fetchall()
      it =0
      self.cppp ={}
      self.inoi ={}
      for pdv in pvend:
         self.qtdconta = self.qtdconta + pdv[3]
         selpro=con.cursor()
         selpro.execute("SELECT * FROM pbestoreal WHERE codigo='"+str(pdv[2])+"'")	
         linp = selpro.fetchone()
         dp = linp[2]
         cb=linp[1]
         pv = linp[5]
         qr = linp[7]
         nc = linp[13]
         self.cppp[it]= str(pdv[2])+ "_" + pdv[8]
         self.inoi[it]=str(pdv[10])
         it +=1
         fundo = None
         cor =None
         corpr = None
         cnc = None
         if nc == 100:
            cnc = "#99FF99"
            if qr < linp[8] :
               cnc = "#FFCC99"
            if linp[7]==0:
               cnc = "#FF0000"
         if pdv[5] < pv :
            corpr = "#FFA500" 
         if pdv[3] < 0 :
            cor="red"
         if qr == 0 :
            fundo = "red"
         if pdv[3] <0 and qr ==0 :
            fundo="blue" 
            cor="red"
         
        
         self.modelo.append([pdv[2],cb,dp,pdv[3],pdv[5],pdv[7],pdv[8],cor,fundo,corpr,cnc])
      self.edcod.set_text('')
      self.edqtd.set_text("1")
      self.eddescp.set_text('')
      self.edpreco.set_text('')
      self.edqrc.set_text('')
      self.edcod.grab_focus()
      self.listaprodutosvendidos_selection = self.listaprodutosvendidos.get_selection()
      self.listaprodutosvendidos_selection.set_mode(gtk.SELECTION_SINGLE)
      self.it = self.qtdconta
      self.entryitens.set_text(str(self.it))
      


   def exibegrade(self,strr):
      codprod = strr
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
         if float(srtt) < 0 : 
             self.codmov.set_text('991')
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
      
      #print self.cppp 
      #print ii
      self.btapaga.set_sensitive(True)
      self.btnn.set_sensitive(True)
      self.edcsellista.set_text(str(self.cppp[f]))
      self.ednni.set_text(str(self.inoi[f]))
  
   def codfocus(self,widget,outro):
      self.btapaga.set_sensitive(False)
      self.btnn.set_sensitive(False)
  
   def btnnclick(self,widget):
      if self.ednni.get_text()=="0":
         self.ednni.set_sensitive(True)
         self.ednni.grab_focus()
      else :
         self.ednni.set_sensitive(False)
         tnt = self.ednni.get_text()
         auxae = self.edcsellista.get_text()
         codpre= auxae.split('_')
         codpr=codpre[0]
         gradpr=codpre[1]
         numvenda = self.ednumerovenda.get_text() 
         
         selpv=con.cursor() 
         # update o produto 
         selpv.execute("UPDATE tb_mov_merc SET n_not_ext='"+str(tnt)+"',cod_mov='898' WHERE n_not_int='"+numvenda+"' AND cod_prod='"+codpr+"' AND grade_sel='"+gradpr+"' ")
         self.ednni.set_text("")
         self.listarprodutosvendidos()
         self.edcod.grab_focus()
 
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
               tax= float(linvenda[3])
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
               self.it=self.it - tax

   def abrejanelafechavenda(self,widget):
      self.janelafechavenda.show_all()
      self.edtota.set_text(self.edtotal.get_text())
      self.edtota.grab_focus()

   def codenter(self,widget,event):
      # print event.keyval
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
      data= self.dataget()
      nw=datetime.now()
      no=str(nw)
      nn = no[11:]
      nnn = nn[:8]
      dat = str(data)+ " " + nnn    
      now=no[:19]
      print "num items ->> "+ str(self.it)

      if t == ftota:
         data = self.caljanela.get_date()
         ms=data[1]+1
         mes="0"+str(ms)
         d=data[2]
         dia="0"+str(d)
         #dt=str(dia[-2:])+"/"+str(mes[-2:])+"/"+str(data[0])
         dt = self.eddata.get_text()
         #dt=str(data[0])+"-"+str(mes[-2:])+"-"+str(dia[-2:])
         if fdin != 0:
            insv = con.cursor()
            insv.execute("INSERT INTO tb_vendas (idcodv,codvend,valorv,fpag,datav,numop,cod_pg,datatime,itens) VALUES (NULL,'"+self.ednumvendedor.get_text()+"','"+str(fdin)+"','dinheiro','"+dt+"','"+str(numvenda)+"','1','"+dat+"','"+str(self.it)+"')")
            print "dinheiro " + str(fdin)
            self.it = 0.0
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
            insv.execute("INSERT INTO tb_vendas (idcodv,codvend,valorv,fpag,datav,numop,cod_pg,datatime,itens) VALUES (NULL,'"+self.ednumvendedor.get_text()+"','"+str(fcar)+"','cartao','"+dt+"','"+str(numvenda)+"','2-"+str(ddcar)+"','"+dat+"','"+str(self.it)+"')")
            print "cartao " + str(fcar)
            self.it = 0.0
         if fche !=0:
            insv = con.cursor()
            insv.execute("INSERT INTO tb_vendas (idcodv,codvend,valorv,fpag,datav,numop,cod_pg,datatime,itens) VALUES (NULL,'"+self.ednumvendedor.get_text()+"','"+str(fche)+"','cheque','"+dt+"','"+str(numvenda)+"','3','"+dat+"','"+str(self.it)+"')")
            print "cheque " + str(fche)
            self.it = 0.0
         fevenda =con.cursor()
         if float(ftota) != float(self.totalreal):
                print "desconto final aplicado"
                vdeff = float(self.totalreal) - float(ftota) 
         else: 
                vdeff=0;
         print "juros cartao = "+ str(dcar) 
         if self.chnt.get_active() == True:#nota tirou
            
            
            upnot = con.cursor()
            upnot.execute("UPDATE tb_mov_merc SET cod_mov='898',n_not_ext='"+self.ednnt.get_text() +"' WHERE n_not_int='"+numvenda+"' ")
            fevenda.execute("UPDATE tb_cv SET vtv='"+str(ftota)+"',dpg='"+str(dcar)+"',aux='"+"d="+str(fdin)+"-c="+str(fcar)+"-h="+str(fche)+"',n_not_ext='"+self.ednnt.get_text()  +"',cod_mov='898',v_des='"+str(vdeff)+"',now='"+now+"' WHERE cv='"+numvenda+"'")
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
             qlt= ql - qv 
             if str(pdv[9]) == "898":
                qrt = qr - qv
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
                   qtdgt=  qtdgrad - qv
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
         self.breopen.set_sensitive(True)
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
  venda()

