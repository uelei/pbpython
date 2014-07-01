#!/usr/bin/python
# -*- coding: utf-8 -*-
#Arquivo: condb.py

import MySQLdb

try:
   print "conectando ..."
   con = MySQLdb.connect(host="192.168.0.111",user="pudhi",passwd="uc3r2l",db="tb_pb",charset="utf8",use_unicode=True)
   cnn = MySQLdb.connect(host="192.168.0.111",user="pudhi",passwd="uc3r2l",db="dbfmy",charset="utf8",use_unicode=True)
   #con = MySQLdb.connect(host="192.168.1.111",user="pudhi",passwd="uc3r2l",db="bancotesteremoto",charset="utf8",use_unicode=True)
   #con = MySQLdb.connect(host="localhost",user="root",passwd="uc3r2l",db="pbvancotest",charset="utf8",use_unicode=True)
   co = open('consulta.t','w')
   co.write('0')
   co.close()
except:
   print "Erro ao conectar ao banco de dados servidor 1 "
   
   try:
      print "conectando servidor dois ..."
      # con = MySQLdb.connect(host="localhost",user="root",passwd="uc3r2l",db="tb_pb",charset="utf8",use_unicode=True)
      con = MySQLdb.connect(host="piubol.ath.cx",port = 3307,user="pudhi",passwd="uc3r2l",db="tb_pb",charset="utf8",use_unicode=True)
      #con = MySQLdb.connect(host="192.168.0.111",user="pudhi",passwd="uc3r2l",db="tb_pb",charset="utf8",use_unicode=True)
      co = open('consulta.t','w')
      co.write('1')      
      co.close()
      
      #con = MySQLdb.connect(host="localhost",user="root",passwd="uc3r2l",db="pbvancotest",charset="utf8",use_unicode=True)
   except:
      print "Erro ao conectar ao banco de dados "
      exit()
   else: 
      print "conectado ao servidor 2... OK"
      print "operando no servidor secundario somente consulta"
      #exit()
else: 
   print "conectado ... OK"


