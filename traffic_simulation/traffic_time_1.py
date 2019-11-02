# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 11:54:52 2018

@author: Shamith
"""
"""
Phase 1: Development of the calculation of the time-of-trip
through the sub development of the car class, time calculation
and other important parts

This phase is complete with good results, as of 19 AUG 2018, 6 PM 
the next phase will be done as and when time permits

"""



class car():
    #this class is to store a times and distances
    def __init__(self,startTimeHours,startTimeMins,sections):
        self.timeStart=self.timehtc(startTimeHours,startTimeMins) #starting time in computer time
        self.timeNow=self.timeStart #current time in computer time
        self.timeTrip = 0 #time completed for trip until now
        self.distNow=0 #current distance covered
        self.distTotal=0 #total distance of trip - calculated later
        self.sectNow=1 #current section of the vehicle
        self.sectLast=max(list(sections.keys())) #last section of the vehicle
        for x,y in sections.items():
            self.distTotal+=y #to get the complete distance
    
    def timehtc(self,h,m):
        #convert human time to computer time
        t=(h*60.0)+(m)
        return t
    
    def timecth(self,t):
        # convert computer time to human time
        h=t//60
        m=t-(h*60)
        return h,m
    
    def dist_section(self,sections):
        #to calculate the section distance till current section for changing section
        #this code is needed, for checking whether to move into new sections or not
        #this code required the original "sections" dictionary to find the required distance sum
        
        #this is, after all, one implementation of the section changing algo, ... 
        #and may not be required for a different implementation
        x=0.0 #cumulative distance counter
        for i in range(self.sectNow + 1):
            #calculate the sum of all distances for all sections covered until now
            if i<1:
                continue
            x+=sections[i]
        #now it returns the sum of all distances to the current section
        return x
    
    #end of class definition

#program variables
startTimeHours=6 #ensure this no is between 1 and 11 (means 1 and 11 pm)
startTimeMins=0 #ensure this no. is between 0 and 60
#code to check above two nos is done later
sections={1:5.0,2:15.3,3:7.2,4:2.5} 
tstep=6 #step time, in minutes
#initialise the car object
c1=car(startTimeHours,startTimeMins,sections)

#some variables for observation purpose
a1=c1.timeNow
a2=c1.sectLast
a3=c1.distTotal


def getspeed(t):
    #simple speed function as per deliverables for phase 1
    #the function to get the speed (as per planned detailed modelling) will be made separately as per phase 2
    #the speed is 10 kmph, only for temporary testing purposes
    return 10.0 


#code to start the calculations
count=0 #no. of iterations of program
while True:
    count+=1
    spd=getspeed(c1.timeNow) #using math model to get the speed
    distCover=spd*(tstep/60.0) #distance covered for 10 min
    if (c1.sectNow == c1.sectLast) & (distCover+c1.distNow > c1.distTotal):
        distLeft=c1.distTotal-c1.distNow #distance left
        time2=distLeft/spd #time to complete
        c1.timeNow+=time2 #adding time
        c1.distNow+=distLeft #adding distance
        break
    if (c1.distNow+distCover > c1.dist_section(sections)) & (c1.sectNow != c1.sectLast):
        distLeft= c1.dist_section(sections) - c1.distNow
        time1=distLeft/spd
        c1.timeNow+=time1
        c1.distNow+=distLeft 
        c1.sectNow+=1 #incrementing the section, to implement the section change
        continue #to start the loop again, and not do the same thing as below
    c1.distNow += distCover
    c1.timeNow += tstep
c1.timeTrip=c1.timeNow-c1.timeStart #time to take trip has been calculated  
a11=c1.timeNow
timeEnd=c1.timecth(c1.timeNow)
timeTrip=c1.timecth(c1.timeTrip)
print("the journey of ",c1.distTotal," km, took",timeTrip[0]," hours &",timeTrip[1]," minutes and ended at ",timeEnd[0],":",timeEnd[1], " pm.")

        