#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: djokester
Samriddhi Sinha,
IIT Kharagpur
"""
from anytree import Node, RenderTree
import os
#lst = string.split(" ")
def build(tr, node):
    if len(tr) > 1:
        if node == 0:
            nde = Node(tr[1])
            build(tr[2:],nde)
            #print("1", nde)
            return(nde)
        else: 
            if tr[0] == "(":
                nde = Node(tr[1], parent = node)
                build(tr[2:],nde)
                #print("2", nde)
            else:
                if tr[0] == ")":
                    build(tr[1:],node.parent)
                else:
                    nde = Node(tr[0], parent = node)
                    build(tr[2:], node.parent)
                    #print("3", nde)
    else:
        return node.parent
        #print("4", node)

def parse(sentence):
    str1 = 'echo \'{"sentence": \"'
    str2 = '\"}\' > examples.jsonl'
    c1 = str1 + sentence + str2 
    os.system(c1)
    c2 = 'python -m allennlp.run predict     https://s3-us-west-2.amazonaws.com/allennlp/models/elmo-constituency-parser-2018.03.14.tar.gz     examples.jsonl'
    a = os.popen(c2).read()
    x = "".join(list(a.split("\"trees\":")[1].split("}\n\n")[0])[2:-1])
    string = list(x)
    #print(string)
    x = []
    for ix, item in enumerate(string):
        if item == "(" and string[ix+1]!= " ":
            x.append(ix+1)
        if item == ")" and string[ix-1]!= " ":
            x.append(ix)
    #print(x)
    x = [i + x.index(i) for i in x]
    #print(x)
    for ix in x:
        string.insert(ix, " ")
    string = "".join(string)
    #print(string)
    lst = string.split(" ")
    a = build(lst, 0)
    for pre, fill, node in RenderTree(a):
        print("%s%s" % (pre, node.name))


if __name__ == '__main__':
    parse("James went to the corner shop to buy some eggs, milk and bread for breakfast.")
