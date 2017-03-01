from __future__ import print_function, division

import nsfg

# Question 1:
    
pres = nsfg.ReadFemResp()

# Question 2:

pres.columns
pres.head(20)
pres.tail(30)

countcol = 0
countrow = 0

for columns in pres:
    countcol += 1
    
for rows in pres.agescrn:
    countrow += 1

print ("There are %d rows and %d columns" %(countrow, countcol))

# Question 3:

minimum = None       
maximum = None

for num in pres.agescrn:                          
    if minimum == None or num < minimum :
        minimum = num

for num in pres.agescrn:        
    if maximum == None or maximum < num :
        maximum = num

print ("Oldest Respondent:", maximum)
print ("Youngest Respondent:", minimum)

# Question 4:
    
countrow2 = 0
for values in pres.numpregs:
    if countrow2 == 2298:
        print ("Pregnancies: " + str(values))
    countrow2 += 1

# Question 5:

ageunder25 =pres[pres['agescrn'] <= 25]
avgpreg = ageunder25['pregnum']

print ("Average number of pregnanices for women aged 25 or under: ", avgpreg.mean())
        
# Question 6:

agemax =pres[pres['agescrn'] == 44]
avgpregmax = agemax['pregnum']
print ("Average number of pregnanices for women aged 44: ", avgpregmax.mean())

