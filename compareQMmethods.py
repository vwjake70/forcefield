import sys
import math
import numpy as np
import matplotlib.pyplot as plt



def atomNumber2ElementName(atom_number2):

	if atom_number2 == 1:
		element_name = "H"
	elif atom_number2 == 2:
		element_name = "He"
	elif atom_number2 == 6:
		element_name = "C"
	elif atom_number2 == 7:
		element_name = "N"
	elif atom_number2 == 8:
		element_name = "O"
	elif atom_number2 == 29:
		element_name = "Cu"
	return element_name


def atomNumber2ElementName(atom_number1):

	if atom_number1 == 1:
		element_name = "H"
	elif atom_number1 == 2:
		element_name = "He"
	elif atom_number1 == 6:
		element_name = "C"
	elif atom_number1 == 7:
		element_name = "N"
	elif atom_number1 == 8:
		element_name = "O"
	elif atom_number1 == 29:
		element_name = "Cu"

	return element_name


switch1 = 0
count1 = 0 
count2_1 = 0

#initial_parameters is used to identify where the "Scan" term is being found to help identify which oxygen is the one being used for the scan
initial_parameters1 = 0


#atom_number refers to the order of the atoms. Thus if copper is always the first atom, it has a atom_number of 1.
atom_number1 = []

#x, y, and z refer to the cartesian coordinate values for all of the atoms at each given frame
x1 = []
y1 = []
z1 = []
atom_name1 = []

#QM_energy is the energy quantum mechanically computed for a given frame 
QM_energy1 = []

#cu_o_bond_dist is the coordination distance between copper and the oxygen being incrementally moved closer to the copper
cu_o_bond_dist1 = []

coords1 = {}
#sys.argv[1] is the script extract.py
log_file1 = sys.argv[1]
with open(log_file1) as input:
	for line in input: 
		d=line.split()
		if len(d)>1:
			#finding the "Scan" term in the log file
			if d[0] == "!" and d[1] == "Initial" and d[2] == "Parameters":
				initial_parameters1 += 1
			#finding which R is assigned for the copper-oxygen bond distance
			if initial_parameters1 == 1:
				if d[0] == "!" and d[1] == "R1" and d[4] == "Scan":
					important_oxygen_name = d[1]
					important_oxygen_definition = d[2]
				elif d[0] == "!" and d[1] == "R2" and d[4] == "Scan":
					important_oxygen_name = d[1]
					important_oxygen_definition = d[2]
				elif d[0] == "!" and d[1] == "R3" and d[4] == "Scan":
					important_oxygen_name = d[1]
					important_oxygen_definition = d[2]
				elif d[0] == "!" and d[1] == "R4" and d[4] == "Scan":
					important_oxygen_name = d[1]
					important_oxygen_definition = d[2]
				elif d[0] == "!" and d[1] == "R5" and d[4] == "Scan":
					important_oxygen_name = d[1]
					important_oxygen_definition = d[2]
			if d[0] == "NAtoms=":
				n_atoms = int(d[1])
			if d[0]=="Optimization" and d[1]=="completed.": 
				switch1 += 1
			if switch1 == 1:
				if important_oxygen_name == d[1] and important_oxygen_definition == d[2]:
					#print d[3]
					cu_o_bond_dist1.append(float(d[3]))
				if d[0]=="SCF" and d[1]=="Done:" and d[2]=="E(UB3LYP)" and d[3]=="=":
					#print d[4]
					QM_energy1.append(float(d[4]) * 627.503) 
				if d[0]=="Standard" and d[1]=="orientation:":
					count1 += 1
				if count1==1:
					count2_1 += 1
					if count2_1 > 3 and count2_1 < n_atoms + 4:
					#	print d[0] 
						atom_number1.append(int(d[0]))
						atom_name1.append(atomNumber2ElementName(int(d[1])))
						x1.append(float(d[3]))
						y1.append(float(d[4]))
						z1.append(float(d[5]))
					if count2_1 == n_atoms + 70:
						switch1 = 0
						count1 = 0 
						count2_1 = 0


switch2 = 0
count2 = 0 
count2_2 = 0

#initial_parameters is used to identify where the "Scan" term is being found to help identify which oxygen is the one being used for the scan
initial_parameters2 = 0


#atom_number refers to the order of the atoms. Thus if copper is always the first atom, it has a atom_number of 1.
atom_number2 = []

#x, y, and z refer to the cartesian coordinate values for all of the atoms at each given frame
x2 = []
y2 = []
z2 = []
atom_name2 = []

#QM_energy is the energy quantum mechanically computed for a given frame 
QM_energy2 = []

#cu_o_bond_dist is the coordination distance between copper and the oxygen being incrementally moved closer to the copper
cu_o_bond_dist2 = []

coords2 = {}
#sys.argv[1] is the script extract.py
log_file2 = sys.argv[2]
with open(log_file2) as input:
	for line in input: 
		d=line.split()
		if len(d)>1:
			#finding the "Scan" term in the log file
			if d[0] == "!" and d[1] == "Initial" and d[2] == "Parameters":
				initial_parameters2 += 1
			#finding which R is assigned for the copper-oxygen bond distance
			if initial_parameters2 == 1:
				if d[0] == "!" and d[1] == "R1" and d[4] == "Scan":
					important_oxygen_name = d[1]
					important_oxygen_definition = d[2]
				elif d[0] == "!" and d[1] == "R2" and d[4] == "Scan":
					important_oxygen_name = d[1]
					important_oxygen_definition = d[2]
				elif d[0] == "!" and d[1] == "R3" and d[4] == "Scan":
					important_oxygen_name = d[1]
					important_oxygen_definition = d[2]
				elif d[0] == "!" and d[1] == "R4" and d[4] == "Scan":
					important_oxygen_name = d[1]
					important_oxygen_definition = d[2]
				elif d[0] == "!" and d[1] == "R5" and d[4] == "Scan":
					important_oxygen_name = d[1]
					important_oxygen_definition = d[2]
			if d[0] == "NAtoms=":
				n_atoms2 = int(d[1])
			if d[0]=="Optimization" and d[1]=="completed.": 
				switch2 += 1
			if switch2 == 1:
				if important_oxygen_name == d[1] and important_oxygen_definition == d[2]:
					#print d[3]
					cu_o_bond_dist2.append(float(d[3]))
				if d[0]=="SCF" and d[1]=="Done:" and d[2]=="E(UPBE1PBE)" and d[3]=="=":
					#print d[4]
					QM_energy2.append(float(d[4]) * 627.503) 
				if d[0]=="Standard" and d[1]=="orientation:":
					count2 += 1
				if count2==1:
					count2_2 += 1
					if count2_2 > 3 and count2_2 < n_atoms + 4:
					#	print d[0] 
						atom_number2.append(int(d[0]))
						atom_name2.append(atomNumber2ElementName(int(d[1])))
						x2.append(float(d[3]))
						y2.append(float(d[4]))
						z2.append(float(d[5]))
					if count2_2 == n_atoms + 70:
						switch2 = 0
						count2 = 0 
						count2_2 = 0







#zero out the first relative qm energy
first_element_in_qm_energy1 = QM_energy1[0]
for i in range(len(QM_energy1)):
	QM_energy1[i] -= first_element_in_qm_energy1
#zero out the second relative qm energy
first_element_in_qm_energy2 = QM_energy2[0]
for i in range(len(QM_energy2)):
	QM_energy2[i] -= first_element_in_qm_energy2
#print "QM1 = ", QM_energy1
#print "QM2 = ", QM_energy2
#print "1 = ", cu_o_bond_dist1
#print "2 = ", cu_o_bond_dist2

plt.grid(b=True, which='major', axis='both', color='#808080', linestyle='--')
plt.plot(cu_o_bond_dist1[1:25], QM_energy1[0:24], "g^")
plt.plot(cu_o_bond_dist2[1:24], QM_energy2[0:23], "b^")
plt.ylabel('Energy (kcal/mol)')
plt.xlabel('Copper-Oxygen Distance ($\AA$)')
plt.legend(['B3LYP','PBE1PBE'], fontsize='10', bbox_to_anchor=(.75, .9, 0.25, 0.0), loc=3, ncol=1, mode='expand', borderaxespad=0., numpoints = 1)
plt.xlim((0,4))
plt.axhline(y = 0, color = "k")
plt.title(r'Comparing B3LYP and PBE1PBE functionals of the 5-Water System', size='14')
#plt.suptitle(r'With Parameters from 1 Water System', size='14')
plt.show()







