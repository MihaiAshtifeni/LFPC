"""import networkx as nx
import matplotlib.pyplot as plt
def add_vertex(v):
  global graph
  global vertices_number
  if v in graph:
    print("Vertex ", v, " already exists.")
  else:
    vertices_number = vertices_number + 1
    graph[v] = []
def add_edge(v1, v2, e):
  global graph
  # Check if vertex v1 is a valid vertex
  if v1 not in graph:
    print("Vertex ", v1, " does not exist.")
  # Check if vertex v2 is a valid vertex
  elif v2 not in graph:
    print("Vertex ", v2, " does not exist.")
  else:
    # Since this code is not restricted to a directed or 
    # an undirected graph, an edge between v1 v2 does not
    # imply that an edge exists between v2 and v1
    temp = [v2, e]
    graph[v1].append(temp)"""

def NAF_to_RG(AF,Q,T,F,R):
	RGsimbols = ["0"]*15
	ALFABET = ["S", "A", "B", "C", "D", "F", "E", "G", "H", "I", "J", "K", "L", "M", "N"]

	print(" Our Nondeterministical Finete Automate:",R)

	print(" Q = ",Q)

	print(" T = ",T)

	for i in range(len(Q)):
		RGsimbols[i] = ALFABET[int(Q[i][1])]    

	i = 0
	while(RGsimbols[i] != "0"):
		print(" q",i,"= {",RGsimbols[i],"}")
		i+=1

	print(" Start = {S}")
	print(" P = {")
	for i in range(len(R)):
		print("     ",RGsimbols[int(R[i][2])]," --> ", R[i][4], RGsimbols[int(R[i][8])])
		if R[i][2] == F[0][1]:
			print("     ",RGsimbols[int(R[i][2])]," -->  EMPTY", )

	print("     }")
	print("_______________________________________________________________")

def equal(A,B):
	if len(A) != len(B):
		return False
	for i in range(len(A)):
		if A[i] != B[i]:
			return False
	print("Uraa")
	return True

def NFA_to_DFA(R,F,T,Q):
	DFAtabel = [["","","",""]for x in range(len(R))]
	for i in range(len(R)):
		DFAtabel[i][0] = R[i][1:3]
		for j in range((len(T))):
			if T[j][0] == R[i][4]:
				DFAtabel[i][j+1] = R[i][7:9]
	Delete = []
	for x in range((len(DFAtabel)-1)):		
		for i in range((len(DFAtabel))):
			if x != i and equal(DFAtabel[x][0],DFAtabel[i][0]):
				if x < i :
					for m in range(len(T)):
						DFAtabel[x][m+1] += DFAtabel[i][m+1]
					Delete.append(i)
					print("Pentru a sterge",Delete)

	n = 0;
	for i in range(len(Delete)): #Stergem nodurile care se repeta
		del DFAtabel[int(Delete[i])-n]
		n +=1
	for i in range(len(DFAtabel)):  # cauram nodurile care sau format noi 
		for j in range(len(DFAtabel[i])):
			for x in range(len(Q)):
				if DFAtabel[i][j] != Q[x]:
					DFAtabel.insert((i+1), ["","","",""])
					L  = i+1
					break
			break
		break	
	for i in range(len(T)+1):
		DFAtabel[L][i] = DFAtabel[L-1][i]
		DFAtabel[L][i] += DFAtabel[L+1][i]


	print("        |   a   |   b   |   c   |")
	print("---------------------------------")
	for i in range(len(DFAtabel)): 
		print(" ",DFAtabel[i][0]," "*(4-len(DFAtabel[i][0])) ,"|"," "*(4-len(DFAtabel[i][1])) ,DFAtabel[i][1],"|",DFAtabel[i][2]," "*(4-len(DFAtabel[i][2])) ,"|",DFAtabel[i][3]," "*(4-len(DFAtabel[i][3])) ,"|")


AF= ['Q', 'T', 'P', 'q0', 'F']
Q = ['q0', 'q1', 'q2', 'q3']
T = ['a', 'b', 'c']   #T - element of tranzition
F = ['q2'] #F - final state
P = "(q0,a)=q0, (q0,a)=q1, (q1,c)=q1, (q1,b)=q2, (q2,b)=q3, (q3,a)=q1"
R = P.split(", ")
#NAF_to_RG(AF,Q,T,F,R)
NFA_to_DFA(R,F,T,Q)
	

