# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 19:06:22 2020

@author: YASH
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 16:41:36 2020

@author: YASH
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 12:22:06 2019

@author: YASH
"""
from nltk.corpus import stopwords 
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize 
from nltk.stem.porter import PorterStemmer
import csv
import pandas as pd
import numpy 
import nltk

#Data cleaning Functions:
def isEnglish(s):
    try:
        s.encode('ascii')
    except UnicodeEncodeError:
        return False
    else:
        return True

    #The following function removes the part of the string that contains the substring eg. if
    #substring = 'http' , then http://www.google.com is removed, that means, remove until a space is found
def rem_substring(i,substring):

    m=0
    
    if (substring in i):
    #while i.find(substring)!=-1:
        k=i.find(substring)
        d=i.find(' ',k,len(i))
        if d!=-1:               #substring is present somwhere in the middle(not the end of the string)
            i=i[:k]+i[d:]
        else:                   #special case when the substring is present at the end, we needn't append the
            i=i[:k]             #substring after the junk string to our result
    
    m+= 1
    return (i)

def removeNonEnglish(i):
    result=[];y1=[];m=0

    if isEnglish(i):
        return i
#the following function converts all the text to the lower case
def lower_case(tweets):
    result=[]
    for i in tweets:
        result.append(i.lower())
    return result
def rem_punctuation(i):
    #print(len(tweets))

    validLetters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "
    
    x = ""
    for j in i:
        if (str(j) in validLetters)==True:
            x += j
    
    return x

def stop_words(tweet):
    #Removal of Stop words like is, am , be, are, was etc.
    
    stop_words1 = set(stopwords.words('english')) 
    indi=0
    
    new_s=[]
    Br_tweet = word_tokenize(tweet)
    for word in Br_tweet:
        if (word not in stop_words1):
            new_s.append(word)
    et=" ".join(new_s)

    return (et)
        
                

 #POS Tagger Function used to identify the adjectives, verbs, adverbs.

def POS_tagger(y,tweets, username):
    final = [];y_final=[]
        # for each line in tweets list
    m=0
    for line in tweets:
        t = []
            # for each sentence in the line
            # tokenize this sentence
        text= word_tokenize(line)
       
        k = nltk.pos_tag(text)
        for i in k:
                # Only Verbs, Nouns Adverbs & Adjectives are Considered
                if ((i[1][:2] == "VB") or (i[1][:2] == "JJ") or (i[1][:2] == "RB") or (i[1][:]=="NN") or (i[1][:]=="NNS")):
                    t.append(i[0])
        one_tweet=" ".join(t)
        if (len(one_tweet)>0):
            final.append(one_tweet)
            y_final.append(y[m])
        m+=1
    final=lower_case(final)
    dict1={'POS_Tweet':final,'class':y_final}
    db1=pd.DataFrame(dict1)
    filename = "Pos_tagged_" + username +  "1.csv"
    
    db1.to_csv(filename)

def stemming(word):
    # Find the root word
    # stemming of words
    porter = PorterStemmer()
    stemmed = porter.stem(word) 
    return stemmed
def emmpty(kl):
    if (len(kl)<=1):
        return True
    else:
        return False
def main():
    c=raw_input("Enter the name of the tweet file:")
    c_f=c+'.csv'
    db=pd.read_csv(c_f)
    db=db.dropna()
    tweets=list(db['tweet'])
    TWEETS=[]
    y=list(db['class'])
    Y=[]
    po=0
    for tweet in tweets:
        if emmpty(tweet)==False:
            tweet=rem_substring(tweet,'#')
        if emmpty(tweet)==False:
            tweet=rem_substring(tweet,'http')
        if emmpty(tweet)==False:
            tweet=rem_substring(tweet,'https')
        if emmpty(tweet)==False:
            tweet=rem_substring(tweet,'www')
        if emmpty(tweet)==False:
            tweet=rem_substring(tweet,'@')
        if emmpty(tweet)==False:
            tweet=rem_substring(tweet,'RT')
            
        if emmpty(tweet)==False:
            tweet=rem_punctuation(tweet)
        if emmpty(tweet)==False:
            tweet=stop_words(tweet)
        if emmpty(tweet)==False:
            tweet= removeNonEnglish(tweet)
        
        if emmpty(tweet)==False:
            TWEETS.append(tweet)
            Y.append(y[po])
        po+=1
            
        
    
   
    
    '''0 - hate speech 1 - offensive language 2 - neither'''
    
    #tweets.replace("."," ")
    for tweet in tweets:
        tweet=tweet.replace("."," ")

    ''' dict1={'Tweet':tweets}
    db1=pd.DataFrame(dict1)
    r_f='cleaned_'+ c + '.csv'
    db1.to_csv(r_f)
    '''    

    
    POS_tagger(Y,TWEETS,c)
     
    print("Tweets have now been cleaned !!")

main()