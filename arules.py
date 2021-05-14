# Author: Pedram Ahadinejad
# Date: Feb 20 2021
# Description: A command line program to exract
# association rules for frequent itemsets.

# =============================================================================
import sys
import time
import itertools

startTime = time.time()


# =============================================================================
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


def subfrom(li1, li2):

    intli1 = li1
    res = (list(set(intli1) - set(li2)))
    # print("result {}".format(res))
    return res


def powerset(s, n):
    return list(itertools.combinations(s, n))


# =============================================================================

lLen = []
# I also use a dic to store and retrieve the counts
sDic = {}
lDic = {}

length = 0
listPowerSets = {}

with open(sys.argv[1], 'r', encoding='utf-8') as inLev:
    for line in inLev:
        line = istrClean(line)
        itemset = string2iset(line.strip('\n'))
        length = len(itemset) - 1
        counts = itemset[0]
        sets = itemset[1:]

        sets = iset2string(sets)
        sDic[sets] = counts
count = 0
countAll = 0
confCheck = float(sys.argv[3])

with open(sys.argv[2], 'r', encoding='utf-8') as inLev:
    for line in inLev:
        line = istrClean(line)
        itemset = string2iset(line.strip('\n'))
        counts = itemset[0]
        sets = itemset[1:]

        subs = powerset(list(range(len(sets))), length)
        for sub in subs:
            lhs = []
            rhs = []
            for i in range(len(sets)):
                if i in sub:
                    lhs.append(sets[i])
                else:
                    rhs.append(sets[i])

            lhs = iset2string(lhs)
            if lhs in sDic:
                conf = (float(counts)) / float(sDic[lhs])
            else:
                continue

            if conf >= confCheck:
                print("{:.3f} {} => {}".format(conf, lhs, iset2string(rhs)))
                count = count + 1
                countAll = countAll + 1
            else:
                countAll = countAll + 1

print("Number of selected Rules {} ".format(count))
print("Number of ALL Rules {} ".format(countAll))

endTime = time.time()
print('Lapsed time:     %.3f' % (endTime - startTime))
