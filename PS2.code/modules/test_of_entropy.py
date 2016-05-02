_author_ = 'Marcus'
from math import *
def entropy(data_set):
    '''
    ========================================================================================================
    Input:  A data_set
    ========================================================================================================
    Job:    Calculates the entropy of the attribute at the 0th index, the value we want to predict.
    ========================================================================================================
    Output: Returns entropy. See Textbook for formula
    ========================================================================================================
    '''
    ent = 0
    numCount = {}
    for i in data_set:
        if i[0] in numCount.keys():
            numCount[i[0]] +=1
        else:
            numCount[i[0]] = 1
    for i in numCount.keys():
        if numCount[i] == len(data_set):
            return 0
        freq = (float)(numCount[i]) / len(data_set)
        ent += freq * log(freq,2)
    return -ent

# ======== Test case =============================
# print "test of entropy(data_set)"
# data_set = [[0],[1],[1],[1],[0],[1],[1],[1]]
# print str(entropy(data_set)) + " should be 0.811"
#
# data_set = [[0],[0],[1],[1],[0],[1],[1],[0]]
# print str(entropy(data_set)) + " should be 1.0"
#
# data_set = [[0],[0],[0],[0],[0],[0],[0],[0]]
# print str((entropy(data_set))) + " should be 0"
# print "================"


def mode(data_set):
    '''
    ========================================================================================================
    Input:  A data_set
    ========================================================================================================
    Job:    Takes a data_set and finds mode of index 0.
    ========================================================================================================
    Output: mode of index 0.
    ========================================================================================================
    '''
    # Your code here
    count_0 = 0
    count_1 = 0

    for i in data_set:
        if i[0] == 1:
            count_1 += 1
        else:
            count_0 += 1
    if count_0 > count_1:
        return 0
    else:
        return 1
    pass
# ======== Test case =============================
# print "Test of mode(data_set)"
# data_set = [[0],[1],[1],[1],[1],[1]]
# print str(mode(data_set)) + " should be 1"
#
# data_set = [[0],[1],[0],[0]]
# print str(mode(data_set)) + " should be 0"
# print "================"


def gain_ratio_nominal(data_set, attribute):
    '''
    ========================================================================================================
    Input:  Subset of data_set, index for a nominal attribute
    ========================================================================================================
    Job:    Finds the gain ratio of a nominal attribute in relation to the variable we are training on.
    ========================================================================================================
    Output: Returns gain_ratio. See https://en.wikipedia.org/wiki/Information_gain_ratio
    ========================================================================================================
    '''
    # Your code here
    numCount = {}
    total = []
    for i in data_set:
        total.append([i[0]])
        if i[attribute] in numCount.keys():
            numCount[i[attribute]].append([i[0]])
        else:
            cache = []
            cache.append([i[0]])
            numCount[i[attribute]] = cache
    sum_ = 0
    IV = 0
    t = len(total)
    for i in numCount:
        a = len(numCount[i])
        sum_ += ((float)(a)/(t)) * entropy(numCount[i])
        b = (float)(a)/(t)
        IV -= b * log(b,2)

    return (entropy(total) - sum_)/IV

# ======== Test case =============================
# print "Test of gain_ratio_nominal"
# data_set, attr = [[1, 2], [1, 0], [1, 0], [0, 2], [0, 2], [0, 0], [1, 3], [0, 4], [0, 3], [1, 1]], 1
# print  str(gain_ratio_nominal(data_set,1)) + " Should be  0.11470666361703151"
#
#
#
# data_set, attr = [[1, 2], [1, 2], [0, 4], [0, 0], [0, 1], [0, 3], [0, 0], [0, 0], [0, 4], [0, 2]], 1
# print str(gain_ratio_nominal(data_set,1)) + " Should be  0.2056423328155741"
#
#
# data_set, attr = [[0, 3], [0, 3], [0, 3], [0, 4], [0, 4], [0, 4], [0, 0], [0, 2], [1, 4], [0, 4]], 1
# print str(gain_ratio_nominal(data_set,1)) + " should be 0.06409559743967516"
#
# print "================================="




def split_on_nominal(data_set, attribute):
    '''
    ========================================================================================================
    Input:  subset of data set, the index for a nominal attribute.
    ========================================================================================================
    Job:    Creates a dictionary of all values of the attribute.
    ========================================================================================================
    Output: Dictionary of all values pointing to a list of all the data with that attribute
    ========================================================================================================
    '''
    # Your code here
    count_Attribute = {}
    for i in data_set:
        if i[attribute] in count_Attribute.keys():
            count_Attribute[i[attribute]].append([i[0],i[attribute]])
        else:
            cache = []
            cache.append([i[0],i[attribute]])
            count_Attribute[i[attribute]] = cache
    return count_Attribute

# ======== Test case =============================
# print "test of split_on_nominal"
# data_set, attr = [[0, 4], [1, 3], [1, 2], [0, 0], [0, 0], [0, 4], [1, 4], [0, 2], [1, 2], [0, 1]], 1
# print str(split_on_nominal(data_set,attr)) + " should be {0: [[0, 0], [0, 0]], 1: [[0, 1]], 2: [[1, 2], [0, 2], [1, 2]], 3: [[1, 3]], 4: [[0, 4], [0, 4], [1, 4]]}"
#
# data_set, attr = [[1, 2], [1, 0], [0, 0], [1, 3], [0, 2], [0, 3], [0, 4], [0, 4], [1, 2], [0, 1]], 1
# print str(split_on_nominal(data_set,attr)) + " should be {0: [[1, 0], [0, 0]], 1: [[0, 1]], 2: [[1, 2], [0, 2], [1, 2]], 3: [[1, 3], [0, 3]], 4: [[0, 4], [0, 4]]}"



def split_on_numerical(data_set, attribute, splitting_value):
    '''
    ========================================================================================================
    Input:  Subset of data set, the index for a numeric attribute, threshold (splitting) value
    ========================================================================================================
    Job:    Splits data_set into a tuple of two lists, the first list contains the examples where the given
	attribute has value less than the splitting value, the second list contains the other examples
    ========================================================================================================
    Output: Tuple of two lists as described above
    ========================================================================================================
    '''
    # Your code here
    count_Attribute = []
    up = []
    down = []
    for i in data_set:
        i[attribute] = round(float(i[attribute]),2)
    for i in data_set:
        if i[attribute] < splitting_value:
            down.append([i[0],i[attribute]])
        else:
            up.append([i[0],i[attribute]])

    count_Attribute.append(down)
    count_Attribute.append(up)

    return count_Attribute

# ======== Test case =============================
# print "test of split_on_numerical(data_set, attribute, splitting_value)"

# d_set,a,sval = [[1, 0.25], [1, 0.89], [0, 0.93], [0, 0.48], [1, 0.19], [1, 0.49], [0, 0.6], [0, 0.6], [1, 0.34],[1, 0.19]],1,0.48

# print  str(split_on_numerical(d_set,a,sval)) + " should be ([[1, 0.25], [1, 0.19], [1, 0.34], [1, 0.19]],[[1, 0.89], [0, 0.93], [0, 0.48], [1, 0.49], [0, 0.6], [0, 0.6]])"

# d_set,a,sval = [[0, 0.91], [0, 0.84], [1, 0.82], [1, 0.07], [0, 0.82],[0, 0.59], [0, 0.87], [0, 0.17], [1, 0.05], [1, 0.76]],1,0.17
# print  str(split_on_numerical(d_set,a,sval)) + " should be ([[1, 0.07], [1, 0.05]],[[0, 0.91],[0, 0.84], [1, 0.82], [0, 0.82], [0, 0.59], [0, 0.87], [0, 0.17], [1, 0.76]])"

def gain_ratio_numeric(data_set, attribute, steps):
    '''
    ========================================================================================================
    Input:  Subset of data set, the index for a numeric attribute, and a step size for normalizing the data.
    ========================================================================================================
    Job:    Calculate the gain_ratio_numeric and find the best single threshold value
            The threshold will be used to split examples into two sets
                 those with attribute value GREATER THAN OR EQUAL TO threshold
                 those with attribute value LESS THAN threshold
            Use the equation here: https://en.wikipedia.org/wiki/Information_gain_ratio
            And restrict your search for possible thresholds to examples with array index mod(step) == 0
    ========================================================================================================
    Output: This function returns the gain ratio and threshold value
    ========================================================================================================
    '''
    max = 0
    t = entropy(data_set)
    tag = 0
    IV = 0
    idx = 0
    while idx < len(data_set):
        divide = split_on_numerical(data_set,attribute,data_set[idx][attribute])
        part_low = entropy(divide[0])
        part_high = entropy(divide[1])
        len_up = len(divide[1])
        len_down = len(divide[0])
        a = float(len_up)/(len_up + len_down)
        b = float(len_down)/(len_up + len_down)
        total_entropy = part_low * b + part_high * a
        max_ = (t - total_entropy)
        if max_ > max:
            max = max_
            tag = data_set[idx][attribute]
            IV = -a*log(a,2) - b*log(b,2)
        idx += steps
    if IV != 0:
        return max/IV, tag
    else:
        return None

# ======== Test case =============================
print "Test of gain_ratio_numeric"
pass_ = False
data_set,attr,step = [[0,0.05], [1,0.17], [1,0.64], [0,0.38], [0,0.19], [1,0.68], [1,0.69], [1,0.17], [1,0.4], [0,0.53]], 1, 2
pass_ = gain_ratio_numeric(data_set,attr,step) == (0.31918053332474033, 0.64)
if not pass_:
    print str(gain_ratio_numeric(data_set,attr,step)) + " should be (0.31918053332474033, 0.64)"
else:
    print "test1 passed"
# gain_ratio_numeric(data_set,attr,step) == (0.31918053332474033, 0.64)
data_set,attr,step = [[1, 0.35], [1, 0.24], [0, 0.67], [0, 0.36], [1, 0.94], [1, 0.4], [1, 0.15], [0, 0.1], [1, 0.61], [1, 0.17]], 1, 4
pass_ = gain_ratio_numeric(data_set,attr,step) == (0.11689800358692547, 0.94)
if not pass_:
        print str(gain_ratio_numeric(data_set,attr,step)) + " should be (0.11689800358692547, 0.94)"
else:
    print "test2 passed"
# gain_ratio_numeric(data_set,attr,step) == (0.11689800358692547, 0.94)
data_set,attr,step = [[1, 0.1], [0, 0.29], [1, 0.03], [0, 0.47], [1, 0.25], [1, 0.12], [1, 0.67], [1, 0.73], [1, 0.85], [1, 0.25]], 1, 1
pass_ = gain_ratio_numeric(data_set,attr,step) == (0.23645279766002802, 0.29)
if not pass_:
        print str(gain_ratio_numeric(data_set,attr,step)) + " should be (0.23645279766002802, 0.29)"
else:
    print "test3 passed"

def pick_best_attribute(data_set, attribute_metadata, numerical_splits_count):
    '''
    ========================================================================================================
    Input:  A data_set, attribute_metadata, splits counts for numeric
    ========================================================================================================
    Job:    Find the attribute that maximizes the gain ratio. If attribute is numeric return best split value.
            If nominal, then split value is False.
            If gain ratio of all the attributes is 0, then return False, False
            Only consider numeric splits for which numerical_splits_count is greater than zero
    ========================================================================================================
    Output: best attribute, split value if numeric
    ========================================================================================================
    '''
    max_gainratio = 0
    best_attribute = 0
    best_numeric_split = 0

    for attribute in range(1,len(data_set[0])):
        is_nominal = attribute_metadata[attribute]['is_nominal']
        if is_nominal:
            gain_ratio = gain_ratio_nominal(data_set,attribute)
            if gain_ratio > max_gainratio:
                max_gainratio = gain_ratio
                best_attribute = attribute
        else:
            gain_ratio,numeric_split = gain_ratio_numeric(data_set,attribute,2)
            if gain_ratio > max_gainratio:
                max_gainratio = gain_ratio
                best_attribute = attribute
                best_numeric_split = numeric_split

    if max_gainratio == 0:
            return False,False

    if attribute_metadata[best_attribute]['is_nominal']:
        return best_attribute,False
    else:
        return best_attribute,best_numeric_split

# # ======== Test Cases =============================
print "Test of pick_best_attribute"
numerical_splits_count = [20,20]
attribute_metadata = [{'name': "winner",'is_nominal': True},{'name': "opprundifferential",'is_nominal': False}]
data_set = [[1, 0.27], [0, 0.42], [0, 0.86], [0, 0.68], [0, 0.04], [1, 0.01], [1, 0.33], [1, 0.42], [0, 0.51], [1, 0.4]]
pass_ = pick_best_attribute(data_set, attribute_metadata, numerical_splits_count) == (1, 0.51)
if not pass_:
    print str(pick_best_attribute(data_set, attribute_metadata, numerical_splits_count)) + " should be (1, 0.51)"
else:
    print "test1 passed"


attribute_metadata = [{'name': "winner",'is_nominal': True},{'name': "weather",'is_nominal': True}]
data_set = [[0, 0], [1, 0], [0, 2], [0, 2], [0, 3], [1, 1], [0, 4], [0, 2], [1, 2], [1, 5]]
pass_ = pick_best_attribute(data_set, attribute_metadata, numerical_splits_count) == (1, False)
if not pass_:
    print str(pick_best_attribute(data_set, attribute_metadata, numerical_splits_count)) + " should be (1,False)"
else:
    print "test2 passed"

