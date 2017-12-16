
import random
import math

class Person: 
	def __init__(self, worldSize, healthStatus): 
		self.xposition=random.uniform(0,worldSize) 
		self.yposition=random.uniform(0,worldSize)
		self.healthStatus=healthStatus 

	def returnPosition(self):
		return (self.xposition, self.yposition) 

	def returnHealthStatus(self): 
		return self.healthStatus # 0=

	def updatePosition(self, newXPosition, newYPosition): 
		self.xposition=newXPosition 
		self.yposition=newYPosition 

	def updateHealthStatus(self, newHealthStatus): 
		self.healthStatus=newHealthStatus 



def main(): 
	numPeople=10;
	worldSize,stepSize=4,0.2  
	percentInitVaccinated, percentInitInfected=60,20 
	infectionRadius, pathogenicity, fatalityRate=0,0,0

	listPeople=createPeople(numPeople, percentInitVaccinated, percentInitInfected, worldSize)

	#print len(listPeople)
	#for item in listPeople: 
	#	print item.returnPosition()

	listSickPositions=getSickPositions(listPeople)

	#print listSickPositions
	
	while len(listSickPositions) != 0 : 
		listPeople=updatePositions(listPeople, stepSize)
		#print len(listPeople)
		#for item in listPeople: 
		#	print item.returnPosition()
		listPeople=updateIllnessStatus(listPeople, listSickPositions,infectionRadius,pathogenicity)
		#listSickPositions=getSickPosition(listPeople)
		

	#percentSurvive=tallyDamage(): 
	#	numHealthy/numVaccinated 

	#print percentSurvive 

def createPeople(numPeople, percentInitVaccinated, percentInitInfected, worldSize): 
	listPeople, numInitVaccinated, numInitInfected=[], int((percentInitVaccinated/100.0)*numPeople), int((percentInitInfected/100.0)*numPeople)
	for i in xrange(numPeople): 
		healthStatus=None
		if (i<numInitVaccinated):
			healthStatus=0
		if (numInitVaccinated <= i and i < numInitInfected+numInitVaccinated): 
			healthStatus=1 
		if(numInitInfected+numInitVaccinated <= i and i < numPeople): 
			healthStatus=2 

		person= Person(worldSize,healthStatus)	
		listPeople.append(person) 
	
	
	return listPeople 


def getSickPositions(listPeople): 
	listSickPositions=[]
	for person in listPeople: 
		if person.healthStatus==1: 
			listSickPositions.append((person.returnPosition()))
	return listSickPositions


def updatePositions(listPeople, stepSize): 
	newXPosition, newYPosition= None, None
	for person in listPeople: 
		while (newXPosition < 0 or newYPosition < 0): 
			bearing=random.uniform(0.0,2.0*math.pi)
			newXPosition=person.xposition + math.cos(bearing)*stepSize
			newYPosition=person.yposition + math.sin(bearing)*stepSize 
		person.updatePosition(newXPosition, newYPosition) 
		newXPosition, newYPosition= None, None
	return listPeople 

def updateIllnessStatus(listPeople,infectionRadius, pathogenicity): 
	for person in listPeople: 
		hasCompany=checkForCompany(person.returnPosition(),listSickPositions) 
		if hasCompany: 
			updateStatus 

	return listPeople



def checkForCompany(position,listPositions): 
	return null



main()
