        

#Author: Pedram Ahadinejad
#Date: Feb 20 2021
#Description: A command line program to exract
#association rules for frequent itemsets.

#=============================================================================
import sys
import time
import itertools 
startTime = time.time()


#=============================================================================
# FUNCTIONS

# itemset / iset: an ordered list of int's representing an itemset
#                 we use int's not strings to make this more efficient

def istrClean(istr):
    istr = ' '.join(istr.strip('\n').split())
    for token in istr.split():
        if not token.isnumeric():
            print('Item "%s" is not an integer!' % token)
            exit(-1)
    return istr

def string2iset(istr):
    return [int(token) for token in istr.split()]

def iset2string(iset):
    itok = [str(item) for item in iset]
    return ' '.join(itok)

def subfrom(li1,li2):
    #li1 = li1.strip("[")
    #li1 = li1.strip("]")
    #li1 = li1.split(",")
    #intli1 = [int(x) for x in li1]
    intli1 = li1
    res = (list(list(set(intli1)-set(li2))))
    #print("result {}".format(res))
    return res

def powerset(s, n):
  j = list(itertools.combinations(s, n))
  #res =[]
  #for i in j:
  #	res.append((list(i)))
  #print(j)
  #print(res)
  for i,item in enumerate(j):
        j[i] = list(item)
  return j

#=============================================================================

sLen = []
lLen = []
# I also use a dic to store and retrieve the counts
sDic = {}
lDic = {}

length = 0
listPowerSets = {}


with open(sys.argv[1], 'r',encoding='utf-8') as inLev:
	for line in inLev:
            #line = istrClean(line)
            itemset = string2iset(line.strip('\n'))
            length = len(itemset)-1
            counts = itemset[0]
            sets = itemset[1:]
            #sLen.append(sets)

            temp = {str(sets):counts}
            sDic.update(temp)

with open(sys.argv[2], 'r',encoding='utf-8') as inLev:
        for line in inLev:
            #line = istrClean(line)
            itemset = string2iset(line.strip('\n'))
            counts = itemset[0]
            sets = itemset[1:]
            #lLen.append(sets)

            temp = {str(sets):counts}
            lDic.update(temp)


#print("Slen")
#print(sLen)
#print("sDic keys")
#print(sDic.keys())

count = 0
countAll = 0
for i in range(len(lDic.keys())-1):
    itemsets = eval(list(lDic.keys())[i])
    subs = powerset(itemsets,length)
    for item in subs:
        #str_item = "'" + str(item) + "'"
        if str(item) in list(sDic.keys()):
            lhs = item
            rhs = subfrom(itemsets,item)
            conf = (float(lDic[str(itemsets)])) / float(sDic[str(item)])
        
        if conf >= float(sys.argv[3]):
            print("{:.3f} {} => {}".format(conf,lhs,rhs))
            count = count + 1
            countAll = countAll + 1
        else:
            countAll = countAll + 1


print("Number of selected Rules {} ".format(count))
print("Number of ALL Rules {} ".format(countAll))

endTime = time.time()
print('Lapsed time:     %.3f' % (endTime - startTime))
