from biomodcacheux import *
# Partie 1 : code genetique
ADN1 = "TTGGTCAGAGCCTGGAAAAAATACTGGGTCACCTACAGCAGTGATGAAATGGTTGGGTTC"
print('Voici la repartition des différentes bases dans ADN1') 
print (freqADN(ADN1))
print('*'*53)
print('Le brin arn correspondant est')
arn1=ADN2arn(ADN1)
print(arn1)
print('*'*53)
print('La proteine générée codée par ce brin ADN')
prot=arn2prot(arn1)
print(prot)
#Partie 2 : Recherche de mutation
## Observez le code pour placer vos fichiers
print('*'*53)
print('Recherche des mutations sur le fichier chromomut.fna')
print('*'*53)
print(muta('chromo.fna','chromomut.fna'))
