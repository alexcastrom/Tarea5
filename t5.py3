import imaplib
import re

#datos
host = 'imap.gmail.com'
imap = imaplib.IMAP4_SSL(host)
############################################################################## PRIMER TXt
imap.login('alex.castro@mail.udp.cl', 'Pass')
imap.select('Inbox')
typ, data = imap.search(None,'FROM', 'noreply@uber.com') ###########messaje-id
count=0

arr=[]
for num in data[0].split():
	
	#if (count ==23 or count==4 or count==15 or count==24):
	#	count = count+1 
	#	continue
	typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (MESSAGE-ID)])')
	datito= data[0][1].decode()
	datito=datito.replace("Message-ID:", "")
	datito=datito.replace(">", "")
	datito=datito.replace("<", "")
	datito=datito.replace("Message-Id:", "")
	datito=datito.strip()
	print(datito)
	count=count+1
	arr.append(datito+"\n")
	print (count)
	if (count ==40):
		print("logrado")
		break


typ, data = imap.search(None,'FROM', 'info@correo.integramedica.cl')####MESSAge
count=0
for num in data[0].split():
	typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (MESSAGE-ID)])')
	datito= data[0][1].decode()
	datito=datito.replace("Message-ID:", "")
	datito=datito.replace(">", "")
	datito=datito.replace("<", "")
	datito=datito.replace("Message-Id:", "")
	datito=datito.strip()
	print(datito)
	arr.append(datito+"\n")
	count=count+1
	print (count)
	if (count ==40):
		print("logrado2")
		break

typ, data = imap.search(None,'FROM', 'start@engage.canva.com')######################### MESSAge
count=0
for num in data[0].split():
	typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (MESSAGE-ID)])')
	datito= data[0][1].decode()
	datito=datito.replace("Message-ID:", "")
	datito=datito.replace(">", "")
	datito=datito.replace("<", "")
	datito=datito.replace("Message-Id:", "")
	datito=datito.strip()
	print(datito)
	arr.append(datito+"\n")
	count=count+1
	print (count)
	if (count ==40):
		print("logrado2")
		break

imap.close()
host = 'imap.gmail.com'
imap = imaplib.IMAP4_SSL(host)

imap.login('cafeamargosinazucar@gmail.com', 'Pass')
imap.select('Inbox')

typ, data = imap.search(None,'FROM', 'comunicacion@cl.linio.com')######################### MESSAge
count=0
for num in data[0].split():
	typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (MESSAGE-ID)])')
	datito= data[0][1].decode()
	datito=datito.replace("Message-ID:", "")
	datito=datito.replace(">", "")
	datito=datito.replace("<", "")
	datito=datito.replace("Message-Id:", "")
	datito=datito.strip()
	print(datito)
	arr.append(datito+"\n")
	count=count+1
	print (count)
	if (count ==40):
		print("logrado2")
		break


typ, data = imap.search(None,'FROM', 'no-reply@twitch.tv')######################### MESSAge
count=0
for num in data[0].split():
	typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (MESSAGE-ID)])')
	datito= data[0][1].decode()
	datito=datito.replace("Message-ID:", "")
	datito=datito.replace(">", "")
	datito=datito.replace("<", "")
	datito=datito.replace("Message-Id:", "")
	datito=datito.strip()
	print(datito)
	arr.append(datito+"\n")
	count=count+1
	print (count)
	if (count ==40):
		print("logrado2")
		break


with open('mssid.txt', 'w') as file:
	file.writelines( arr )
imap.close()
############################################################################## SEGUNDO TXt


host = 'imap.gmail.com'
imap = imaplib.IMAP4_SSL(host)

imap.login('alex.castro@mail.udp.cl', 'Pass')
imap.select('Inbox')

typ, data = imap.search(None,'FROM', 'noreply@uber.com')########### PRIMER RECEIVER
count=0

arr=[]

cc=0
for num in data[0].split():
	cc=cc+1
	print(cc)
	#if (count ==23 or count==4 or count==15 or count==24):
	#	count = count+1 
	#	continue
	typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (Received)])')
	datito= data[0][1].decode()
	datito=datito.replace("Message-ID:", "")
	datito=datito.replace(">", "")
	datito=datito.replace("<", "")
	datito=datito.strip()
	datito = datito.split("\nR")
	i=len(datito)
	#if (i==3):
	#	continue
	datito[i-1]=datito[i-1].replace("eceived: ", "")
	datito[i-1]=datito[i-1].replace('\r', '').replace('\n', '')
	print(datito[i-1])
	arr.append(datito[i-1]+"\n")
	count=count+1
	#print (count)
	if (count ==40):
		print("logrado")
		break



typ, data = imap.search(None,'FROM', 'info@correo.integramedica.cl')  ##############   primer receiver
count=0
for num in data[0].split():
	typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (Received)])')
	datito= data[0][1].decode()
	datito=datito.replace("Message-ID:", "")
	datito=datito.replace(">", "")
	datito=datito.replace("<", "")
	datito=datito.replace("Message-Id:", "")
	datito=datito.strip()
	datito = datito.split("\nR")
	i=len(datito)
	if (i==3):
		continue
	datito[i-1]=datito[i-1].replace("eceived: ", "")
	datito[i-1]=datito[i-1].replace('\r', '').replace('\n', '')
	print(datito[i-1])
	arr.append(datito[i-1]+"\n")
	count=count+1
	print (count)
	if (count ==40):
		print("logrado")
		break

typ, data = imap.search(None,'FROM', 'start@engage.canva.com')  ##############   primer receiver
count=0
for num in data[0].split():
	typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (Received)])')
	datito= data[0][1].decode()
	datito=datito.replace("Message-ID:", "")
	datito=datito.replace(">", "")
	datito=datito.replace("<", "")
	datito=datito.replace("Message-Id:", "")
	datito=datito.strip()
	datito = datito.split("\nR")
	i=len(datito)
	datito[i-1]=datito[i-1].replace("eceived: ", "")
	datito[i-1]=datito[i-1].replace('\r', '').replace('\n', '')
	print(datito[i-1])
	arr.append(datito[i-1]+"\n")
	count=count+1
	print (count)
	if (count ==40):
		print("logrado")
		break

imap.close()

host = 'imap.gmail.com'
imap = imaplib.IMAP4_SSL(host)

imap.login('cafeamargosinazucar@gmail.com', 'Pass')
imap.select('Inbox')

typ, data = imap.search(None,'FROM', 'comunicacion@cl.linio.com')  ##############   primer receiver
count=0
for num in data[0].split():
	typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (Received)])')
	datito= data[0][1].decode()
	datito=datito.replace("Message-ID:", "")
	datito=datito.replace(">", "")
	datito=datito.replace("<", "")
	datito=datito.replace("Message-Id:", "")
	datito=datito.strip()
	datito = datito.split("\nR")
	i=len(datito)
	datito[i-1]=datito[i-1].replace("eceived: ", "")
	datito[i-1]=datito[i-1].replace('\r', '').replace('\n', '')
	print(datito[i-1])
	arr.append(datito[i-1]+"\n")
	count=count+1
	print (count)
	if (count ==40):
		print("logrado")
		break

typ, data = imap.search(None,'FROM', 'no-reply@twitch.tv')  ##############   primer receiver
count=0
for num in data[0].split():
	typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (Received)])')
	datito= data[0][1].decode()
	datito=datito.replace("Message-ID:", "")
	datito=datito.replace(">", "")
	datito=datito.replace("<", "")
	datito=datito.replace("Message-Id:", "")
	datito=datito.strip()
	datito = datito.split("\nR")
	i=len(datito)
	datito[i-1]=datito[i-1].replace("eceived: ", "")
	datito[i-1]=datito[i-1].replace('\r', '').replace('\n', '')
	print(datito[i-1])
	arr.append(datito[i-1]+"\n")
	count=count+1
	print (count)
	if (count ==40):
		print("logrado")
		break

with open('1rec.txt', 'w') as file:
	file.writelines( arr )
imap.close()
############################################################################## TERCER TXt


host = 'imap.gmail.com'
imap = imaplib.IMAP4_SSL(host)

imap.login('alex.castro@mail.udp.cl', 'Pass')
imap.select('Inbox')
arr=[]
typ, data = imap.search(None,'FROM', 'noreply@uber.com') ######## ULTIMO RECEIVER
count=0
for num in data[0].split():
	#if (count ==23 or count==4 or count==15 or count==24):
	#	count = count+1 
	#	continue
	typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (Received)])')
	datito= data[0][1].decode()
	datito=datito.replace("Message-ID:", "")
	datito=datito.replace(">", "")
	datito=datito.replace("<", "")
	datito=datito.replace("Message-Id:", "")
	datito=datito.strip()
	datito = datito.split("\nR")
	datito[0]=datito[0].replace("Received: ", "")
	datito[0]=datito[0].replace('\r', '').replace('\n', '')
	print(datito[0])
	arr.append(datito[0]+"\n")
	count=count+1
	print (count)
	if (count ==40):
		print("logrado")
		break


typ, data = imap.search(None,'FROM', 'info@correo.integramedica.cl')
count=0
for num in data[0].split():
	typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (Received)])') ##################### Last Receiver
	datito= data[0][1].decode()
	datito=datito.replace("Message-ID:", "")
	datito=datito.replace(">", "")
	datito=datito.replace("<", "")
	datito=datito.replace("Message-Id:", "")
	datito=datito.strip()
	datito = datito.split("\nR")
	
	datito[0]=datito[0].replace("Received: ", "")
	datito[0]=datito[0].replace('\r', '').replace('\n', '')
	print(datito[0])
	arr.append(datito[0]+"\n")
	count=count+1
	print (count)
	if (count ==40):
		print("logrado")
		break


typ, data = imap.search(None,'FROM', 'start@engage.canva.com')
count=0
for num in data[0].split():
	typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (Received)])') ##################### Last Receiver
	datito= data[0][1].decode()
	datito=datito.replace("Message-ID:", "")
	datito=datito.replace(">", "")
	datito=datito.replace("<", "")
	datito=datito.replace("Message-Id:", "")
	datito=datito.strip()
	datito = datito.split("\nR")
	datito[0]=datito[0].replace("Received: ", "")
	datito[0]=datito[0].replace('\r', '').replace('\n', '')
	print(datito[0])
	arr.append(datito[0]+"\n")
	count=count+1
	print (count)
	if (count ==40):
		print("logrado")
		break


imap.close()

host = 'imap.gmail.com'
imap = imaplib.IMAP4_SSL(host)

imap.login('cafeamargosinazucar@gmail.com', 'Pass')
imap.select('Inbox')

typ, data = imap.search(None,'FROM', 'comunicacion@cl.linio.com')
count=0
for num in data[0].split():
	typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (Received)])') ##################### Last Receiver
	datito= data[0][1].decode()
	datito=datito.replace("Message-ID:", "")
	datito=datito.replace(">", "")
	datito=datito.replace("<", "")
	datito=datito.replace("Message-Id:", "")
	datito=datito.strip()
	datito = datito.split("\nR")
	datito[0]=datito[0].replace("Received: ", "")
	datito[0]=datito[0].replace('\r', '').replace('\n', '')
	print(datito[0])
	arr.append(datito[0]+"\n")
	count=count+1
	print (count)
	if (count ==40):
		print("logrado")
		break



typ, data = imap.search(None,'FROM', 'no-reply@twitch.tv')
count=0
for num in data[0].split():
	typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (Received)])') ##################### Last Receiver
	datito= data[0][1].decode()
	datito=datito.replace("Message-ID:", "")
	datito=datito.replace(">", "")
	datito=datito.replace("<", "")
	datito=datito.replace("Message-Id:", "")
	datito=datito.strip()
	datito = datito.split("\nR")
	datito[0]=datito[0].replace("Received: ", "")
	datito[0]=datito[0].replace('\r', '').replace('\n', '')
	print(datito[0])
	arr.append(datito[0]+"\n")
	count=count+1
	print (count)
	if (count ==40):
		print("logrado")
		break

with open('lastrec.txt', 'w') as file:
	file.writelines( arr )
arr2=[]
for i in arr:
	ref=i.split(" ")[1]+"; "+i.split(" ")[5]
	arr2.append(ref+"\n")

with open('extralast.txt', 'w') as file:
	file.writelines( arr2 )
imap.close()

############################################################################## CUARTO TXT
host = 'imap.gmail.com'
imap = imaplib.IMAP4_SSL(host)

imap.login('alex.castro@mail.udp.cl', 'Pass')
imap.select('Inbox')
arr=[]

typ, data = imap.search(None,'FROM', 'noreply@uber.com')######################## FROM
count=0
for num in data[0].split():
	#if (count ==23 or count==4 or count==15 or count==24):
	#	count = count+1 
	#	continue
	typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (From)])')
	datito= data[0][1].decode()
	datito=datito.replace("Message-ID:", "")
	datito=datito.replace("Message-Id:", "")
	datito=datito.strip()
	datito=datito.replace("From: ", "")
	print(datito)
	arr.append(datito+"\n")
	count=count+1
	print (count)
	if (count ==40):
		print("logrado")
		break


typ, data = imap.search(None,'FROM', 'info@correo.integramedica.cl') #####################  FROM
count=0
for num in data[0].split():
	typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (From)])')
	datito= data[0][1].decode()
	datito=datito.replace("Message-ID:", "")
	datito=datito.replace("Message-Id:", "")
	datito=datito.strip()
	datito=datito.replace("From: ", "")
	print(datito)
	arr.append(datito+"\n")
	count=count+1
	print (count)
	if (count ==40):
		print("logrado")
		break


typ, data = imap.search(None,'FROM', 'start@engage.canva.com') #####################  FROM
count=0
for num in data[0].split():
	typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (From)])')
	datito= data[0][1].decode()
	datito=datito.replace("Message-ID:", "")
	datito=datito.replace("Message-Id:", "")
	datito=datito.strip()
	datito=datito.replace("From: ", "")
	print(datito)
	arr.append(datito+"\n")
	count=count+1
	print (count)
	if (count ==40):
		print("logrado")
		break


imap.close()

host = 'imap.gmail.com'
imap = imaplib.IMAP4_SSL(host)

imap.login('cafeamargosinazucar@gmail.com', 'Pass')
imap.select('Inbox')

typ, data = imap.search(None,'FROM', 'comunicacion@cl.linio.com') #####################  FROM
count=0
for num in data[0].split():
	typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (From)])')
	datito= data[0][1].decode()
	datito=datito.replace("Message-ID:", "")
	datito=datito.replace("Message-Id:", "")
	datito=datito.strip()
	datito=datito.replace("From: ", "")
	print(datito)
	arr.append(datito+"\n")
	count=count+1
	print (count)
	if (count ==40):
		print("logrado")
		break


typ, data = imap.search(None,'FROM', 'no-reply@twitch.tv') #####################  FROM
count=0
for num in data[0].split():
	typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (From)])')
	datito= data[0][1].decode()
	datito=datito.replace("Message-ID:", "")
	datito=datito.replace("Message-Id:", "")
	datito=datito.strip()
	datito=datito.replace("From: ", "")
	print(datito)
	arr.append(datito+"\n")
	count=count+1
	print (count)
	if (count ==40):
		print("logrado")
		break


with open('from.txt', 'w') as file:
	file.writelines( arr )
imap.close()

############################################################################## QUINTO TXT
host = 'imap.gmail.com'
imap = imaplib.IMAP4_SSL(host)

imap.login('alex.castro@mail.udp.cl', 'Pass')
imap.select('Inbox')
arr=[]
typ, data = imap.search(None,'FROM', 'noreply@uber.com')   ########### CORREO
count=0
for num in data[0].split():
	#if (count ==23 or count==4 or count==15 or count==24):
	#	count = count+1 
	#	continue
	typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (From)])')
	datito= data[0][1].decode()
	datito=datito.replace(">", "")
	datito=datito.strip()
	datito = datito.split("<")

	print(datito[1])
	arr.append(datito[1]+"\n")
	count=count+1
	print (count)
	if (count ==40):
		print("logrado")
		break


typ, data = imap.search(None,'FROM', 'info@correo.integramedica.cl')  ########################3 CORREO
count=0
for num in data[0].split():
	typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (From)])')
	datito= data[0][1].decode()
	datito=datito.replace(">", "")
	datito=datito.strip()
	datito = datito.split("<")

	print(datito[1])
	arr.append(datito[1]+"\n")
	count=count+1
	print (count)
	if (count ==40):
		print("logrado")
		break


typ, data = imap.search(None,'FROM', 'start@engage.canva.com')  ########################3 CORREO
count=0
for num in data[0].split():
	typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (From)])')
	datito= data[0][1].decode()
	datito=datito.replace(">", "")
	datito=datito.strip()
	datito = datito.split("<")

	print(datito[1])
	arr.append(datito[1]+"\n")
	count=count+1
	print (count)
	if (count ==40):
		print("logrado")
		break


imap.close()

host = 'imap.gmail.com'
imap = imaplib.IMAP4_SSL(host)

imap.login('cafeamargosinazucar@gmail.com', 'Pass')
imap.select('Inbox')

typ, data = imap.search(None,'FROM', 'comunicacion@cl.linio.com')  ########################3 CORREO
count=0
for num in data[0].split():
	typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (From)])')
	datito= data[0][1].decode()
	datito=datito.replace(">", "")
	datito=datito.strip()
	datito = datito.split("<")

	print(datito[1])
	arr.append(datito[1]+"\n")
	count=count+1
	print (count)
	if (count ==40):
		print("logrado")
		break


typ, data = imap.search(None,'FROM', 'no-reply@twitch.tv')  ########################3 CORREO
count=0
for num in data[0].split():
	typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (From)])')
	datito= data[0][1].decode()
	datito=datito.replace(">", "")
	datito=datito.strip()
	datito = datito.split("<")

	print(datito[1])
	arr.append(datito[1]+"\n")
	count=count+1
	print (count)
	if (count ==40):
		print("logrado")
		break


with open('correo.txt', 'w') as file:
	file.writelines( arr )
imap.close()
######################################################################### TXT SEIS


host = 'imap.gmail.com'
imap = imaplib.IMAP4_SSL(host)

imap.login('alex.castro@mail.udp.cl', 'Pass')
imap.select('Inbox')
arr=[]
typ, data = imap.search(None,'FROM', 'noreply@uber.com')   
count=0

for num in data[0].split():
	#if (count ==23 or count==4 or count==15 or count==24):
	#	count = count+1 
	#	continue
	typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (Received)])')
	datito= data[0][1].decode()
	datito=datito.replace("Message-ID:", "")
	datito=datito.replace(">", "")
	datito=datito.replace("<", "")
	datito=datito.strip()
	datito = datito.split("\nR")
	i=len(datito)
	datito[i-1]=datito[i-1].replace("eceived: ", "")
	
	datito[i-1]=datito[i-1].replace('\r', '').replace('\n', '')
	time=datito[i-1].split(" ")
	ii=len(time)
	print(time[ii-2]+" "+time[ii-1])
	if(time[ii-1][0] != "("):
		arr.append(time[ii-1]+"\n")
		count=count+1
		if (count ==40):
			print("logrado")
			break
		continue
	arr.append(time[ii-2]+" "+time[ii-1]+"\n")
	count=count+1
	print (count)
	if (count ==40):
		print("logrado")
		break


typ, data = imap.search(None,'FROM', 'info@correo.integramedica.cl')  ##############   primer receiver
count=0
for num in data[0].split():
	typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (Received)])')
	datito= data[0][1].decode()
	datito=datito.replace("Message-ID:", "")
	datito=datito.replace(">", "")
	datito=datito.replace("<", "")
	datito=datito.replace("Message-Id:", "")
	datito=datito.strip()
	datito = datito.split("\nR")
	i=len(datito)
	datito[i-1]=datito[i-1].replace("eceived: ", "")
	datito[i-1]=datito[i-1].replace('\r', '').replace('\n', '')
	time=datito[i-1].split(" ")
	ii=len(time)
	print(time[ii-2]+" "+time[ii-1])
	if(time[ii-1][0] != "("):
		arr.append(time[ii-1]+"\n")
		count=count+1
		if (count ==40):
			print("logrado")
			break
		continue
	arr.append(time[ii-2]+" "+time[ii-1]+"\n")
	count=count+1
	print (count)
	if (count ==40):
		print("logrado")
		break


typ, data = imap.search(None,'FROM', 'start@engage.canva.com')  ##############   primer receiver
count=0
for num in data[0].split():
	typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (Received)])')
	datito= data[0][1].decode()
	datito=datito.replace("Message-ID:", "")
	datito=datito.replace(">", "")
	datito=datito.replace("<", "")
	datito=datito.replace("Message-Id:", "")
	datito=datito.strip()
	datito = datito.split("\nR")
	i=len(datito)
	datito[i-1]=datito[i-1].replace("eceived: ", "")
	datito[i-1]=datito[i-1].replace('\r', '').replace('\n', '')
	time=datito[i-1].split(" ")
	ii=len(time)
	print(time[ii-2]+" "+time[ii-1])
	if(time[ii-1][0] != "("):
		arr.append(time[ii-1]+"\n")
		count=count+1
		if (count ==40):
			print("logrado")
			break
		continue
	arr.append(time[ii-2]+" "+time[ii-1]+"\n")
	count=count+1
	print (count)
	if (count ==40):
		print("logrado")
		break

imap.close()

host = 'imap.gmail.com'
imap = imaplib.IMAP4_SSL(host)

imap.login('cafeamargosinazucar@gmail.com', 'Pass')
imap.select('Inbox')

typ, data = imap.search(None,'FROM', 'comunicacion@cl.linio.com')  ##############   primer receiver
count=0
for num in data[0].split():
	typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (Received)])')
	datito= data[0][1].decode()
	datito=datito.replace("Message-ID:", "")
	datito=datito.replace(">", "")
	datito=datito.replace("<", "")
	datito=datito.replace("Message-Id:", "")
	datito=datito.strip()
	datito = datito.split("\nR")
	i=len(datito)
	datito[i-1]=datito[i-1].replace("eceived: ", "")
	datito[i-1]=datito[i-1].replace('\r', '').replace('\n', '')
	time=datito[i-1].split(" ")
	ii=len(time)
	print(time[ii-3])
	arr.append(time[ii-3]+"\n")
	count=count+1
	print (count)
	if (count ==40):
		print("logrado")
		break

typ, data = imap.search(None,'FROM', 'no-reply@twitch.tv')  ##############   primer receiver
count=0
for num in data[0].split():
	typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (Received)])')
	datito= data[0][1].decode()
	datito=datito.replace("Message-ID:", "")
	datito=datito.replace(">", "")
	datito=datito.replace("<", "")
	datito=datito.replace("Message-Id:", "")
	datito=datito.strip()
	datito = datito.split("\nR")
	i=len(datito)
	datito[i-1]=datito[i-1].replace("eceived: ", "")
	datito[i-1]=datito[i-1].replace('\r', '').replace('\n', '')
	time=datito[i-1].split(" ")
	ii=len(time)
	print(time[ii-2]+" "+time[ii-1])
	if(time[ii-1][0] != "("):
		arr.append(time[ii-1]+"\n")
		count=count+1
		if (count ==40):
			print("logrado")
			break
		continue
	arr.append(time[ii-2]+" "+time[ii-1]+"\n")
	count=count+1
	print (count)
	if (count ==40):
		print("logrado")
		break

with open('time.txt', 'w') as file:
	file.writelines( arr )
imap.close()


################################################################ TXT EXTRA1
host = 'imap.gmail.com'
imap = imaplib.IMAP4_SSL(host)
arr=[]
imap.login('alex.castro@mail.udp.cl', 'Pass')
imap.select('Inbox')

typ, data = imap.search(None,'FROM', 'noreply@uber.com')########### PRIMER RECEIVER
count=0


lim=40
cc=0
for num in data[0].split():
	cc=cc+1
	print(cc)
	#if (count ==23 or count==4 or count==15 or count==24):
	#	lim=lim+1
	#	count = count+1 
	#	continue
	typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (Received)])')
	datito= data[0][1].decode()
	datito=datito.replace("Message-ID:", "")
	datito=datito.replace(">", "")
	datito=datito.replace("<", "")
	datito=datito.strip()
	datito = datito.split("\nR")
	i=len(datito)
	#if (i==3):
	#	count=count+1
	#	lim=lim+1
	#	continue
	datito[i-1]=datito[i-1].replace("eceived: ", "")
	datito[i-1]=datito[i-1].replace('\r', '').replace('\n', '')
	datito[i-1]=datito[i-1].replace("from localhost (", "")
	datito[i-1]=datito[i-1].replace(") by", "")
	datito[i-1]=datito[i-1].replace(" (SG) with ESMTP id", "")
	datito[i-1]=datito[i-1].replace(" for alex.castro@mail.udp.cl", "")
	tr = datito[i-1].split(";")
	tr2=tr[0].split(" ")
	dat = ""
	check=True
	for j in tr2:
		if check:
			check=False
			dat=dat+j
		else:
			dat=dat+" "+j
	if len(dat.split(" "))==4:
		dat=dat.split(" ")[0]+" "+dat.split(" ")[1]+"; "+dat.split(" ")[2]+"; "+dat.split(" ")[3]
	else:
		dat=dat.split(" ")[0]+"; "+dat.split(" ")[1]+"; "+dat.split(" ")[2]
	
	print(dat)
	arr.append(dat+"\n")
	count=count+1
	#print (count)
	if (count ==40):
		print("logrado")
		break


typ, data = imap.search(None,'FROM', 'info@correo.integramedica.cl')  ##############   primer receiver
count=0
for num in data[0].split():
	typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (Received)])')
	datito= data[0][1].decode()
	datito=datito.replace("Message-ID:", "")
	datito=datito.replace(">", "")
	datito=datito.replace("<", "")
	datito=datito.replace("Message-Id:", "")
	datito=datito.strip()
	datito = datito.split("\nR")
	i=len(datito)
	datito[i-1]=datito[i-1].replace("eceived: ", "")
	datito[i-1]=datito[i-1].replace('\r', '').replace('\n', '')
	tr= datito[i-1].replace("with UTF8SMTPS id ","")
	tr= tr.replace(") by","")
	tr= tr.replace("from ","")
	tr= tr.replace("(","")
	tr =tr.split(" for")
	tr2=tr[0].split(" ")
	f= tr2[0]+" "+tr2[2]+"; "+tr2[3]+"; "+tr2[4]
	print(f)
	arr.append(f+"\n")
	count=count+1
	print (count)
	if (count ==40):
		print("logrado")
		break


typ, data = imap.search(None,'FROM', 'start@engage.canva.com')  ##############   primer receiver
count=0
for num in data[0].split():
	typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (Received)])')
	datito= data[0][1].decode()
	datito=datito.replace("Message-ID:", "")
	datito=datito.replace(">", "")
	datito=datito.replace("<", "")
	datito=datito.replace("Message-Id:", "")
	datito=datito.strip()
	datito = datito.split("\nR")
	i=len(datito)
	datito[i-1]=datito[i-1].replace("eceived: ", "")
	datito[i-1]=datito[i-1].replace('\r', '').replace('\n', '')
	datito[i-1]=datito[i-1].replace("from NjA1NTYzMg (", "")
	datito[i-1]=datito[i-1].replace(") by", "")
	datito[i-1]=datito[i-1].replace(" (SG) with HTTP id", "")
	ref2=datito[i-1].split(" ")
	f=""
	if ref2[0]=="unknown":
		f=ref2[0]+"; "+ref2[1]+"; "+ref2[2]
	else:
		f=ref2[0]+" "+ref2[1]+"; "+ref2[2]+"; "+ref2[3]
	print(f)
	arr.append(f+"\n")
	count=count+1
	print (count)
	if (count ==40):
		print("logrado")
		break

imap.close()

host = 'imap.gmail.com'
imap = imaplib.IMAP4_SSL(host)

imap.login('cafeamargosinazucar@gmail.com', 'Pass')
imap.select('Inbox')

typ, data = imap.search(None,'FROM', 'comunicacion@cl.linio.com')  ##############   primer receiver
count=0
for num in data[0].split():
	typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (Received)])')
	datito= data[0][1].decode()
	datito=datito.replace("Message-ID:", "")
	datito=datito.replace(">", "")
	datito=datito.replace("<", "")
	datito=datito.replace("Message-Id:", "")
	datito=datito.strip()
	datito = datito.split("\nR")
	i=len(datito)
	datito[i-1]=datito[i-1].replace("eceived: ", "")
	datito[i-1]=datito[i-1].replace('\r', '').replace('\n', '')
	datito[i-1]=datito[i-1].replace("by ", "")
	datito[i-1]=datito[i-1].replace(" id", "")
	datito[i-1]=datito[i-1].replace(")", "")
	datito[i-1]=datito[i-1].replace("envelope-from bounce-", "")
	ref=datito[i-1].split(" (")
	f= ref[1]+"; "+ref[0].split(" ")[0]+"; "+ref[0].split(" ")[1]
	print(f)
	arr.append(f+"\n")
	count=count+1
	print (count)
	if (count ==40):
		print("logrado")
		break


typ, data = imap.search(None,'FROM', 'no-reply@twitch.tv')  ##############   primer receiver
count=0
for num in data[0].split():
	typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (Received)])')
	datito= data[0][1].decode()
	datito=datito.replace("Message-ID:", "")
	datito=datito.replace(">", "")
	datito=datito.replace("<", "")
	datito=datito.replace("Message-Id:", "")
	datito=datito.strip()
	datito = datito.split("\nR")
	i=len(datito)
	datito[i-1]=datito[i-1].replace("eceived: ", "")
	datito[i-1]=datito[i-1].replace('\r', '').replace('\n', '')
	datito[i-1]=datito[i-1].replace("from ", "")
	datito[i-1]=datito[i-1].replace(") by", "")
	datito[i-1]=datito[i-1].replace(" with ESMTPS id", "")
	ref=datito[i-1].split(" ")
	f=ref[0]+" "+ref[2]+"; "+ref[3]+"; "+ref[4]
	print(f)
	arr.append(f+"\n")
	count=count+1
	print (count)
	if (count ==40):
		print("logrado")
		break

with open('extrafisrt.txt', 'w') as file:
	file.writelines( arr )
imap.close()
