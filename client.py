import xmlrpc.client
import datetime
class test:
  def __init__(self,date,nom,prenom):
      self.date=date
      self.prenom=prenom
      self.nom=nom
   
prenom=input("prenom: \n")
nom=input("nom: \n")
date=datetime.datetime.now().time()
donnee=test(date,nom,prenom)
print(donnee.date,donnee.nom,donnee.prenom)
proxy=xmlrpc.client.ServerProxy("http://192.168.56.102:6789/")
result=proxy.nbre(donnee)
print(f"result:{result}")
proxy=xmlrpc.client.ServerProxy("http://192.168.56.102:6789/")
result=proxy.nbre(donnee)
print(f"result:{result}")
