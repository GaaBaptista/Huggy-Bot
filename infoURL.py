#!/usr/bin/env python
# -*- coding: utf-8 -*-


import requests
arquivo = open('URL.txt', 'w')

headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer c9eafb5a968c067976231d4baf5ca7bc'
}
r = requests.get('https://api.huggy.io/v2/contacts/contact_id', headers=headers) # https://api.huggy.io/v2/chats

response_body = r.text
x = response_body.split("{")
for i in x:
	z = 0
	ponto = 0
	while z < len(i) - 2:
		if(ponto == 1 and i[z] != "," and i[z] != "\""):
			arquivo.write(i[z])
		elif(i[z] == ","):
			ponto = 0
			arquivo.write(" ")
		elif(i[z] == ":"):
			ponto = 1
		z = z + 1
	if z != 0:
		arquivo.write("\n")

arquivo.close()