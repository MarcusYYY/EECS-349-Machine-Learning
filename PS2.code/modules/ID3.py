from math import *
from node import Node
import sys

def ID3(data_set, attribute_metadata, numerical_splits_count, depth):
    '''
        See Textbook for algorithm.
        Make sure to handle unknown values, some suggested approaches were
        given in lecture.
        ========================================================================================================
        Input:  A data_set, attribute_metadata, maximum number of splits to consider for numerical attributes,
        maximum depth to search to (depth = 0 indicates that this node should output a label)
        ========================================================================================================
        Output: The node representing the decision tree learned over the given data set
        ========================================================================================================
        '''
# Your code here
#     for attribute in range(0,len(data_set[0])):
#         handle_unknown(attribute,data_set,attribute_metadata)
#
#     d_tree = ID3_helper(data_set, attribute_metadata, numerical_splits_count, depth)
#     return d_tree
#
#
# def ID3_helper(data_set, attribute_metadata, numerical_splits_count, depth):
#     classList = [example[-1] for example in data_set]
#     #remaining values of this feature are all the same
#     if classList.count(classList[0]) == len(classList):
#         return classList[0]
#
#     # there is no remaining feature
#     if len(data_set[0]) == 1
#         return mode(classList)
#
#     bestFeature , best_split = pick_best_attribute(data_set, attribute_metadata, numerical_splits_count)
#     bestFeature_name = attribute_metadata[bestFeature]
#     myTree = {bestFeature_name:{}}
#     featValues = [example[bestFeature] for example in data_set]
#     uniqueFeatValues = set(featValues)
#     del (attribute_metadata[bestFeature])
#     for values in uniqueFeatValues:
#         subData_set = splitDataSet(data_set,bestFeature,values)
#         myTree[bestFeature_name][values] = ID3_helper(subData_set,attribute_metadata)
#     return myTree


def splitDataSet(data_set,attribute,values):
    retDataSet = []
    for featVec in data_set:
        if featVec[attribute] == values:
            reducedFeatVec = featVec[:attribute]
            reducedFeatVec.extend(featVec[attribute+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet







def handle_unknown(attribute,data_set,attribute_metadata):
    
    if attribute_metadata[attribute]['is_nominal']:
        valFreq = {}
        missing_idx = []
        idx = 0
        for i in data_set:
            if i[attribute] != None:
                if i[attribute] not in valFreq.keys():
                    valFreq[i[attribute]] = 1
                else:
                    valFreq[i[attribute]] +=1
            else:
                missing_idx.append(idx)
            idx += 1
        max_ = 0
        for key in valFreq.keys():
            if valFreq[key] > max_:
                max_ = valFreq[key]
                major = key
        for index in missing_idx:
            data_set[index][attribute] = major
    else:
        sum_ = 0
        len_ = 0
        missing_idx = []
        idx = 0
        for i in data_set:
            if i[attribute] != None:
                sum_ += i[attribute]
                len_ += 1
            else:
                missing_idx.append(idx)
            idx += 1
        mean_ = sum_ / len_
        for index in missing_idx:
            data_set[index][attribute] = mean_

# ======== Test Cases =============================
# print "Test of handle_unknown"

# attribute_metadata = [{'name': "winner",'is_nominal': True},{'name': "opprundifferential",'is_nominal': False}]
# data_set = [[0],[1],[1],[None],[1],[1]]
# handle_unknown(0,data_set,attribute_metadata)
# pass_ = data_set == [[0],[1],[1],[1],[1],[1]]

# if not pass_:
#     print str(handle_unknown(0,data_set,attribute_metadata)) + " should be [[0],[1],[1],[1],[1],[1]] "
# else:
#     print "test1 passed"



# data_set = [[0,2.7],[1,3.2],[1,4.0],[0,4.1],[1,4.0],[0,None]]
# handle_unknown(1,data_set,attribute_metadata)
# pass_ = data_set == [[0,2.7],[1,3.2],[1,4.0],[0,4.1],[1,4.0],[0,3.6]]
# if not pass_:
#     print str(handle_unknown(1,data_set,attribute_metadata)) + " should be [[0,2],[1,3],[1,4],[0,4],[1,4],[0,4]]"
# else:
#     print "test2 passed"




def check_homogenous(data_set):
    '''
        ========================================================================================================
        Input:  A data_set
        ========================================================================================================
        Job:    Checks if the output value (index 0) is the same for all examples in the the data_set, if so return that output value, otherwise return None.
        ========================================================================================================
        Output: Return either the homogenous attribute or None
        ========================================================================================================
        '''
    # Your code here
    flag = data_set[0][0]
    for i in data_set:
        if i[0] != flag:
            return None
    return flag
# ======== Test Cases =============================
# data_set = [[0],[1],[1],[1],[1],[1]]
# check_homogenous(data_set) ==  None
# data_set = [[0],[1],[None],[0]]
# check_homogenous(data_set) ==  None
# data_set = [[1],[1],[1],[1],[1],[1]]
# check_homogenous(data_set) ==  1

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
            if numerical_splits_count < 0:
                continue
            gain_ratio,numeric_split = gain_ratio_numeric(data_set,attribute,1)
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
# numerical_splits_count = [20,20]
# attribute_metadata = [{'name': "winner",'is_nominal': True},{'name': "opprundifferential",'is_nominal': False}]
# data_set = [[1, 0.27], [0, 0.42], [0, 0.86], [0, 0.68], [0, 0.04], [1, 0.01], [1, 0.33], [1, 0.42], [0, 0.51], [1, 0.4]]
# pick_best_attribute(data_set, attribute_metadata, numerical_splits_count) == (1, 0.51)
# attribute_metadata = [{'name': "winner",'is_nominal': True},{'name': "weather",'is_nominal': True}]
# data_set = [[0, 0], [1, 0], [0, 2], [0, 2], [0, 3], [1, 1], [0, 4], [0, 2], [1, 2], [1, 5]]
# pick_best_attribute(data_set, attribute_metadata, numerical_splits_count) == (1, False)

# Uses gain_ratio_nominal or gain_ratio_numeric to calculate gain ratio.

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
        return count_0
    else:
        return count_1

# ======== Test case =============================
# data_set = [[0],[1],[1],[1],[1],[1]]
# mode(data_set) == 1
# data_set = [[0],[1],[0],[0]]
# mode(data_set) == 0

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
        freq = (float)(numCount[i]) / (len(data_set))
        ent += freq * log(freq,2)
    return -ent

# ======== Test case =============================
# data_set = [[0],[1],[1],[1],[0],[1],[1],[1]]
# entropy(data_set) == 0.811
# data_set = [[0],[0],[1],[1],[0],[1],[1],[0]]
# entropy(data_set) == 1.0
# data_set = [[0],[0],[0],[0],[0],[0],[0],[0]]
# entropy(data_set) == 0


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
# data_set, attr = [[1, 2], [1, 0], [1, 0], [0, 2], [0, 2], [0, 0], [1, 3], [0, 4], [0, 3], [1, 1]], 1
# gain_ratio_nominal(data_set,attr) == 0.11470666361703151
# data_set, attr = [[1, 2], [1, 2], [0, 4], [0, 0], [0, 1], [0, 3], [0, 0], [0, 0], [0, 4], [0, 2]], 1
# gain_ratio_nominal(data_set,attr) == 0.2056423328155741
# data_set, attr = [[0, 3], [0, 3], [0, 3], [0, 4], [0, 4], [0, 4], [0, 0], [0, 2], [1, 4], [0, 4]], 1
# gain_ratio_nominal(data_set,attr) == 0.06409559743967516

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
# data_set,attr,step = [[0,0.05], [1,0.17], [1,0.64], [0,0.38], [0,0.19], [1,0.68], [1,0.69], [1,0.17], [1,0.4], [0,0.53]], 1, 2
# gain_ratio_numeric(data_set,attr,step) == (0.31918053332474033, 0.64)
# data_set,attr,step = [[1, 0.35], [1, 0.24], [0, 0.67], [0, 0.36], [1, 0.94], [1, 0.4], [1, 0.15], [0, 0.1], [1, 0.61], [1, 0.17]], 1, 4
# gain_ratio_numeric(data_set,attr,step) == (0.11689800358692547, 0.94)
# data_set,attr,step = [[1, 0.1], [0, 0.29], [1, 0.03], [0, 0.47], [1, 0.25], [1, 0.12], [1, 0.67], [1, 0.73], [1, 0.85], [1, 0.25]], 1, 1
# gain_ratio_numeric(data_set,attr,step) == (0.23645279766002802, 0.29)

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
# data_set, attr = [[0, 4], [1, 3], [1, 2], [0, 0], [0, 0], [0, 4], [1, 4], [0, 2], [1, 2], [0, 1]], 1
# split_on_nominal(data_set, attr) == {0: [[0, 0], [0, 0]], 1: [[0, 1]], 2: [[1, 2], [0, 2], [1, 2]], 3: [[1, 3]], 4: [[0, 4], [0, 4], [1, 4]]}
# data_set, attr = [[1, 2], [1, 0], [0, 0], [1, 3], [0, 2], [0, 3], [0, 4], [0, 4], [1, 2], [0, 1]], 1
# split on_nominal(data_set, attr) == {0: [[1, 0], [0, 0]], 1: [[0, 1]], 2: [[1, 2], [0, 2], [1, 2]], 3: [[1, 3], [0, 3]], 4: [[0, 4], [0, 4]]}

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
    up = []
    down = []
    for i in data_set:
        i[attribute] = round(float(i[attribute]),2)
    for i in data_set:
        if i[attribute] < splitting_value:
            down.append([i[0],i[attribute]])
        else:
            up.append([i[0],i[attribute]])

count_Attribute = (down,up)
    
    
    
    return count_Attribute
    
    return count_Attribute

# ======== Test case =============================
# d_set,a,sval = [[1, 0.25], [1, 0.89], [0, 0.93], [0, 0.48], [1, 0.19], [1, 0.49], [0, 0.6], [0, 0.6], [1, 0.34], [1, 0.19]],1,0.48
# split_on_numerical(d_set,a,sval) == ([[1, 0.25], [1, 0.19], [1, 0.34], [1, 0.19]],[[1, 0.89], [0, 0.93], [0, 0.48], [1, 0.49], [0, 0.6], [0, 0.6]])
# d_set,a,sval = [[0, 0.91], [0, 0.84], [1, 0.82], [1, 0.07], [0, 0.82],[0, 0.59], [0, 0.87], [0, 0.17], [1, 0.05], [1, 0.76]],1,0.17
# split_on_numerical(d_set,a,sval) == ([[1, 0.07], [1, 0.05]],[[0, 0.91],[0, 0.84], [1, 0.82], [0, 0.82], [0, 0.59], [0, 0.87], [0, 0.17], [1, 0.76]])