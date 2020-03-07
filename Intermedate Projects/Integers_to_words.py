import numpy as np
import fractions
import re 
import collections


ones=["zero","one","two","three","four","five","six","seven","eight","nine"]
tens=["tens","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
twentys=["twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
hundreds=["hundred","thousand","million","billion"]
word_form=[]

def one_word(numb):
    word_form.append(ones[int(numb)])

def tens_word(numb):
    #print("comes here")
    print(numb)
    if int(numb)!=0:
        if int(numb)>=20:
            word_form.append(twentys[int(numb[0])-2])
            if int(numb[1])>0:
                one_word(numb[1])
        elif int(numb)<10:
            #print("comes here")
            one_word(numb[1])
        else:
            word_form.append(tens[int(numb)-10])


def hundred_word(numb):
    #print("comes in hundred")
    if int(numb)!=0:
        if numb[0] in "123456789":
            word_form.append(ones[int(numb[0])]+" hundred")
            
        tens_word(numb[1:])


def thousand_word(numb):
        #print("comes in thousand")
        num1=numb[len(numb)-3:]
        num2=numb[0:len(numb)-3]
        if int(num2)!=0:

            if len(num2)==1:
                one_word(num2)
            elif len(num2)==2:
                tens_word(num2)
            else:
                hundred_word(num2)
            word_form.append("Thousand")

        hundred_word(num1)

def million_word(numb):

        #print("comes in million")
        num1=numb[len(numb)-6:]
        num2=numb[0:len(numb)-6]
        if int(num2)!=0:
            if len(num2)==1:
                one_word(num2)
            elif len(num2)==2:
                tens_word(num2)
            else:
                hundred_word(num2)
            word_form.append("Million")

        thousand_word(num1)


def billion_word(numb):
    num1=numb[1:]
    one_word(numb[0])
    word_form.append("billion")
    million_word(num1)


number=input("enter the number: ")
l=len(number)

if int(number)==0:
    word_form.append("zero")
else:
    if l==1:
        one_word(number)
    elif l==2:
        tens_word(number)
    elif l==3:
        hundred_word(number)
    elif l<=6 and l>=4:
        thousand_word(number)
    elif l<=9 and l>=7:
        million_word(number)
    else:
        billion_word(number)

word_=" ".join(word_form)
print(word_)