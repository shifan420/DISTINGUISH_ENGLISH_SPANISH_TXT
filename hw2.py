#!/usr/bin/env python
# coding: utf-8

# In[151]:


import sys
import math


# In[152]:


def get_parameter_vectors():
    '''
    This function parses e.txt and s.txt to get the  26-dimensional multinomial
    parameter vector (characters probabilities of English and Spanish) as
    descibed in section 1.2 of the writeup

    Returns: tuple of vectors e and s
    '''
    #Implementing vectors e,s as lists (arrays) of length 26
    #with p[0] being the probability of 'A' and so on
    e=[0]*26
    s=[0]*26
    m = 0

    with open('e.txt',encoding='utf-8') as f:
        for line in f:
            char,prob=line.strip().split(" ")
            e[ord(char)-ord('A')]=float(prob)
    f.close()

    with open('s.txt',encoding='utf-8') as f:
        for line in f:
            char,prob=line.strip().split(" ")
            s[ord(char)-ord('A')]=float(prob)
    f.close()

    return (e,s)


# In[161]:


def shred(filename):
    with open(filename, encoding = 'utf-8') as f:
        readfile = f.read()
        def processfile(readfile, phrase):
            if readfile:
                for i in '~!@#$%^&*()_+`-=[\\]\;\'./,{}|:"<>?':
                    readfile = readfile.replace(i,"")
                    readfile = readfile.upper()
                count = readfile.count(phrase)
            return count
    alpha_list = []
    alpha_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    print('Q1')
    countlist = [0]*26
    for i in range(26):
        countlist[i] = process_letter(readfile, alpha_list[i])
        print(alpha_list[i] + str(' ') + str(countlist[i]))
    e,s = get_parameter_vectors()
    e1 = e[0]
    s1 = s[0]
    X1 = countlist[0]
    print("Q2")
    q2_1 = X1*math.log(e1)
    q2_2 = X1*math.log(s1)
    print("%.4f" % q2_1)
    print("%.4f" % q2_2)
    
    sum_e= 0
    for i in range(26):
        sum_e = countlist[i] * math.log(e[i]) + sum_e
    sum_s= 0
    for i in range(26):
        sum_s = countlist[i] * math.log(s[i]) + sum_s   
    
    print('Q3')
    q3_1 = math.log(0.6)+ sum_e
    q3_2 = math.log(0.4)+ sum_s
    print("%.4f" % q3_1)
    print("%.4f" % q3_2)
    
    print('Q4')
    
    q4 = 1/(1 + math.exp(q3_2 - q3_1))
    print("%.4f" % q4)
    return 


# In[163]:


shred('letter.txt')

