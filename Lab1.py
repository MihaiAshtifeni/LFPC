NecessarySimbol = "S" 
def CheckGrama(simbol,index,gr):                 #Verifica gramatica pentru fiecare simbol in parte; simbol -este caracterul care vine; lenght - lungimea lungimea gramaticii ; index - locul unde se afla simbolul
	F = True
	A = False
	global NecessarySimbol
	for i in range(len(gr)):
		if simbol == gr[i][2]:
			if gr[i][0] == NecessarySimbol:
				NecessarySimbol = gr[i][3]
				return False		
	return True	
 
def ReadGrama(Grama,st):       
	gr = Grama.split("; ")
	for n in range(len(st)):
		if CheckGrama(st[n],n,gr):
			print("Cuvantul are un simbol gresit")
			return
	if NecessarySimbol == "*" :	
	    print("<",st,">","URAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA!")
	else:	
		print("<",st,">","Cuvantul sa terminat nu intrun Simbop terminal si nu este corect")													

Grama = "S_aP; S_bQ; P_bP; P_cP; P_dQ; P_e*; Q_eQ; Q_fQ; Q_a*"
String = "ace"
ReadGrama(Grama,String)
