from collections import defaultdict


def get_rules():
    dic = defaultdict()
    start_state='E'
    dic={       #rules of grammar in LL(1) form
        "E" : [ ["T","E1"] ],
        "T" : [ ["F","T1"] ],
        "F" : [ ["id"], ["(","E",")"] ],
        "E1": [ ["+","T","E1"], ["eps"] ],
        "T1": [ ["*","F","T1"],  ["eps"],  ]
    }
    return dic,start_state


def print_rules(rules):
    print("\nRules are:")
    for key,rule in rules.items():
        print(key,end=" => ")
        for sub_rule in rule:
            for symbol in sub_rule:
                print(symbol,end=" ")
            print(' | ',end='')
        print()
    return
        
        
def isNonTerminal(symbol):
    if symbol in rules.keys():#all keys of rules are Non terminals
        return True
    return False

def first(rules,key,firstSet):
    for rule in rules[key]:#for every rule of that Non-terminal
        symbol=rule[0]
        if not isNonTerminal(symbol): #for terminals (not False => True)
            firstSet[key].add(symbol)
        else:                         # for terminal 
            firstSet[key]=firstSet[key].union(first(rules,symbol,firstSet))
    return firstSet[key]

    
def get_first_set(rules):#rules is defaultdict
    firstSet=defaultdict(set)
    for key in rules.keys():
        firstSet[key]
    for key,rule in rules.items():#for all rules
        first(rules,key,firstSet)
    return firstSet
    

def print_FFset(ffset,flag):#both first and follow as FFset
    if flag:
        print("\nFirst sets are:")
    else:
        print("\nFollow sets are:")
    for key,value in ffset.items():
        print(key,"=",value)
    return

def follow(rules,firstSet,followSet,non_ter):
    # for case; any_non_ter => alpha non_ter beta ( alpha,beta belongsto NonTer or Ter ) 
    for new_non_ter,rule in rules.items(): #for all productions, 1-1 production
        for sub_rule in rule:  #for one production_rules, 1-1 rule
            for i in range(len(sub_rule)): #for one rule_symbols, 1-1 symbol
                if sub_rule[i]==non_ter:
                    if i+1 < len(sub_rule):#checking next symbol beta 
                        beta=sub_rule[i+1]# when beta is present
#                         print("Y => alpha X beta as",new_non_ter,'=>..',non_ter,beta)
                        
                        if isNonTerminal(beta): #add firstSet(beta) into followSet(non_ter)
                            followSet[non_ter]=followSet[non_ter].union(firstSet[beta])
                            followSet[non_ter].discard('eps') #trying to remove epsilon, if there is
                        else:
                            followSet[non_ter].add(beta)
                            
                        if 'eps' in firstSet[beta] and new_non_ter!=beta :#!= for avoiding infinite loop (for T; P=> +TP)
                              followSet[non_ter]=followSet[non_ter].union(follow(rules,firstSet,followSet,new_non_ter))#add firstSet(beta) into followSet(non_ter)
                    
                    elif i+1 == len(sub_rule) and new_non_ter!=non_ter: # when beta is not there & != for avoiding infinite loop
#                         print("Y => alpha X as",new_non_ter,'=>..',non_ter)
                        if isNonTerminal(sub_rule[i]):
                            followSet[non_ter]=followSet[non_ter].union(follow(rules,firstSet,followSet,new_non_ter))
                            
    return followSet[non_ter]


def get_follow_set(rules,firstSet,start_state):#rules and follow are defaultdicts.
    followSet=defaultdict(set)
    for non_ter in rules.keys():
        if non_ter == start_state: #add terminal symbol
            followSet[non_ter].add('$')
        else:
            followSet[non_ter]
    
    for non_ter in rules.keys():
        follow(rules,firstSet,followSet,non_ter)
    return followSet


from collections import defaultdict
from copy import deepcopy
if __name__=="__main__":
    
    rules,start_state=get_rules()
    firstSet = get_first_set(rules)
    followSet = get_follow_set(rules,deepcopy(firstSet),start_state)
    
    print_rules(rules);       
    print_FFset(firstSet,True);   
    print_FFset(followSet,False);  

