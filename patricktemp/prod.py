#!/usr/bin/python
# -*- coding: utf-8 -*-
#Arquivo: prod.py

import pygtk
import gtk
import gtk.glade
from conbd import coneccao
import MySQLdb

jpg = gtk.glade.XML('prod.glade')
japrod = jpg.get_widget('japrod')
procproduto = jpg.get_widget('entry1')
eddescprod = jpg.get_widget('entry3') 
edcod = jpg.get_widget('entry2')
edun = jpg.get_widget('entry4')
edqt = jpg.get_widget('entry8')
edpv = jpg.get_widget('entry5')
edpc = jpg.get_widget('entry6')
btnewprod =jpg.get_widget('button2')
btfind = jpg.get_widget('button1')
btedit = jpg.get_widget('button3')
btgrava =jpg.get_widget('bgravarproduto')

con = MySQLdb.connect("localhost", "root", "uc3r2l")
con.select_db('pbbd')

class japroduto :
   def __init__(self):
      jpg.signal_autoconnect(self)
      japrod.show_all()
      gtk.main()
   
   def showjp (self,widget):
      self.exibeproduto("1")

   def fjaprod(self,widget, data):
      gtk.main_quit()

   def bgravarprod_clicked (self,widget):
      gaprod=con.cursor()
      descp=eddescprod.get_text()
      codp=edcod.get_text()
      unp= edun.get_text()
      qtp= edqt.get_text()
      pvp= edpv.get_text()
      pcp= edpc.get_text()
      ii=  procproduto.get_text()
      gaprod.execute("UPDATE pbbbbbbbbbbbb SET codbarras='"+str(codp)+"',descricaop='"+str(descp)+"',undp='"+str(unp)+"',qtdautalest='"+str(qtp)+"',precov='"+str(pvp)+"',creal='"+str(pcp)+"' WHERE codigo='"+str(ii)+"'")
      

      btfind.set_sensitive(True)
      procproduto.set_sensitive(True)
      btnewprod.set_sensitive(True)
      btedit.set_sensitive(True)
      edun.set_sensitive(False)
      eddescprod.set_sensitive(False)
      edcod.set_sensitive(False)
      edqt.set_sensitive(False)
      edpv.set_sensitive(False)
      edpc.set_sensitive(False)
      btedit.set_sensitive(False)
      btgava.set_sensitive(False)









   def editc(self,widget):
      btfind.set_sensitive(False)
      procproduto.set_sensitive(False)
      btnewprod.set_sensitive(False)
      edun.set_sensitive(True)
      eddescprod.set_sensitive(True)
      edcod.set_sensitive(True)
      edqt.set_sensitive(True)
      edpv.set_sensitive(True)
      edpc.set_sensitive(True)
      btedit.set_sensitive(False) 
      btgrava.set_sensitive(True)

   def newproduto (self,widget):

       luprod=con.cursor()
       luprod.execute("SELECT * FROM pbbbbbbbbbbbb ORDER BY `codigo` DESC")
       lluprod = luprod.fetchone()
       #print str(lluprod[0])
       ult= int(lluprod[0])+1
       iprod = con.cursor()
       iprod.execute("INSERT INTO `pbbd`.`pbbbbbbbbbbbb`(`codigo` ,`codbarras` ,`descricaop` ,`fornecedorp` ,`undp` ,`precov` ,`custoc` ,`qtdautalest` ,`qestlj1` ,`qestl2` ,`qestlj3` ,`qmin` ,`creal` ,`nc` ,`grade` ,`class`)VALUES ('"+str(ult)+"', 'cod', 'descricao', '', 'und', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0','0.00', '', '', '');")
       lprod=con.cursor()
       strprocurado = str(ult)
       self.exibeproduto(strprocurado)

       btfind.set_sensitive(False)
       procproduto.set_text(str(ult))
       procproduto.set_sensitive(False)
       btnewprod.set_sensitive(False)
       self.editc("1")
       
       
   def exibeproduto (self,strp):

      lprod=con.cursor()
      strprocurado = strp
      lprod.execute("SELECT * FROM pbbbbbbbbbbbb WHERE codbarras='"+strprocurado+"'")
      npe = int(lprod.rowcount)
      if npe ==1:
         llprod = lprod.fetchone()  
         eddescprod.set_text(str(llprod[2]))
         edcod.set_text(str(llprod[1]))
         edun.set_text(str(llprod[4]))
         edqt.set_text(str(llprod[7]))
         edpv.set_text(str(llprod[5]))
         edpc.set_text(str(llprod[12]))
      else: 
         lprod.execute("SELECT * FROM pbbbbbbbbbbbb WHERE codigo='"+strprocurado+"'")
         npee = int(lprod.rowcount)
         if npee ==1:
                    llprod = lprod.fetchone()
     		    eddescprod.set_text(str(llprod[2]))
    		    edcod.set_text(str(llprod[1]))
    		    edun.set_text(str(llprod[4]))
  		    edqt.set_text(str(llprod[7]))
  		    edpv.set_text(str(llprod[5]))
  		    edpc.set_text(str(llprod[12]))
         else :
               print " "
          



   def pexibeproduto (self,strp):

    
      strp = procproduto.get_text()
      self.exibeproduto(strp)
      
      
