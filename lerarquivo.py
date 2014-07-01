#!/usr/bin/env python
arquivo = open("file.txt","r")
#print arquivo
#type(arquivo)
conteudo= arquivo.read()
arquivo.close()
print conteudo
