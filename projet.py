from random import getrandbits, randint, randrange, random, choice
import numpy.random as nprnd
from time import time
from math import log10, pow
import pickle
import os
import sys
import bisect
import itertools


#### calcul du temps d'exec###
#import cProfile
##import re
#import pstats






#TODO:
	# itertools et repro etc...
	# vérifier taille des fichiers enregistrés.
	
	## vérifier taux de reproduction des pathos et hotes.
	## sysargv pour le nom de fichier
	## recharger les pop enregistrées.





# structures:

	#population_hotes:
		#hote:
			#allele:
				#gene:
					#int()
	
	#population_patho:
		#espece:
			#patho:
				#pept:
					#int()









def execution():
	"""
	main function.
	"""
	
	
	##############################################
	# paramètres:
	##############################################
	
	### Nom de l'expérience:
	
	#ok=False
	
	#while not ok:
		#nom_expe=input("Nom de l'expérience?\n")
		#nom_fichier=nom_expe+".dat"
		#compris=False
		
		#while not compris:
			#new_dir=True
			#if nom_expe in os.listdir("/home/thomas/Documents/ecole/2013-2014/q2/projet/data/"):
				#test=input("Voulez-vous remplacer "+nom_expe+"? (y/n/quit)\n")
				
				#if test=="n":
					#compris=True
					
				#elif test=="y":
					#ok=True
					#compris=True
					#new_dir=False
					
				#elif test=="quit":
					#sys.exit("\nAu revoir!\n")
				
				#else:
					#print("Réponse non comprise.\n")
			
			#else:
				#compris=True
				#ok=True
				
		
	#nom_fichier=nom_expe+".dat"
	#if new_dir:
		#os.mkdir("/home/thomas/Documents/ecole/2013-2014/q2/projet/data/"+nom_expe)
	
	
	
	### hotes
	nh=sys.argv[1]
	ngenes=1
	alleles=2
	generation_hote=10000
	
	# fréquence de mutation des hotes
	FqMutHotes=0.00001
	


	### pathos
	nesppatho=50
	maxpathos=10
	npept=20
	generation_patho=10
	
	# fq mutation min pathos
	FqMutMinPathos=0.1
	
	# autres:
	def_fitness_patho=0.00001 # fitness par défaut des pathogènes. Pour éviter une division par 0.
	
	
	##############################################
	# Impression paramètres
	#("name",nom_fichier),
	parameter_list=[("nh",nh),("ngenes",ngenes),("alleles",alleles),("generation_hote",generation_hote),("FqMutHotes",FqMutHotes),("nesppatho",nesppatho),("maxpathos",maxpathos),("npept",npept),("generation_patho",generation_patho),("FqMutMinPathos",FqMutMinPathos),("def_fitness_patho",def_fitness_patho)]
	
	print("\n##############\n# Paramètres #\n##############\n")
	for param in parameter_list:
		print("#PARAM	",param[0],"=",param[1])#,sep="=")
	
	print("\n")
	#print("géné","	","n_genes","	","dt","	","homo","	","hété")
	
	
	
	
	
	
	############################################################################
	# initialisation:
	
	
	#iterations=nh*ngenes*alleles+nesppatho*maxpathos*npept
	init=time()
	
	# sauvegarde en print
	#liste_resultats=[parameter_list]	#initialisation liste resultats à liste de parametres.
	#fout=open("/home/thomas/Documents/ecole/2013-2014/q2/projet/data/"+nom_expe+"/"+nom_fichier,"wb")
	#pickle.dump(liste_resultats,fout)
	#fout.close()
	
	




	
	
	#taux mutation pathogènes
	log_FqMutMinPathos=log10(FqMutMinPathos)
	log_FqMutHotes=log10(FqMutHotes)
	ddifflog=(log_FqMutMinPathos-log_FqMutHotes)/(nesppatho-1)
	
	listelogs=[]
	
	for i in range(nesppatho):
		listelogs.append(pow(10,log_FqMutMinPathos-(i*ddifflog)))
	
	freqmutpathos=tuple(listelogs)
	
	
	
	
	
	##################################################
	# init Listes d'hotes
	
	
	#create_hosts(nh, alleles, ngenes,population_hotes)
	#Crée les nh hotes avec ngenes dans 2 alleles. les gènes sont différents.
	string=getrandbits(16)
	
	population_hotes=[[[string for gene in range(ngenes)] for allele in range(alleles)] for hote in range(nh)]
	
	population_hotes_enfant=[[[] for allele in range(alleles)] for hote in range(nh)]
	
	
	
	
	
	########################################################################
	# init listes de pathogènes
	
	population_patho=[[[getrandbits(16) for peptide in range(npept)] for patho in range(maxpathos)] for espece in range(nesppatho)]
	
	population_patho_enfant=[[[str() for peptide in range(npept)] for patho in range(maxpathos)] for espece in range(nesppatho)]
	
	
	
	###############################################
	# init fitness et reproduction
	
	
	fitness_hotes=[0 for i in range(nh)]
	
	
	repro_pathos=[[0 for patho in range(maxpathos)] for espece in range(nesppatho)]
	
	
	sommes_fitness_especes_pathos=[0 for espece in range(nesppatho)]
	
	
	repro_hotes=[0 for hote in range(nh)]
	
	
	
	################################################################
	# Comparaison des bitstrings
	
	for gene_hote in range(generation_hote):
		
		hote_init=time()
		
		fitness_hotes=[0 for hote in range(nh)]
		
		for gene_patho in range(generation_patho):
			
			#print("génération patho:",gene_patho)
			fitness_pathos=[[[0 for i in range(3)] for patho in range(maxpathos)] for espece in range(nesppatho)]
			randlist=nprnd.randint(maxpathos, size=nesppatho*nh).tolist()
			
			for hote in range(nh):
				
				trouvés=0
				
				
				for espece in range(nesppatho):
					
					##########################
					#Pour un pathogène:
					patho=randlist.pop()
					#patho=randint(0,maxpathos-1)# plus lent que nprnd.randint...
					fitness_pathos[espece][patho][1]+=1
					fitness_patho=0
					trouve=False
					#try:
					for allele in population_hotes[hote]:
						
						for gene in allele:
							
							for pept in population_patho[espece][patho]:
								
								if '1111111' in bin(gene^pept):
									trouve=True
									trouvés+=1
									fitness_patho+=1
									break
							
							if trouve:
								break
						
						if trouve:
							break
					fitness_pathos[espece][patho][0]+=fitness_patho
				
				fitness_hotes[hote]+=trouvés
				
			
			
			##################################################
			# Fitness Pathogènes.
			#Calculé par espèce puisque la repro sera faite ainsi aussi. 
			
			
			for espece in range(nesppatho):
				
				sommes_fitness_especes_pathos[espece]=0	# somme de fitness d'une espece
				
				for patho in range(maxpathos):
					
					# évite les div par zéro
					try:
						#calcul fitness("presentation","rencontre","fitness")
						fitness_pathos[espece][patho][2]=(fitness_pathos[espece][patho][1]-fitness_pathos[espece][patho][0])/fitness_pathos[espece][patho][1]
						
						#calcul carré fitness
						fitness_pathos[espece][patho][2]*=fitness_pathos[espece][patho][2]

						sommes_fitness_especes_pathos[espece]+=fitness_pathos[espece][patho][2]
						
					except ZeroDivisionError:
						
						fitness_pathos[espece][patho][2]=def_fitness_patho
						
						#fitness_pathos[espece][patho][2]*=fitness_pathos[espece][patho][2]
						
						sommes_fitness_especes_pathos[espece]+=fitness_pathos[espece][patho][2]
						
				
			
			
			
			##############################################################
			# calcul du taux de reproduction des pathos dans chaque espece
			
			sommes_repro_especes_pathos=[]
			sommes_repro_especes_pathos_cum=[]
			
			for espece in range(nesppatho):
				
				sommes_repro_especes_pathos.append(0)
				sommes_repro_especes_pathos_cum.append([])
				
				for patho in range(maxpathos):
					
					try:
						repro_pathos[espece][patho]= fitness_pathos[espece][patho][2]/ sommes_fitness_especes_pathos[espece]
						
					except ZeroDivisionError:
						repro_pathos[espece][patho]=def_fitness_patho
						
					sommes_repro_especes_pathos[espece]+= repro_pathos[espece][patho]
					sommes_repro_especes_pathos_cum[espece].append(sommes_repro_especes_pathos[espece])
				
				sommes_repro_especes_pathos_cum[espece][maxpathos-1]=1.0
			
			
			
			
			
			
			
			###################################################################
			# reproduction pathos selon proba.
			
			
			for espece in range(nesppatho):#sommes_repro_especes_pathos_cum:
				
				
				
				for patho_enfant in range(maxpathos):
					
					rand_patho=random()
					
					for patho_parent in range(maxpathos):
						
						if rand_patho < sommes_repro_especes_pathos_cum[espece][patho_parent]:
							
							population_patho_enfant[espece][patho_enfant][:] = population_patho[espece][patho_parent][:]
							break
			
			
			# remplacement pop adulte par pop enfants.
			# changé [:]
			population_patho=[[[population_patho_enfant[espece][patho][peptide] for peptide in range(npept)] for patho in range(maxpathos)] for espece in range(nesppatho)]
			#population_patho_enfant=[[[str() for peptide in range(npept)] for patho in range(maxpathos)] for espece in range(nesppatho)]
			
			
			
			
			
			
			
			
			###################################################################
			# Mutations pathogènes
			# randlist pour aller plus vite
			
			randfloats=nprnd.ranf(nesppatho*maxpathos*npept).tolist()
			#print(len(randlist2))
			
			for espece in range(nesppatho):
				
				for patho in range(maxpathos):
					
					for pept in range(npept):
						
						if randfloats.pop()<=freqmutpathos[espece]:
						#if random()<=freqmutpathos[espece]:
							
							population_patho[espece][patho][pept]=getrandbits(16)
						
		
		
		###################################################################
		# fitness hotes
		
		fitness_tot_hotes=0
		
		for hote in range(nh):
			tot_rencontres=nesppatho*generation_patho
			fitness_hotes[hote]=fitness_hotes[hote]/tot_rencontres # calcul du fitness
			fitness_hotes[hote]*=fitness_hotes[hote]# au carré
			fitness_tot_hotes+=fitness_hotes[hote]# somme des carrés de fitness pour la pop
		#print(fitness_hotes)
			
			
			
			
			
		###################################################################
		# calcul taux de reproduction hotes.
		
		repro_hotes_tot=0
		
		repro_hotes_cum=[0 for hote in range(nh)]
		
		
		for hote in range(nh):
			
			repro_hotes[hote]=fitness_hotes[hote]/fitness_tot_hotes
			
			repro_hotes_tot+=repro_hotes[hote]
			#print(repro_hotes_tot)
			repro_hotes_cum[hote]=repro_hotes_tot
			#print(hote," ",repro_hotes[hote],repro_hotes_cum[hote])
		repro_hotes_cum[nh-1]=1.0
		#print(hote," ",repro_hotes[nh-1],repro_hotes_cum[nh-1])
		
		#print(repro_hotes)
		#print(repro_hotes_cum)
		
		for hote_enfant in range(nh):
			
			identiques = True
			
			while identiques:
				
				rand_parent1=random()
				rand_parent2=random()
				
				for hote_parent in range(nh):
					
					if rand_parent1 < repro_hotes_cum[hote_parent]:
						parent1=hote_parent
						break
				
				for hote_parent in range(nh):
					
					if rand_parent2 < repro_hotes_cum[hote_parent]:
						parent2=hote_parent
						break
				
				if parent1!=parent2:
					
					identiques=False
			
			choix_parent1=randint(0,alleles-1)
			
			choix_parent2=randint(0,alleles-1)
			
			population_hotes_enfant[hote_enfant] = [population_hotes[parent1][randint(0,alleles-1)][:], population_hotes[parent2][randint(0,alleles-1)][:]]
			# changé [:]
		
		population_hotes=[[population_hotes_enfant[hote][allele][:] for allele in range(alleles)] for hote in range(nh)]
		population_hotes_enfant=[[[] for allele in range(alleles)] for hote in range(nh)]
			
		#####################################################################
		# Mutations hotes
		# comptage genes
		
		
		
		randfloatshotes=nprnd.ranf(nh*alleles*ngenes).tolist()
		
		genes_pop_hotes=set()
		
		for hote in range(nh):
			
			for allele in range(alleles):
				
				for gene in range(ngenes):
					
					if randfloatshotes.pop()<=FqMutHotes:
					#if random()<=FqMutHotes:
						
						population_hotes[hote][allele][gene]=getrandbits(16)
					
					if population_hotes[hote][allele][gene] not in genes_pop_hotes:
						
						genes_pop_hotes.add(population_hotes[hote][allele][gene])
		
		
		
		
		
		
		
		
		#####################################################################
		# Homozygotes/hétérozygotes
		
		hétérozygotes=0
		homozygotes=0
		
		for hote in population_hotes:
			
			if hote[0]==hote[1]:
				
				homozygotes+=1
				
			else:
				
				hétérozygotes+=1
		
		
		
		
		
		
		
		########################################################################
		## Sauvegarde populations
		
		#liste_resultats=[]#nouvelle génération
		
		
		#############################################
		## sauvegarde des hotes
		#generation_a_sauver=len(liste_resultats)-1
		#liste_resultats.append(population_hotes)# on ajoute une liste de pop_hotes
		## changé [:]
		
		##for hote in range(nh):
			##liste_resultats[0].append([])
		
			##for allele in range(alleles):
				##liste_resultats[0][hote].append([])
				
				##for gene in range(ngenes):
					##liste_resultats[0][hote][allele]=population_hotes[hote][allele][:]
					###pop_hotes_to_save[hote][allele][gene]=population_hotes[hote][allele][gene]
		
		
		##############################################
		## sauvegarde des pathos 
		## changé [:]
		
		#liste_resultats.append(population_patho) # ajout d'une liste pop_pathos
		##for espece in range(nesppatho):
			##liste_resultats[1].append([])
			
			##for patho in range(maxpathos):
				##liste_resultats[1][espece].append([])
				##liste_resultats[1][espece][patho]=population_patho[espece][patho][:]
			
		##if gene_hote%10==0:
		##liste_resultats.append((pop_hotes_to_save,pop_pathos_to_save))
		#fout=open("/home/thomas/Documents/ecole/2013-2014/q2/projet/data/"+nom_expe+"/"+nom_fichier,"ab")
		#pickle.dump(liste_resultats,fout)
		#fout.close()
		
		#######################################################################
		# Sauvegarde populations en print
		
		
		
		
		
		
		#####################################################################
		# Infos génération hotes
		
		for hote in range(nh):
			print("# POP_HO",gene_hote,hote,population_hotes[hote])
		
		for espece in range(nesppatho):
			for patho in range(maxpathos):
				print("# POP_PA",gene_patho+(10*gene_hote),espece,patho,population_patho[espece][patho])
		
		hote_term=time()
		
		#diter=iterations-iterations_ancien
		#print("######### génération", gene_hote," #########\nt=",hote_term-hote_init,"s\n")#,trouvés,"trouvés\n",diter,"iterations/",iterations_max,"itérations max\n",int(diter/(hote_term-hote_init)),"itérations/s\n")
		
		#iterations_ancien=iterations
		
		#print("# GENER	","géné","	","n_genes","	","dt","	","homo","	","hété")
		print("# GENER	",gene_hote,"	", len(genes_pop_hotes),"	", round(hote_term-hote_init,2),"	",homozygotes,"	",hétérozygotes)
		#,"\n\n population:", genes_pop_hotes)
		
		
	####################################################################
	# Infos finales
	
	term=time()
	T=term-init
	print("")
	print(T,"s")
	print(generation_hote, "hôtes")
	print(T/generation_hote, "s/hôte")
	print(generation_hote/T, "hôte/s")
	print("")
	print(generation_patho*generation_hote, "pathos")
	print((generation_patho*generation_hote)/T, "géné pathos/s")
	print(T/(generation_patho*generation_hote), "s/patho")

	
	
	
	
	
	
	
	###################################
	# debug
	#print_fitness_hotes(fitness_hotes)
	#print_fitness_pathos(fitness_pathos)
	#print_repro_pathos(nesppatho, maxpathos, repro_pathos,sommes_repro_especes_pathos,population_patho,population_patho_enfant,sommes_repro_especes_pathos,sommes_repro_especes_pathos_cum)
	#print_pop_pathos_enfants(repro_pathos, population_patho_enfant)
	#print_test_pathos(repro_pathos, population_patho_enfant,test_pathos)#debug test random pathos
	#print(population_patho_enfant)
	#print_repro_hotes(repro_hotes)
	#print(liste_fitness_debug)
	#print("tot	", repro_hotes_tot)
	






#######################################################################
# execution
os.chdir("/home/thomas/Documents/ecole/2013-2014/q2/projet/")
if __name__ == "__main__":
	print("\n###################################\n# Bienvenue dans la matrice, néo. #\n###################################")
	execution()
	
	
#execution()








#### Calcul de l'efficacité et tps de calcul ###
#cProfile.run('execution()','stats')
#p = pstats.Stats('stats')
##p.strip_dirs().sort_stats(-1).print_stats()
##p.sort_stats('name')
##p.print_stats()
#p.sort_stats('cumulative').print_stats(20)
##print(p.get_sort_arg_defs())








######################################################################################################
# Poubelle




#def print_fitness_pathos(fitness_pathos):
	#""" Imprime le fitness des pathos en human readable
	#"""
	#print("Pathogènes")
	#for espece in fitness_pathos:
		#print (espece)
		#for patho in fitness_pathos[espece]:
			#print(patho,"	rencontres:", fitness_pathos[espece][patho]["rencontre"],"	presentations:", fitness_pathos[espece][patho][0],"	fitness:", fitness_pathos[espece][patho]["fitness"])



#def print_fitness_hotes(fitness_hotes):
	#"""Imprime le fitness des hotes en human readable
	#"""
	#print("hôtes")
	#for hote in fitness_hotes:
		#print(hote,"	fitness: ", fitness_hotes[hote])



#def print_repro_pathos(nesppatho, maxpathos, repro_pathos,sommes_repro_especes,population_patho,population_patho_enfant,sommes_repro_especes_pathos,sommes_repro_especes_pathos_cum):
	#"""Imprime la repro des pathos en human readable
	#"""
	#print("repro pathos")
	#for espece in range(nesppatho):
		#print (espece)
		#print("n°patho	repro	(patho_parent, patho_enft)	somme_repro	somme_repro_cum")
		#for patho in range(maxpathos):
			#print(patho,"	",repro_pathos[espece][patho],"	",sommes_repro_especes_pathos[espece],"	",sommes_repro_especes_pathos_cum[espece][patho])#,"	",population_patho_enfant[espece][patho][0:2])
		#print("\ntot	",sommes_repro_especes[espece])



#def print_pop_pathos_enfants(repro_pathos, population_patho_enfant):
	#print("pop pathos enfants")
	#for espece in population_patho_enfant:
		#print(espece)
		#print("enf	parents	repro_par")
		#for patho_enfant in population_patho_enfant[espece]:
			#print(patho_enfant,"	",population_patho_enfant[espece][patho_enfant][0],"	",repro_pathos[espece][population_patho_enfant[espece][patho_enfant][0]])

#def print_test_pathos(repro_pathos, population_patho, test_pathos):
	#"""debug test random pathos"""
	#print("pop pathos")
	#for espece in population_patho:
		#print(espece)
		#print("par	repro_par	prob-finale")
		#for patho_parent in population_patho[espece]:
			#print(patho_parent,"	",patho_parent,"	",repro_pathos[espece][patho_parent],"	",test_pathos[espece][patho_parent][1])


#def print_repro_hotes(repro_hotes):
	#"""Imprime la repro des hotes en human readable
	#"""
	#print("repro hotes")
	#for hote in repro_hotes:
		#print(hote,"	",repro_hotes[hote])

