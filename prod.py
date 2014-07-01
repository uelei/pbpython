#!/usr/bin/python
# -*- coding: utf-8 -*-
#Arquivo: prod.py

import pygtk
import gtk
import gtk.glade
from conbd import con,cnn
import datetime
import time
from datetime import datetime
import sys
import gobject

ano, mes, dia, hora, minuto, segundo, semana, juliano, verao= time.localtime()


arquivo = open("novo.txt","r")
conteudo= arquivo.read()
arquivo.close()

class japroduto :
   def __init__(self):
      jpg = gtk.glade.XML('prod.glade')
      self.japrod = jpg.get_widget('japrod')
      self.procproduto = jpg.get_widget('entry1')
      self.eddescprod = jpg.get_widget('entry3')
      self.edcodp = jpg.get_widget('entry12') 
      self.edcod = jpg.get_widget('entry2')
      self.edun = jpg.get_widget('entry4')
      self.edqt = jpg.get_widget('entry8')
      self.edpv = jpg.get_widget('entry5')
      self.edpc = jpg.get_widget('entry6')
      self.btnewprod = jpg.get_widget('button2')
      self.btfind = jpg.get_widget('button1')
      self.btedit = jpg.get_widget('button3')
      self.btgrava = jpg.get_widget('bgravarproduto')
      self.btagrad = jpg.get_widget('button4')
      self.edtgrad = jpg.get_widget('entry7')
      self.edqgrad = jpg.get_widget('entry9')
      self.edqtrc = jpg.get_widget('entry10')
      self.btat = jpg.get_widget('button8')
      self.btrec = jpg.get_widget('button5')
      self.cbgrad = jpg.get_widget('combobox1')
      self.btrc = jpg.get_widget('but')
      self.barra = jpg.get_widget('progressbar1')
      self.btatual = jpg.get_widget('button6')
      self.edcrent = jpg.get_widget('entry11')
      self.tabelamov = jpg.get_widget('treeview1')
      self.barra =jpg.get_widget('progressbar2')
      self.cnc = jpg.get_widget('combobox2')
      self.claa = jpg.get_widget('entry13')



      jpg.signal_autoconnect(self)
      self.japrod.show_all()
      if int(conteudo) == 1 :
         btnewprod.set_sensitive(True)
      gtk.main()

      coa = open('consulta.t','r')
      co = coa.read()
      if co == "1":
         print "operando no servidor secundario somente consulta"
         self.btedit.set_sensitive(False)
         self.btatual.set_sensitive(False)
         self.bgrava.set_sensitive(False)
   

   def ncmudou(self,widget): 
       at = self.cnc.get_active()
       af =  float(at)/ 10 
       self.barra.set_fraction(af)
       
       

   def showjp (self,widget):
      self.exibeproduto("1")
 
   def progress_bar(self,value, max, barsize):
      chars = int(value * barsize / float(max))
      percent = int((value / float(max)) * 100)
      sys.stdout.write("#" * chars)
      sys.stdout.write(" " * (barsize - chars + 2))
      if value >= max:
         sys.stdout.write("Concluido. \n\n")
      else:
         sys.stdout.write("[%3i%%]\r" % (percent))
         sys.stdout.flush()
   def mostrarmov(self,widget):
      ncolunas = self.tabelamov.get_columns()
      for col in ncolunas:
         self.tabelamov.remove_column(col)  


      self.modelo = gtk.ListStore(
            gobject.TYPE_UINT,
            gobject.TYPE_STRING,
            gobject.TYPE_STRING,
            gobject.TYPE_STRING,
            gobject.TYPE_STRING, 
            gobject.TYPE_STRING,
            gobject.TYPE_STRING,gobject.TYPE_STRING,gobject.TYPE_STRING,gobject.TYPE_STRING)
      ##self.modelo = gtk.TreeStore(str,str,str,str,str,str)
      self.tabelamov.set_model(self.modelo)
      self.tabelamov.append_column(gtk.TreeViewColumn("cod mov",gtk.CellRendererText(), text=0))
      self.tabelamov.append_column(gtk.TreeViewColumn("data",gtk.CellRendererText(), text=1))
      self.tabelamov.append_column(gtk.TreeViewColumn("n i",gtk.CellRendererText(), text=2))
      self.tabelamov.append_column(gtk.TreeViewColumn("movimento",gtk.CellRendererText(), text=3))
      self.tabelamov.append_column(gtk.TreeViewColumn("qtd",gtk.CellRendererText(), text=4))
      self.tabelamov.append_column(gtk.TreeViewColumn("grade",gtk.CellRendererText(), text=5))
      codp = self.edcodp.get_text()
      selpvendidos=con.cursor()
      selpvendidos.execute("SELECT * FROM tb_mov_merc WHERE cod_prod='"+codp+"' ORDER BY i DESC")
      pvend = selpvendidos.fetchall()
      for pdv in pvend :
         fundo = None
         cor =None
         corpr = None
         selmov =con.cursor()
         codmov  = str(pdv[9])
         selmov.execute("SELECT * FROM t_mov WHERE cit='"+codmov+"'")
         lin = selmov.fetchone()
         demov = str(lin[1])

         self.modelo.append([pdv[0],pdv[11],pdv[1],demov,pdv[3],pdv[8],'',cor,fundo,corpr])


     




   def atualizar(self,widget):
      self.btfind.set_sensitive(False)
      nvcv= con.cursor()
      #data= self.dataget()
      nw=datetime.now()
      no=str(nw)
      nn = no[11:]
      nnn = nn[:8]
      #dat = str(data)+ " " + nnn    
      now=no[:19]
      nvcv.execute("INSERT INTO tb_cv (cv,data,vend,vtc,vtv,dpg,aux,n_not_ext,now,cod_mov,v_des,cod_cli) VALUES (NULL,'"+str(now)+"','0','0','0','0','0','0','"+str(now)+"','666','0','1')")  
      nuv =  int(con.insert_id())
      con.commit()
      self.nuv = str(nuv)
      #usar o nuv como numero do movimento

      lprod=con.cursor()
      lprod.execute("SELECT * FROM ESTOQUE ")
      npe = int(lprod.rowcount)
      npe = npe * 2 
      pvend = lprod.fetchall()
      it =0
      print "processando..."
      for pdv in pvend:
         it +=1

         cod = pdv[0]
         codb = pdv[1]
         desc = pdv[2]
         grupo  = pdv[3]
         forne = pdv[4]
         und = pdv[6]
         pre = pdv[7]
         ind = pdv[8]
         cc = pdv[9]
         qtd = pdv[12]
         cf = pdv[19]
         ipi = pdv[20]
         cst = pdv[21]
         st = pdv[22] 
         
         pcbp=con.cursor()
         pcbp.execute("SELECT * FROM pbestoreal WHERE codigo='"+cod+"'")
         npcbe=int(pcbp.rowcount)
         if npcbe == 1:
            linpc = pcbp.fetchone()
            qtde = linpc[7]
            nc = linpc[13]
            
            if qtd < qtde :
               inspv = con.cursor()
               dqtd = qtd - qtde 
               stv = float(dqtd) * float(pre)
               stc = float(dqtd) * float(cc)
               
               #ncf = int(nc)-10
               inspv.execute("INSERT INTO tb_mov_merc (i,n_not_int,cod_prod,qtd_prod,pc_u,pv_u,pc_s,pv_s,grade_sel,cod_mov,n_not_ext,data_sel,data_real,operador,p_des,v_des) VALUES (NULL,'"+self.nuv+"','"+str(cod)+"','"+str(dqtd)+"','"+str(cc)+"','"+str(pre)+"','"+str(stc)+"','"+str(stv)+"','','111','0','"+str(now)+"','"+str(now)+"','0','0','0') ")

               # saida auto estoque 
            else :
               if qtd > qtde :
                 # entrada auto  estoque 
                 # print "maior:"
                  inspv = con.cursor()
                  dqtd = qtd - qtde 
                  stv = float(dqtd) * float(pre)
                  stc = float(dqtd) * float(cc)
                  
                  #ncf = int(nc)-10
                  inspv.execute("INSERT INTO tb_mov_merc (i,n_not_int,cod_prod,qtd_prod,pc_u,pv_u,pc_s,pv_s,grade_sel,cod_mov,n_not_ext,data_sel,data_real,operador,p_des,v_des) VALUES (NULL,'"+self.nuv+"','"+str(cod)+"','"+str(dqtd)+"','"+str(cc)+"','"+str(pre)+"','"+str(stc)+"','"+str(stv)+"','','171','0','"+str(now)+"','"+str(now)+"','0','0','0') ")
              
               else :
                   ncf = int(nc) 
                     #atualizar estoque 
                     # print "."+cod
            #update tb pbestoreal
            gaprod = con.cursor()
            gaprod.execute("UPDATE pbestoreal SET codbarras='"+str(codb)+"',descricaop='"+str(desc)+"',fornecedorp='"+str(forne)+"',undp='"+str(und)+"',qtdautalest='"+str(qtd)+"',precov='"+str(pre)+"',custoc='"+ str(cc)+"',nc='"+str(ncf)+"',class='" +str(grupo)+"' WHERE codigo='"+str(cod)+"'")
            it +=1

         else:
            issp= con.cursor()
            issp.execute("INSERT INTO pbestoreal(`codigo` ,`codbarras` ,`descricaop` ,`fornecedorp` ,`undp` ,`precov` ,`custoc` ,`qtdautalest` ,`qestlj1` ,`qestl2` ,`qestlj3` ,`qmin` ,`creal` ,`nc` ,`grade` ,`class`)VALUES ('"+str(cod)+"', '"+str(codb)+"', '"+str(desc)+"', '"+str(forne)+"', '"+str(und)+"', '"+str(pre)+"', '"+str(cc)+"', '"+str(qtd)+"', '0.00', '0.00', '0.00', '0','"+str(cc)+"', '50', '', '" +str(grupo)+"');")
            ##inserir no mov tb ...
            it +=1
            inspv = con.cursor()
            stv = float(dqtd) * float(pre)
            stc = float(dqtd) * float(cc)
            inspv.execute("INSERT INTO tb_mov_merc (i,n_not_int,cod_prod,qtd_prod,pc_u,pv_u,pc_s,pv_s,grade_sel,cod_mov,n_not_ext,data_sel,data_real,operador,p_des,v_des) VALUES (NULL,'"+self.nuv+"','"+str(cod)+"','"+str(qtd)+"','"+str(cc)+"','"+str(pre)+"','"+str(stc)+"','"+str(stv)+"','','1','0','"+now+"','"+now+"','0','0','0') ")
         self.progress_bar(it, npe, 60 )
      dell = con.cursor()
      dell.execute("TRUNCATE TABLE ESTOQUE")
      self.btfind.set_sensitive(True)
      self.btatual.set_sensitive(False)
      


   def atnt(self,widget):
      let=cnn.cursor()
      let.execute("SELECT * FROM ESTOQUE ")
      pvend = let.fetchall()
      for pdv in pvend:
         

         cod = pdv[0]
         codb = pdv[1]
         desc = pdv[2]
         grupo  = pdv[3]
         forne = pdv[4]
         und = pdv[6]
         pre = pdv[7]
         ind = pdv[8]
         cc = pdv[9]
         qtd = pdv[12]
         cf = pdv[19]
         ipi = pdv[20]
         cst = pdv[21]
         st = pdv[22] 
       
         pcbp=con.cursor()
         pcbp.execute("SELECT * FROM pbestoreal WHERE codigo='"+cod+"'")
         npcbe=int(pcbp.rowcount)
         if npcbe == 1:
            
            self.btfind.set_sensitive(False)
         else:
            issp= con.cursor()
            issp.execute("INSERT INTO pbestoreal(`codigo` ,`codbarras` ,`descricaop` ,`fornecedorp` ,`undp` ,`precov` ,`custoc` ,`qtdautalest` ,`qestlj1` ,`qestl2` ,`qestlj3` ,`qmin` ,`creal` ,`nc` ,`grade` ,`class`)VALUES ('"+str(cod)+"', '"+str(codb)+"', '"+str(desc)+"', '"+str(forne)+"', '"+str(und)+"', '"+str(pre)+"', '"+str(cc)+"', '0.0', '0.00', '0.00', '0.00', '0','"+str(cc)+"', '100', '', '" +str(grupo)+"');")
            ##inserir no mov tb ...
            
      sys.stdout.write(".")
      lnt=cnn.cursor()
      lnt.execute("SELECT * FROM COMPRAS WHERE `OPERACAO` LIKE 'Compra para comercialização' OR `OPERACAO` LIKE 'compra p/ com. de mercadoria ST' ")
      pcom = lnt.fetchall()
      for pco in pcom:
         nnf = pco[0]
         fo  = pco[4] 
         de = pco[6]
         tt = pco[25]
         fnt=con.cursor()
         fnt.execute("SELECT * FROM notasentrada WHERE `NUMERONF` LIKE '"+nnf+"'AND `FORNECEDOR` LIKE '"+fo+"'AND EMISSAO = '"+str(de)+"' AND  `OPERACAO` LIKE 'Compra para comercialização' ")
         nlfnt=int(fnt.rowcount)
         if nlfnt ==1 : 
            #l=fnt.fetchone()
            self.btfind.set_sensitive(False)


         else :
            print nnf 
            nvcv= con.cursor()
            #data= self.dataget()
            nw=datetime.now()
            no=str(nw)
            nn = no[11:]
            nnn = nn[:8]
            #dat = str(data)+ " " + nnn    
            now=no[:19]
            nvcv.execute("INSERT INTO tb_cv (cv,data,vend,vtc,vtv,dpg,aux,n_not_ext,now,cod_mov,v_des,cod_cli) VALUES (NULL,'"+str(now)+"','0','"+str(tt)+"','0','0','0','0','"+str(now)+"','777','0','1')")  
            nuv =  int(con.insert_id())
            con.commit()
            self.nuv = str(nuv)            




            itnt=cnn.cursor()
            itnt.execute("SELECT *FROM `ITENS002` WHERE `NUMERONF` LIKE '"+nnf+"' AND `FORNECEDOR` LIKE '"+fo+"' ")
            itntf = itnt.fetchall()
            
            for it in itntf: 
                 
                 ##print "---->"+it[2]+" X "+str(it[9])
                 cod = it[2]
                 qtd = it[9]
                 pcc = it[10]
                 ptc = it[11]
                 inspv = con.cursor()
                 inspv.execute("INSERT INTO tb_mov_merc (i,n_not_int,cod_prod,qtd_prod,pc_u,pv_u,pc_s,pv_s,grade_sel,cod_mov,n_not_ext,data_sel,data_real,operador,p_des,v_des) VALUES (NULL,'"+self.nuv+"','"+str(cod)+"','"+str(qtd)+"','"+str(pcc)+"','0','"+str(ptc)+"','0','','777','"+str(nnf)+"','"+str(now)+"','"+str(now)+"','0','0','0') ")
                 
                 pcbp=con.cursor()
                 pcbp.execute("SELECT * FROM pbestoreal WHERE codigo='"+cod+"'")
                 npcbe=int(pcbp.rowcount)
                 if npcbe == 1:
                    linpc = pcbp.fetchone()
                    qtde = linpc[7]
                    qtdr = linpc[8]
                 qtdf= qtde + qtd 
                 qtdrf= qtdr + qtd
                 gaprod = con.cursor()
                 gaprod.execute("UPDATE pbestoreal SET qtdautalest='"+str(qtdf)+"',qestlj1='"+str(qtdrf)+"',custoc='"+str(pcc)+"' WHERE codigo='"+str(cod)+"'")          
          
             
      icf=con.cursor()
      icf.execute("DROP TABLE IF EXISTS `tb_pb`.`notasentrada`;")
      icf.execute(" CREATE  TABLE  `tb_pb`.`notasentrada` (  `NUMERONF` varchar( 6  )  NOT  NULL , `SERIE` varchar( 3  )  NOT  NULL , `MODELO` varchar( 2  )  NOT  NULL , `VENDEDOR` varchar( 35  )  NOT  NULL , `FORNECEDOR` varchar( 60  )  NOT  NULL , `OPERACAO` varchar( 40  )  NOT  NULL , `EMISSAO` date NOT  NULL , `FRETE` double NOT  NULL , `SEGURO` double NOT  NULL , `DESPESAS` double NOT  NULL , `VOLUMES` double NOT  NULL , `ESPECIE` varchar( 13  )  NOT  NULL , `MARCA` varchar( 13  )  NOT  NULL , `TRANSPORTA` varchar( 60  )  NOT  NULL , `FRETE12` varchar( 1  )  NOT  NULL , `SAIDAH` varchar( 8  )  NOT  NULL , `SAIDAD` date NOT  NULL , `DUPLICATAS` double NOT  NULL , `BASEICM` double NOT  NULL , `ICMS` double NOT  NULL , `ICMSSUBSTI` double NOT  NULL , `BASESUBSTI` double NOT  NULL , `ALIQUOTA` double NOT  NULL , `ISS` double NOT  NULL , `IPI` double NOT  NULL , `TOTAL` double NOT  NULL , `MERCADORIA` double NOT  NULL , `COMPLEMEN1` varchar( 60  )  NOT  NULL , `COMPLEMEN2` varchar( 60  )  NOT  NULL , `COMPLEMEN3` varchar( 60  )  NOT  NULL , `COMPLEMEN4` varchar( 60  )  NOT  NULL , `EMITIDA` varchar( 1  )  NOT  NULL , `SERVICOS` double NOT  NULL , `DESCRICAO1` varchar( 100  )  NOT  NULL , `DESCRICAO2` varchar( 100  )  NOT  NULL , `DESCRICAO3` varchar( 100  )  NOT  NULL , `PESOBRUTO` double NOT  NULL , `PESOLIQUI` double NOT  NULL , `DESCPROD` double NOT  NULL , `CODIGOBASE` double NOT  NULL  ) ENGINE  =  MyISAM  DEFAULT CHARSET  = latin1;")
      icf.execute(" INSERT INTO `tb_pb`.`notasentrada` SELECT * FROM `dbfmy`.`COMPRAS` ;")
      icf2=con.cursor()
      
      icf2.execute("DROP TABLE IF EXISTS `tb_pb`.`itensntentrada`;")
      icf2.execute(" CREATE  TABLE  `tb_pb`.`itensntentrada` (  `NUMERONF` varchar( 6  )  NOT  NULL , `SERIE` varchar( 3  )  NOT  NULL , `CODIGO`varchar( 5  )  NOT  NULL , `DESCRICAO` varchar( 45  )  NOT  NULL , `ST` varchar( 3  )  NOT  NULL , `IPI` double NOT  NULL , `ICM` double NOT  NULL , `BASE` double NOT  NULL , `MEDIDA` varchar( 3  )  NOT  NULL , `QUANTIDADE` double NOT  NULL , `UNITARIO` double NOT  NULL , `TOTAL` double NOT  NULL , `LISTA` double NOT  NULL , `CUSTO` double NOT  NULL , `PESO` double NOT  NULL , `FORNECEDOR` varchar( 60  )  NOT  NULL , `CFOP` varchar( 5  ) NOT  NULL , `DESCONTO` double NOT  NULL , `CST` varchar( 3  )  NOT  NULL , `CSOSN` varchar( 3  )  NOT  NULL , `VL_FRETE` double NOT  NULL ,`VL_SEGURO` double NOT  NULL , `VL_DESPESA` double NOT  NULL , `ALQSTORIGE` double NOT  NULL , `ALQSTDEST` double NOT  NULL , `BC_ICMSST` double NOT  NULL ,`VL_BCST` double NOT  NULL , `MVA` double NOT  NULL , `VL_ICMSST` double NOT  NULL , `CST_IPI` varchar( 3  )  NOT  NULL , `CST_PIS` varchar( 3  )  NOT  NULL , `CST_COFINS` varchar( 3  )  NOT  NULL , `PIS` double NOT  NULL , `COFINS` double NOT  NULL , `BASEPIS` double NOT  NULL , `BASECOFINS` double NOT  NULL  ) ENGINE  =  MyISAM  DEFAULT CHARSET  = latin1;")
      icf2.execute(" INSERT INTO `tb_pb`.`itensntentrada` SELECT * FROM `dbfmy`.`ITENS002` ;")
      self.btfind.set_sensitive(True)
      print "atualizacao concluida !."
      sys.stdout.write(".")
      




   def bgravarprod_clicked (self,widget):
      gaprod=con.cursor()
      descp=self.eddescprod.get_text()
      codp=self.edcod.get_text()
      unp= self.edun.get_text()
      qtp= self.edqt.get_text()
      pvp= self.edpv.get_text()
      pcp= self.edpc.get_text()
      qtr = self.edqtrc.get_text()
      ii=  self.procproduto.get_text()
      nc = self.cnc.get_active()
      ncc = int(float(nc)*10)
      #print ncc

      gaprod.execute("UPDATE pbestoreal SET codbarras='"+str(codp)+"',descricaop='"+str(descp)+"',undp='"+str(unp)+"',qtdautalest='"+str(qtr)+"',qestlj1='"+str(qtp)+"',precov='"+str(pvp)+"',creal='"+str(pcp)+"',nc='"+str(int(ncc))+"' WHERE codigo='"+str(ii)+"'")
      

      self.btfind.set_sensitive(True)
      self.procproduto.set_sensitive(True)
      if int(conteudo) == 1 :
         self.btnewprod.set_sensitive(True)
      self.btedit.set_sensitive(True)
      self.edun.set_sensitive(False)
      self.eddescprod.set_sensitive(False)
      self.edcod.set_sensitive(False)
      self.edqt.set_sensitive(False)
      self.edpv.set_sensitive(False)
      self.edpc.set_sensitive(False)
      self.btedit.set_sensitive(True)
      self.btagrad.set_sensitive(False)
      self.btgrava.set_sensitive(False)
      self.btrc.set_sensitive(False)
      self.edqtrc.set_sensitive(False)
      self.edqgrad.set_sensitive(False)
      self.edtgrad.set_sensitive(False)
      self.btrec.set_sensitive(False)
      self.cnc.set_sensitive(False)
      self.barra.set_sensitive(False)

   def editc(self,widget):
      self.btfind.set_sensitive(False)
      self.procproduto.set_sensitive(False)
      self.btnewprod.set_sensitive(False)
      self.edun.set_sensitive(True)
      self.eddescprod.set_sensitive(True)
      self.edcod.set_sensitive(True)
      self.edqt.set_sensitive(True)
      self.edpv.set_sensitive(True)
      self.edpc.set_sensitive(True)
      self.btedit.set_sensitive(False) 
      self.btgrava.set_sensitive(True)
      self.btagrad.set_sensitive(True)
      self.btrc.set_sensitive(True)
      self.cnc.set_sensitive(True)
      self.barra.set_sensitive(True)
   
   def btrcclick(self,widget):
      self.edqtrc.set_sensitive(True)
      self.btrc.set_sensitive(False)

   def btaddgrad(self,widget):
      self.edtgrad.set_sensitive(True)
      self.edqgrad.set_sensitive(True)
      self.btrec.set_sensitive(True)
      self.edtgrad.grab_focus()
   
   def addgrad(self,widget):
      qtg= self.edqgrad.get_text()
      edtgd = self.edtgrad.get_text()
      if qtg > 0 and edtgd != "":
         igrd = con.cursor()
         igrd.execute("INSERT INTO tb_grad (`igrad`,`codprod`,`qta_grade`,`des_grade`)VALUES (NULL ,'"+str(self.codp)+"', '"+str(qtg)+"','"+str(edtgd)+"')")
         #print "gravando grade "
         self.edqgrad.set_text("1")
         self.edtgrad.set_text("")
         self.edqgrad.set_sensitive(False)
         self.edtgrad.set_sensitive(False)
         self.btrec.set_sensitive(False)
         self.btagrad.grab_focus()
         self.bgravarprod_clicked(self)
         #self.eddescprod.set_text(" ")
         #self.eddescprod.set_text(self.codp)
         self.exibegrade(str(1))
         self.exibegrade(str(self.codp))
      
   def newproduto (self,widget):

       luprod=con.cursor()
       luprod.execute("SELECT * FROM pbestoreal ORDER BY `codigo` DESC")
       lluprod = luprod.fetchone()
       #print str(lluprod[0])
       ult= int(lluprod[0])+1
       iprod = con.cursor()
       iprod.execute("INSERT INTO pbestoreal(`codigo` ,`codbarras` ,`descricaop` ,`fornecedorp` ,`undp` ,`precov` ,`custoc` ,`qtdautalest` ,`qestlj1` ,`qestl2` ,`qestlj3` ,`qmin` ,`creal` ,`nc` ,`grade` ,`class`)VALUES ('"+str(ult)+"', 'cod', 'descricao', '', 'und', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0','0.00', '', '', '');")
       lprod=con.cursor()
       strprocurado = str(ult)
       self.exibeproduto(strprocurado)

       self.btfind.set_sensitive(False)
       self.procproduto.set_text(str(ult))
       self.procproduto.set_sensitive(False)
       self.btnewprod.set_sensitive(False)
       self.editc("1")
       
       
   def exibeproduto (self,strp):
      
      lprod=con.cursor()
      strprocurado = strp
      lprod.execute("SELECT * FROM pbestoreal WHERE codbarras='"+strprocurado+"'")
      npe = int(lprod.rowcount)
      if npe ==1:
         
         llprod = lprod.fetchone()  
         self.eddescprod.set_text(str(llprod[2]))
         self.edcod.set_text(str(llprod[1]))
         self.edun.set_text(str(llprod[4]))
         self.edqt.set_text(str(llprod[8]))
         self.edpv.set_text(str(llprod[5]))
         self.edpc.set_text(str(llprod[12]))
         self.edqtrc.set_text(str(llprod[7]))
         self.edcrent.set_text(str(llprod[6]))
         self.edcodp.set_text(str(llprod[0]))
         self.claa.set_text(str(llprod[15]))
         f=float(str(llprod[13]))/ 100
         self.barra.set_fraction(f)
         self.codp = str(llprod[0])
         self.at= (int(llprod[13])/10) 
         self.cnc.set_active(self.at) 
      else: 
         lprod.execute("SELECT * FROM pbestoreal WHERE codigo='"+strprocurado+"'")
         npee = int(lprod.rowcount)
         if npee ==1:
                    llprod = lprod.fetchone()
     		    self.eddescprod.set_text(str(llprod[2]))
    		    self.edcod.set_text(str(llprod[1]))
    		    self.edun.set_text(str(llprod[4]))
  		    self.edqt.set_text(str(llprod[8]))
  		    self.edpv.set_text(str(llprod[5]))
  		    self.edpc.set_text(str(llprod[12]))
                    self.edqtrc.set_text(str(llprod[7]))
                    self.edcrent.set_text(str(llprod[6]))
                    self.edcodp.set_text(str(llprod[0]))
                    self.claa.set_text(str(llprod[15]))
                    f=float(str(llprod[13]))/ 100
                    self.barra.set_fraction(f)
                    self.codp = str(llprod[0])
                    self.at= (int(llprod[13])/10)
                    self.cnc.set_active(self.at) 
      self.exibegrade(str(self.codp))
      
     #print f
      coa = open('consulta.t','r')
      co = coa.read()
      if co == "1":
         
         self.btedit.set_sensitive(False)	
         self.btatual.set_sensitive(False)
         #self.bgrava.set_sensitive(False)



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
      ncolunas = self.tabelamov.get_columns()
      for col in ncolunas:
         self.tabelamov.remove_column(col) 
      if self.npg > 0: 
         ##self.bb
         #self.lgrade.set_sensitive(True)
         pgr = lgrad.fetchall()
         #self.edgrad.set_text(" ")
         
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
         #self.edgrad.set_text("--")
         #self.lgrade.set_sensitive(False)

   def fjaprod (self,widget,dados):
      if __name__ == "__main__":
             gtk.main_quit()
             exit(0)

   def pexibeproduto (self,strp):

    
      strp = self.procproduto.get_text()
      self.exibeproduto(strp)
      
if __name__ == "__main__":
   self.a = japroduto()

