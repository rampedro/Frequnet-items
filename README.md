#Improving Apriori:

The Apriori algorithm for discovering frequent itemsets can be expensive. So people are always looking at different ways to improve further the approach's efficiency.

One expensive step, for example, is validating candidate itemsets by counting their supports to find the ones meeting or exceeding the support threshold. A common implementation is to use a hash-tree. If this step is done naïvely, the implementation will be too slow to be used.

Let us consider an Apriori program that takes as input the frequent itemsets of length k (with respect to some support-count threshold), the transaction itemsets, and a support-count threshold, and produces as output the frequent itemsets of length k+1. (We assume the support-count threshold for the input frequent itemsets provided will be the same as, or lower than, the requested threshold for the output.) Let us name such a program levelUp.

How much time levelUp will take for a given task depends on how many pre-candidates are produced (by the join step). A pre-candidate advances to being a candidate itemset if it passes the apriori test. At a given support-count threshold, the same number of candidate itemsets will result, regardless. But perhaps we can reduce the number of pre-candidates produced.

Consider that we order the items in each itemset from least to most frequent, rather than just ordering them in some “random” way, say lexicographically (as by the standard algorithm). That is, how frequently each item appears in the transaction database; so the frequencies of those 1-itemsets. Why could this help? The prefixes of the frequent itemsets of length k will be less common, meaning fewer pre-candidates should result from the join step. If this is significant in practice, this could make the algorithm perform better.

Write a program in Python (3) or in Java called “levelUp.py” or “LevelUp.java”, respectively, to test this. Your algorithm should take three arguments, and a fourth optional argument:

a file with the frequent itemsets of length k at the given support threshold (but not with the support counts reported),
a file with the transaction itemsets, and
the support threshold count.
E.g.,

% python levelUp.py mushroom-lev4-sup500.dat mushroom-trans.dat 500
