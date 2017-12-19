
import random
import math

class Person: 
	def __init__(self, worldSize, healthStatus): 
		self.xposition=random.uniform(0,worldSize) 
		self.yposition=random.uniform(0,worldSize)
		self.healthStatus=healthStatus 
		self.infectionTime=0

	def returnPosition(self):
		return (self.xposition, self.yposition) 

	def returnHealthStatus(self): 
		return self.healthStatus # 0= Vaccinated, 1 = Infected, 2= Healthy, 3 = Immunized, 4= Dead 

	def returnInfectionTime(self): 
		return self.infectionTime

	def updatePosition(self, newXPosition, newYPosition): 
		self.xposition=newXPosition 
		self.yposition=newYPosition 

	def updateHealthStatus(self, newHealthStatus): 
		self.healthStatus=newHealthStatus 

	def updateInfectionTime(self): 
		self.infectionTime+=1



def main(numPeople, percentInitVaccinated,  percentInitInfected, pathogenicity, lengthIllness, fatalityRate): 
	worldSize=(1.0/3)*math.sqrt(numPeople)
	stepSize=0.05*worldSize 
	numInitUnVaccinated=int(((100-percentInitVaccinated)/100.0)*numPeople)
	infectionRadius=0.02*worldSize

	print "worldSize", worldSize 
	print "stepSize", stepSize
	print "infectionRadius", infectionRadius

	listPeople=createPeople(numPeople, percentInitVaccinated, percentInitInfected, worldSize)

	listSickPositions=getSickPositions(listPeople)

	
	while len(listSickPositions) != 0 : 
		listPeople=updatePositions(listPeople, stepSize)
		print "Num sick", len(listSickPositions)
		listPeople=updateIllnessStatus(listPeople, listSickPositions,infectionRadius,pathogenicity, lengthIllness, fatalityRate)
		listSickPositions=getSickPositions(listPeople)

		

	
	percentSurvive=tallyDamage(listPeople, numInitUnVaccinated)


	print "Percent Survive", percentSurvive 

	numDead=0 

	for person in listPeople: 
		if person.returnHealthStatus()==4: 
			numDead+=1 

	print "numDead", numDead

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
		if person.returnHealthStatus()==1: 
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

def updateIllnessStatus(listPeople, listSickPositions, infectionRadius, pathogenicity, lengthIllness, fatalityRate): 
	numberCompany=0
	for person in listPeople: 
		if person.returnHealthStatus()==2: 
			numberCompany=checkForCompany(person.returnPosition(),listSickPositions, infectionRadius) 
			for x in xrange(numberCompany): 
				if random.random()<pathogenicity: 
					person.updateHealthStatus(1)

		if person.returnHealthStatus()==1: 
			person.updateInfectionTime()
		if person.returnInfectionTime() > lengthIllness: 
			if(random.random() < fatalityRate): 
				person.updateHealthStatus(4)
			else: 
				person.updateHealthStatus(2)


	return listPeople



def checkForCompany(position,listSickPositions, infectionRadius): 
	numberCompany=0
	xpos,ypos= position[0],position[1]
	for sickPosition in listSickPositions: 
		distance=math.sqrt(math.pow(sickPosition[0]-xpos,2)+math.pow(ypos-sickPosition[1],2))
		if distance <= infectionRadius: 
			 numberCompany+=1
	return numberCompany


def tallyDamage(listPeople, numInitUnVaccinated): 
	numFinalHealthy=0.0 
	for person in listPeople: 
		if person.returnHealthStatus()==2: 
			numFinalHealthy+=1 

	return numFinalHealthy/numInitUnVaccinated


if __name__ == "__main__": 
	main(1000, 90, 1, 1, 6, .8)

