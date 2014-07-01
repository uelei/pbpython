#!/usr/bin/python
# -*- coding: utf-8 -*-
#Arquivo: pbbd.py

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
   import MySQLdb
   import datetime
   from datetime import datetime
except:
   print "impossivel carregar as bibliotecas "
   exit(1)
 
try:
     print "conectando ..."
     con = MySQLdb.connect(host="localhost",user="root",passwd="uc3r2l",db="pbbd",charset="utf8",use_unicode=True)
     #bd=MySQLdb.connect(host="localhost",user="python",passwd="python",db="python",charset="utf8", use_unicode = True) 
except:
     print "Erro ao conectar ao banco de dados"
     exit()
else: 
     #con.select_db('pbbd')
     print "conectado ... OK"
     
from prod import japroduto 
print "importado janela produto"

class Aplicacao:
   def __init__(self):

#Carrega a interface a partir do arquivo glade
    aw = gtk.glade.XML('pb.glade')
#carrega os widgets

#janela principal
    self.janelapb = aw.get_widget('pbjanelaprincipal')
    self.bttotalvendas = aw.get_widget('bttotalvendas')
#janela fecha vendas
    self.janelafechavenda = aw.get_widget('janelafechavenda')
    self.edtota = aw.get_widget('edtota')
    self.eddin = aw.get_widget('eddin')
    self.edcar = aw.get_widget('edcar')
    self.edche = aw.get_widget('edche')
    self.btfechavenda = aw.get_widget('btfechavenda')
    self.cbfp = aw.get_widget('cbfp')
    self.chnt = aw.get_widget('chnt')
    self.ednnt = aw.get_widget('ednnt')
    
#janela totalvendas
    self.janelatotalvendas = aw.get_widget('janelatotalvendas')

    self.tabelatotalvendas= aw.get_widget('treeview')
    self.calendar = aw.get_widget('calendar1')
    self.rbdia = aw.get_widget('rdtotaldia')
    self.rbmes = aw.get_widget('rdtotalmes')
    self.rbano = aw.get_widget('rdtotalano')

#janela de venda

    self.janelavenda = aw.get_widget('janelavenda')
    self.ednumvendedor = aw.get_widget('ednumvendedor')
    self.eddata= aw.get_widget('eddata')
    self.btnovavend = aw.get_widget('btnovavend')
    self.ednumerovenda=aw.get_widget('ednumvenda')
    self.btsair = aw.get_widget('btsair')
    self.labelcod = aw.get_widget('label12')
    self.labelqtd = aw.get_widget('label14')
    self.edcod = aw.get_widget('edcod')
    self.edqtd = aw.get_widget('edqtd')
    self.labelpreco = aw.get_widget('label15')
    self.edpreco = aw.get_widget('edprecov')
    self.btinseri = aw.get_widget('btinseri')
    self.btapaga = aw.get_widget('btapaga')
    self.labeldescp = aw.get_widget('label13')
    self.eddescp = aw.get_widget('eddescp')
    self.listaprodutosvendidos = aw.get_widget('listaprodutosvendidos')
    self.labeltotal =aw.get_widget('label16')
    self.edtotal = aw.get_widget('edtotal')
    self.btfinalizar = aw.get_widget('btfinalizar')
    self.edgrade = aw.get_widget('edgrade')
    self.edcodigo = aw.get_widget('edcodigo')
    self.la1 = aw.get_widget('la1')
    self.edt1 = aw.get_widget('edt1')
    self.la2 = aw.get_widget('la2')
    self.edt2 = aw.get_widget('edt2')
    self.la3 = aw.get_widget('la3')
    self.edt3 = aw.get_widget('edt3')
    self.la4 = aw.get_widget('la4')
    self.edt4 = aw.get_widget('edt4')
    self.la5 = aw.get_widget('la5')
    self.edt5 = aw.get_widget('edt5')
    self.la6 = aw.get_widget('la6')
    self.edt6 = aw.get_widget('edt6')
    self.edpc = aw.get_widget('edpc')
    self.edp2 = aw.get_widget('edp2')
    self.edc2 = aw.get_widget('edc2')
    self.edqr = aw.get_widget('edqr')
#janela de calendario 
    self.janelacalendario = aw.get_widget('janelacalendario')
    self.caljanela = aw.get_widget('caljanela')    

#janelagrade
    self.janelagrade = aw.get_widget('janelagrade')
    self.btcancelagrade = aw.get_widget('btcancelagrade')
    self.btokgrade = aw.get_widget('btokgrade')
    self.ra1 = aw.get_widget('ra1')
    self.ra2 = aw.get_widget('ra2')
    self.ra3 = aw.get_widget('ra3')
    self.ra4 = aw.get_widget('ra4')
    self.ra5 = aw.get_widget('ra5')
    self.ra6 = aw.get_widget('ra6')
    self.eda1 = aw.get_widget('eda1')
    self.eda2 = aw.get_widget('eda2')
    self.eda3 = aw.get_widget('eda3')
    self.eda4 = aw.get_widget('eda4')
    self.eda5 = aw.get_widget('eda5')
    self.eda6 = aw.get_widget('eda6')
    self.edcodgrade = aw.get_widget('edcodgrade')
#janela produto
    self.janelaproduto = aw.get_widget('janelaproduto')
    self.edlocalizarproduto = aw.get_widget('edlocalizarproduto')
    self.spin = aw.get_widget('spinbutton1')

#Conecta todos os Sinais aos Callbacks
    aw.signal_autoconnect(self)

#Exibe janela principalpb
    self.janelapb.show_all()

#Inicia o loop principal de eventos (GTK MainLoop)
    gtk.main()
    
#Callbacks = acoes 
   def localizarproduto(self,widget):
      stringprocurado = self.edlocalizarproduto.get_text()
      lcp= con.cursor()
      lcp.execute("SELECT * FROM pbestoreal WHERE codigo='"+stringprocurado+"'")
      linlc = lcp.fetchone()
      self.spin.set_text(str(linlc[7]))

   def procuraproduto (self,widget):
      self.btapaga.set_sensitive(False)
      strprocurado = self.edcod.get_text()
      pcp=con.cursor()
      pcp.execute("SELECT * FROM pbestoreal WHERE codigo='"+strprocurado+"'")
      npe = int(pcp.rowcount)
      if npe ==1:  
        
         self.labelcod.set_text("codigo")
         linp = pcp.fetchone()
         self.eddescp.set_text(str(linp[2]))
         self.edpreco.set_text(str(linp[5]))
         self.edcodigo.set_text(str(linp[0]))
         self.edpc.set_text(str(linp[12]))
         self.edqr.set_text("qr= "+str(linp[7]))
         grade=str(linp[14])
         if grade == "s":
            
            self.listagrade(linp[0])
         else:
            self.naopossuigrade()
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
            grade=str(linpc[14])
            self.edpc.set_text(str(linpc[12]))
            self.edqr.set_text("qr= "+str(linpc[7]))
            if grade == "s":
              
               self.listagrade(linpc[0])
            else :
               self.naopossuigrade()
         else:
            self.labelcod.set_text("codigo")
            self.eddescp.set_text("Produto nao encontrado")
            self.edpreco.set_text(" ")
            self.edcodigo.set_text('')
            self.edpc.set_text("")
            self.edqr.set_text("")
            self.naopossuigrade()

   def listagrade(self,grd):
      sgrade=con.cursor()
      sgrade.execute("SELECT * FROM grade WHERE codigo='"+str(grd)+"'")  
      gra= sgrade.fetchone()  
      self.la1.set_sensitive(True)
      self.la1.set_text(str(gra[7]))
      self.edt1.set_text(str(gra[1]))
      self.la2.set_sensitive(True)
      self.la2.set_text(str(gra[8]))
      self.edt2.set_text(str(gra[2]))
      self.la3.set_sensitive(True)
      self.la3.set_text(str(gra[9]))
      self.edt3.set_text(str(gra[3]))
      self.la4.set_sensitive(True)
      self.la4.set_text(str(gra[10]))
      self.edt4.set_text(str(gra[4]))
      self.la5.set_sensitive(True)
      self.la5.set_text(str(gra[11]))
      self.edt5.set_text(str(gra[5]))
      self.la6.set_sensitive(True)
      self.la6.set_text(str(gra[12]))
      self.edt6.set_text(str(gra[6]))
   def naopossuigrade(self):
      self.la1.set_sensitive(False)
      self.la1.set_text('')
      self.edt1.set_text('')
      self.la2.set_sensitive(False)
      self.la2.set_text('')
      self.edt2.set_text('')
      self.la3.set_sensitive(False)
      self.la3.set_text('')
      self.edt3.set_text('')
      self.la4.set_sensitive(False)
      self.la4.set_text('')
      self.edt4.set_text('')
      self.la5.set_sensitive(False)
      self.la5.set_text('')
      self.edt5.set_text('')
      self.la6.set_sensitive(False)
      self.la6.set_text('')
      self.edt6.set_text('')
      

   def ednumvendedorenter(self,widget,event):
      if event.keyval == 65293:
         self.novavenda(self)
   def edqtdenter(self,widget,event):
      if event.keyval ==65293:
         self.edpreco.grab_focus()
   def edprecoenter(self,widget,event):
      if event.keyval == 65293:
         self.btinseri.grab_focus()
   def eddescpin (self,widget,event):
      self.edcod.grab_focus()


   def btinserirproduto (self,widget):
      self.edp2.set_text(self.edpreco.get_text())
      self.edc2.set_text(self.edcodigo.get_text())
      numvenda = self.ednumerovenda.get_text()
      strprocurado = self.edcodigo.get_text()
      pcp=con.cursor()
      pcp.execute("SELECT * FROM pbestoreal WHERE codigo='"+strprocurado+"'")
      npe = int(pcp.rowcount)
      if npe ==1:
         linp = pcp.fetchone()
         grade=str(linp[14])
         if grade == "s": 
            if self.edgrade.get_text() == "":
               self.abrejanelagrade(self,strprocurado)
            else: 
               print "erro gradeja selecionado "
         else:
            self.gravainsersaodeproduto()
           
      else:
         print "produto inexistente !"
         self.edcod.grab_focus()





   def gravainsersaodeproduto(self):

      if self.edgrade.get_text()=="":
         self.edgrade.set_text(' ')
      numvenda = self.ednumerovenda.get_text()
      selpvendidos=con.cursor()
      strprocurado = self.edcodigo.get_text()
      grd= self.edgrade.get_text()
      selpvendidos.execute("SELECT * FROM tbrpv WHERE cv='"+numvenda+"' AND cp='"+strprocurado+"' AND tam='"+grd+"'")
      npv=int(selpvendidos.rowcount)
      if npv >= 1:  
         linpven = selpvendidos.fetchone()
         ii = linpven[0]
         qtdv = linpven[3]
         pcd =linpven[4]
         pvd = linpven[5]
         pctq = linpven[6]
         pvtq = linpven[7]
         seltvenda =con.cursor()
         seltvenda.execute("SELECT * FROM tbtvc WHERE cv='"+numvenda+"'")
         linvenda = seltvenda.fetchone()
         vct= linvenda[3]
         vvt= linvenda[4]
         cu=self.edpc.get_text()
         cu=cu.replace(",",".")
         vu = self.edpreco.get_text()
         vu=vu.replace(",",".")
         qtd = self.edqtd.get_text()
         qtd=qtd.replace(",",".")
         qtdt = float(qtd) + float(qtdv)
         cut= float(cu)*float(qtdt)

         if qtdt ==0:

            apsql=con.cursor()
            apsql.execute("DELETE FROM tbrpv WHERE ii='"+str(ii)+"'")
            print "produto "+self.edcodigo.get_text() + " apagado !"
         else:
            cuu= cut / qtdt
            pvqtd=float(vu) * float(qtd)
            pvt=pvqtd+float(pvtq)
            pvunit= pvt/qtdt
            upp=con.cursor()
            upp.execute("UPDATE tbrpv SET qtd='"+str(qtdt)+"',pvd='"+str(pvunit)+"',pctq='"+str(cuu)+"',pvtq='"+str(pvt)+"' WHERE ii='"+str(ii)+"'")
            print "produto "+self.edcodigo.get_text() + " acrescentado !"
         cu=self.edpc.get_text()
         cu=cu.replace(",",".")
         vu = self.edpreco.get_text()
         vu=vu.replace(",",".")
         qtd = self.edqtd.get_text()
         qtd=qtd.replace(",",".")         
         tc = float(cu)* float(qtd)
         tv = float(vu) * float(qtd)
         ttc = vct+tc
         ttv = vvt+tv
         seltvenda.execute("UPDATE tbtvc SET vlc='"+str(ttc)+"',vlv='"+str(ttv)+"' WHERE cv='"+numvenda+"'")
         con.commit() 

      else:
         seltvenda =con.cursor()
         seltvenda.execute("SELECT * FROM tbtvc WHERE cv='"+numvenda+"'")
         linvenda = seltvenda.fetchone()
         vct= linvenda[3]
         vvt= linvenda[4]

         qtd = self.edqtd.get_text()
         qtd=qtd.replace(",",".")

         cu=self.edpc.get_text()
         cu=cu.replace(",",".")

         qtg=float(qtd)
         tc = float(cu)* qtg
         vu = self.edp2.get_text()
         vu=vu.replace(",",".")

         vg = float(vu)
         tv = vg * qtg
         ttc = vct+tc
         ttv = vvt+tv
         insp = con.cursor()
         codpro = self.edc2.get_text()
         insp.execute("INSERT INTO tbrpv (ii,cv,cp,qtd,pcd,pvd,pctq,pvtq,nt,tam) VALUES(NULL,'"+numvenda+"','"+codpro+"','"+str(qtd)+"','"+str(cu)+"','"+str(vu)+"','"+str(tc)+"','"+str(tv)+"','"+numvenda+"','"+str(self.edgrade.get_text())+"')")
         con.commit()
         print "produto "+self.edcodigo.get_text() + " inserido !"
         seltvenda.execute("UPDATE tbtvc SET vlc='"+str(ttc)+"',vlv='"+str(ttv)+"' WHERE cv='"+numvenda+"'")

      
      self.edgrade.set_text("")
      self.edcod.set_text("") 
      
      self.listarprodutosvendidos()
      

   def abrejanelatotalvendas(self, widget):
    self.janelatotalvendas.show_all()
   def abrejanelaproduto(self, widget):
      #self.janelaproduto.show_all()
      japroduto()
      
   def novavenda(self,widget):
      if self.ednumvendedor.get_text() !="": 
         numvendedor=self.ednumvendedor.get_text()
         try: 
            nuv= int(numvendedor)
         except:
            print "numero do vendedor invalido (letra)"
         else: 
            n=0
            selvendedor = con.cursor()
            codv=self.ednumvendedor.get_text()
            selvendedor.execute("SELECT * FROM vendedores WHERE codv='"+codv+"'")
            numlinhas = int(selvendedor.rowcount)
            if numlinhas ==1:
               #print "vendedor valido "
               selultimavenda = con.cursor()
               selultimavenda.execute("SELECT * FROM tbtvc ORDER BY cv ASC")
               for vendas in selultimavenda:
                  numvenda= vendas[0]
               numerovenda= int(numvenda)
               numerovenda=numerovenda +1
               crianovavenda= con.cursor()
               data= self.eddata.get_text()
               nw=datetime.now()
               no=str(nw)
               now=no[:19]
               crianovavenda.execute("INSERT INTO tbtvc (cv,data,vend,vlc,vlv,dpg,aux,cvr,now) VALUES ('"+str(numerovenda)+"','"+data+"','"+codv+"','0','0','0','0','0','"+str(now)+"')")  
               con.commit()
               nuv= str(numerovenda)
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
               self.labeldescp.set_sensitive(True)
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
   def abrejanelavenda(self, widget):
      self.janelavenda.show_all()
      self.ednumvendedor.grab_focus() ##rotina para por focus no edit
      data = self.caljanela.get_date()
      ms=data[1]+1
      mes="0"+str(ms)
      d=data[2]
      dia="0"+str(d)
      #dt = str(data[0])+"-"+str(mes[-2:]+"-"+str(dia[-2:])
      dt=str(data[0])+"-"+str(mes[-2:])+"-"+str(dia[-2:])
      self.eddata.set_text(dt)
   def codenter(self,widget,event):
     # print event.keyval
      if event.keyval ==65293:
         self.btinserirproduto(self)
      if event.keyval ==65421:
         self.btinserirproduto(self)   
      if event.keyval ==65472:
         self.abrejanelafechavenda(self)

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
      self.listaprodutosvendidos.append_column(gtk.TreeViewColumn("tam",gtk.CellRendererText(), text=6))
      selnumv =con.cursor()
      numvenda = self.ednumerovenda.get_text()
      selnumv.execute("SELECT * FROM tbtvc WHERE cv='"+numvenda+"'")
      lin = selnumv.fetchone()
      self.edtotal.set_text(str(lin[4]))
      selpvendidos=con.cursor()
      selpvendidos.execute("SELECT * FROM tbrpv WHERE cv='"+numvenda+"'")
      pvend = selpvendidos.fetchall()
      for pdv in pvend:
         selpro=con.cursor()
         selpro.execute("SELECT * FROM pbestoreal WHERE codigo='"+str(pdv[2])+"'")	
         linp = selpro.fetchone()
         dp = linp[2]
         cb=linp[1]
         self.tipodetabelavenda.append([pdv[2],cb,dp,pdv[3],pdv[5],pdv[7],pdv[9]])
      self.edcod.set_text('')
      self.edqtd.set_text("1")
      self.eddescp.set_text('')
      self.edpreco.set_text('')
      self.edcod.grab_focus()

      
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
    self.tipodetabela = gtk.ListStore(str,str,str,str,str)
    self.tabelatotalvendas.set_model(self.tipodetabela)
    self.tabelatotalvendas.append_column(gtk.TreeViewColumn("vendedor",gtk.CellRendererText(), text=0))
    self.tabelatotalvendas.append_column(gtk.TreeViewColumn("diheiro",gtk.CellRendererText(), text=1))
    self.tabelatotalvendas.append_column(gtk.TreeViewColumn("cartao",gtk.CellRendererText(), text=2))
    self.tabelatotalvendas.append_column(gtk.TreeViewColumn("cheque",gtk.CellRendererText(), text=3))
    self.tabelatotalvendas.append_column(gtk.TreeViewColumn("total",gtk.CellRendererText(), text=4))
    dint=0
    cart=0
    chet=0
    ttt=0
    myvor= con.cursor()
    myvor.execute("SELECT * FROM vendedores")
    tt=0
    myrvor= myvor.fetchall()
    for vendedor in myrvor:
     din=0
     car=0
     che=0
     tt=0
     ven= vendedor[0]
     data = self.calendar.get_date()
     ms=data[1]+1
     mes="0"+str(ms)
     d=data[2]
     dia="0"+str(d)
     if self.rbdia.get_active():
        dt=dia[-2:]+"/"+str(mes[-2:])+"/"+str(data[0])
     elif self.rbmes.get_active():
        dt="/"+str(mes[-2:])+"/"+str(data[0])
     else:
        dt="/"+str(data[0])
     myvd=con.cursor()
     myvd.execute("SELECT * FROM vendas WHERE codvend='"+str(ven)+"' AND datav like '%"+str(dt)+"%' AND fpag='dinheiro'")
     rsd= myvd.fetchall()
     for vd in rsd:
        din=din+vd[2]
     myvc=con.cursor()
     myvc.execute("SELECT * FROM vendas WHERE codvend='"+str(ven)+"' AND datav like '%"+str(dt)+"%' AND fpag='cartao'")
     rsc= myvc.fetchall()
     for vc in rsc:
        car=car+vc[2]
     myvh=con.cursor()
     myvh.execute("SELECT * FROM vendas WHERE codvend='"+str(ven)+"' AND datav like '%"+str(dt)+"%' AND fpag='cheque'")
     rsh= myvh.fetchall()
     for vh in rsh:
        che=che+vh[2]
     tt=din+car+che
     self.tipodetabela.append([ven,din,car,che,tt])
     dint=dint+din
     cart=cart+car
     chet = chet + che
     ttt=ttt+tt 
    self.tipodetabela.append(["subtotal",dint,cart,chet,ttt])
   def soma(self,widget):
     self.somatotalvendas()
#janela grade acoes 
   def abrejanelagrade(self,widget,codp):
      self.edcodgrade.set_text(codp)
      selgra= con.cursor()
      selgra.execute("SELECT * FROM grade WHERE codigo='"+codp+"'")
      lgra  = selgra.fetchone()
      self.ra1.set_active(False) 
      self.ra1.grab_focus()
      self.ra1.set_sensitive(True)
      self.ra2.set_sensitive(True)
      self.ra3.set_sensitive(True)
      self.ra4.set_sensitive(True)
      self.ra5.set_sensitive(True)
      self.ra6.set_sensitive(True)
      self.janelagrade.show_all()
      self.ra1.set_label(str(lgra[7]))
      self.eda1.set_text(str(lgra[1]))
      self.ra2.set_label(str(lgra[8]))
      self.eda2.set_text(str(lgra[2]))
      self.ra3.set_label(str(lgra[9]))
      self.eda3.set_text(str(lgra[3]))
      self.ra4.set_label(str(lgra[10]))
      self.eda4.set_text(str(lgra[4]))
      self.ra5.set_label(str(lgra[11]))
      self.eda5.set_text(str(lgra[5]))
      self.ra6.set_label(str(lgra[12]))
      self.eda6.set_text(str(lgra[6]))
      if str(lgra[7])=="--":
         self.ra1.set_sensitive(False)
      if str(lgra[8])=="--":
         self.ra2.set_sensitive(False)
      if str(lgra[9])=="--":
         self.ra3.set_sensitive(False)
      if str(lgra[10])=="--":
         self.ra4.set_sensitive(False)
      if str(lgra[11])=="--":
         self.ra5.set_sensitive(False)
      if str(lgra[12])=="--":
         self.ra6.set_sensitive(False)
      self.janelagrade.show_all()



   def fechajgrade(self,widget,codp):
      self.janelagrade.hide()

   def btcancelgrade(self,widget):
      
      self.edcod.grab_focus()
      self.edgrade.set_text("")
      self.janelagrade.hide()

   def ra1sel(self,widget,event):
      if event.keyval ==32 or event.keyval ==65293:
         self.edgrade.set_text(self.ra1.get_label())
         self.janelagrade.hide()
         self.gravainsersaodeproduto()
   def ra2sel(self,widget,event):
      if event.keyval ==32 or event.keyval ==65293:
         self.edgrade.set_text(self.ra2.get_label())
         self.janelagrade.hide()
         self.gravainsersaodeproduto()
   def ra3sel(self,widget,event):
      if event.keyval ==32 or event.keyval ==65293:
         self.edgrade.set_text(self.ra3.get_label())
         self.janelagrade.hide()
         self.gravainsersaodeproduto()

   def ra4sel(self,widget,event):
      if event.keyval ==32 or event.keyval ==65293:
         self.edgrade.set_text(self.ra4.get_label())
         self.janelagrade.hide()
         self.gravainsersaodeproduto()
   def ra5sel(self,widget,event):
      if event.keyval ==32 or event.keyval ==65293:
         self.edgrade.set_text(self.ra5.get_label())
         self.janelagrade.hide()      
         self.gravainsersaodeproduto()
   def ra6sel(self,widget,event):
      if event.keyval ==32 or event.keyval ==65293:
         self.edgrade.set_text(self.ra6.get_label())
         self.janelagrade.hide()
         self.gravainsersaodeproduto()
   def btokgradeclick(self,widget):
      if self.edgrade.get_text() != "":
         self.janelagrade.hide()
         self.gravainsersaodeproduto()
      else: 
         print "selecione grade"
   def abrejanelafechavenda(self,widget):
      self.janelafechavenda.show_all()
      self.edtota.set_text(self.edtotal.get_text())
      self.edtota.grab_focus()
 
   def fechajanelafechavenda(self,widget):
      self.janelafechavenda.hide()
      self.edcod.grab_focus()
   def xfechavenda(self,widget,data):
      self.janelafechavenda.hide()
      self.edcod.grab_focus()
      self.cbfp.set_active_text(None)

   def edtotaenter(self,widget,event):
      if event.keyval == 65293:
         self.eddin.grab_focus()
         tota=self.edtota.get_text()
         tota= tota.replace(",",".")
         self.edtota.set_text(tota)
      if event.keyval == 65363:
         self.chnt.grab_focus()



   def edtotaout(self,widget,event):
      self.eddin.grab_focus()
      tota=self.edtota.get_text()
      tota= tota.replace(",",".")
      self.edtota.set_text(tota)
   def eddinenter(self,widget,event):
      if event.keyval == 65293:
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
         ftota = float(tota)
         fdin = float(din)


   def edcarenter(self,widget,event):
      if event.keyval == 65293:
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
      if event.keyval == 65293:
         self.btfechavenda.grab_focus()
         che = self.edche.get_text()
         che = che.replace(",",".")
         self.edche.set_text(che)

   def edcheout(self,widget,data):
      che = self.edche.get_text()
      che = che.replace(",",".")
      self.edche.set_text(che)



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
      if t == ftota:
         data = self.caljanela.get_date()
         ms=data[1]+1
         mes="0"+str(ms)
         d=data[2]
         dia="0"+str(d)
         dt=str(dia[-2:])+"/"+str(mes[-2:])+"/"+str(data[0])
         #dt=str(data[0])+"-"+str(mes[-2:])+"-"+str(dia[-2:])
         if fdin != 0:
            insv = con.cursor()
            insv.execute("INSERT INTO vendas (idcodv,codvend,valorv,fpag,datav,numop) VALUES (NULL,'"+self.ednumvendedor.get_text()+"','"+str(fdin)+"','dinheiro','"+dt+"','"+str(numvenda)+"')")
            print "dinheiro " + str(fdin)

         if fcar !=0:
            insv = con.cursor()
            insv.execute("INSERT INTO vendas (idcodv,codvend,valorv,fpag,datav,numop) VALUES (NULL,'"+self.ednumvendedor.get_text()+"','"+str(fcar)+"','cartao','"+dt+"','"+str(numvenda)+"')")
            print "cartao " + str(fcar)
         if fche !=0:
            insv = con.cursor()
            insv.execute("INSERT INTO vendas (idcodv,codvend,valorv,fpag,datav,numop) VALUES (NULL,'"+self.ednumvendedor.get_text()+"','"+str(fche)+"','cheque','"+dt+"','"+str(numvenda)+"')")
            print "cheque " + str(fche)
         fevenda =con.cursor()
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
         print "juros cartao = "+ str(dcar) 
         fevenda.execute("UPDATE tbtvc SET vlv='"+str(ftota)+"',dpg='"+str(dcar)+"',aux='"+"d="+str(fdin)+"-c="+str(fcar)+"-h="+str(fche)+"',cvr='"+self.ednnt.get_text()  +"' WHERE cv='"+numvenda+"'")
         selpvendidos = con.cursor()
         selpvendidos.execute("SELECT * FROM tbrpv WHERE cv='"+numvenda+"'")
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
         pvend = selpvendidos.fetchall()
         for pdv in pvend:
            
            if self.chnt.get_active() == True:#nota tirou
               selpro=con.cursor()
               selpro.execute("SELECT * FROM pbestoreal WHERE codigo='"+str(pdv[2])+"'")
               linp = selpro.fetchone()
               qr=float(linp[7])
               qloja = float(linp[8])
               qv = float(pdv[3])
               qrt = qr - qv	
               qlojat= qloja - qv 
               upprod=con.cursor()
               
               upprod.execute("UPDATE pbestoreal SET qtdautalest='"+str(qrt)+"',qestlj1='"+str(qlojat)+"' WHERE codigo='"+str(pdv[2])+"'")
               if qv < 0: 
                  
                  inmo=con.cursor()
                  qd=qv * -1
                  inmo.execute("INSERT INTO movimentos (ci,codp,qtdm,coop,data,tam) VALUES ('"+str(pdv[0])+"','"+str(pdv[2])+"','"+str(qd)+"','991','"+self.eddata.get_text()+"','"+str(pdv[9])+"')")
               elif qv >0:#898 saida con nt
                  
                  inmo=con.cursor()
                  inmo.execute("INSERT INTO movimentos (ci,codp,qtdm,coop,data,tam) VALUES ('"+str(pdv[0])+"','"+str(pdv[2])+"','"+str(qv)+"','898','"+self.eddata.get_text()+"','"+str(pdv[9])+"')")
               else:
                 print "erro na saida do produto = " + pdv[2]

            else:
               selpro=con.cursor()
               selpro.execute("SELECT * FROM pbestoreal WHERE codigo='"+str(pdv[2])+"'")
               linp = selpro.fetchone()
               qloja = float(linp[8])
               qv = float(pdv[3])
               qlojat= qloja - qv 
               upprod=con.cursor()
               upprod.execute("UPDATE pbestoreal SET qestlj1='"+str(qlojat)+"' WHERE codigo='"+str(pdv[2])+"'")
               if qv < 0: 
                  
                  inmo=con.cursor()
                  qd=qv * -1
                  inmo.execute("INSERT INTO movimentos (ci,codp,qtdm,coop,data,tam) VALUES ('"+str(pdv[0])+"','"+str(pdv[2])+"','"+str(qd)+"','991','"+self.eddata.get_text()+"','"+str(pdv[9])+"')")
               elif qv >0:
                   #898 saida con nt
                  
                  inmo=con.cursor()
                  inmo.execute("INSERT INTO movimentos (ci,codp,qtdm,coop,data,tam) VALUES ('"+str(pdv[0])+"','"+str(pdv[2])+"','"+str(qv)+"','109','"+self.eddata.get_text()+"','"+str(pdv[9])+"')")
               else:
                 print "erro na saida do produto = " + pdv[2]
            #dar baixa na grade 
            if linp[14]=="s":
               selgrade=con.cursor()
               selgrade.execute("SELECT * FROM grade WHERE codigo='"+str(pdv[2])+"'")
               lg = selgrade.fetchone()
               if lg[7]== pdv[9]:
                  a=float(lg[1])
                  ad=a - qv
                  upgrade=con.cursor()
                  upgrade.execute("UPDATE grade SET t1='"+str(ad)+"' WHERE codigo='"+str(pdv[2])+"'")
                                    
               elif lg[8]==pdv[9]:
                  a=float(lg[2])
                  ad=a - qv
                  upgrade=con.cursor()
                  upgrade.execute("UPDATE grade SET t2='"+str(ad)+"' WHERE codigo='"+str(pdv[2])+"'")
                  
               elif lg[9]==pdv[9]:
                  a=float(lg[3])
                  ad=a - qv
                  upgrade=con.cursor()
                  upgrade.execute("UPDATE grade SET t3='"+str(ad)+"' WHERE codigo='"+str(pdv[2])+"'")
                  
               elif lg[10]==pdv[9]:
                  
                  a=float(lg[4])
                  ad=a - qv
                  upgrade=con.cursor()
                  upgrade.execute("UPDATE grade SET t4='"+str(ad)+"' WHERE codigo='"+str(pdv[2])+"'")
               elif lg[11]==pdv[9]:
      
                  a=float(lg[5])
                  ad=a - qv
                  upgrade=con.cursor()
                  upgrade.execute("UPDATE grade SET t5='"+str(ad)+"' WHERE codigo='"+str(pdv[2])+"'")
               elif lg[12]==pdv[9]:
                  
                  a=float(lg[6])
                  ad=a - qv
                  upgrade=con.cursor()
                  upgrade.execute("UPDATE grade SET t6='"+str(ad)+"' WHERE codigo='"+str(pdv[2])+"'")
               else: 
                  print "erro de grade "
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
         self.labeldescp.set_sensitive(False)
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

   def cbfpenter(self,widget,event):
      if event.keyval == 65293:
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
         
   def btsairvenda(self,widget):
      self.janelavenda.hide()
      return True

#Sai do loop principal de eventos, finalizando o programa
   def sair(self, widget, data):

    con.close()   
    gtk.main_quit()
    
#Inicia a aplicacao
if __name__ == "__main__":
   Aplicacao()
  
      

