print("Welcome! to mad libs generator\nlet's build a story")
option='no'
while option=='yes'or'Yes'or'YES':
    noun1=input("input a noun: ")
    noun3=input("input a noun: ")
    noun2=input("input a noun: ")
    verb1=input("input a verb (a present participle): ")
    adjective=input("input an adjective: ")
    verb2=input("input a verb (present tense): ")
    noun4=input("input a noun: ")
    verb3=input("input a verb (present tense): ")
    print("here is your story\n")
    print(noun1,"struck a meteor, unaware that it would lead to",noun3,".\n",noun2,"kept following it, in the hope of ",verb1,noun1,"but everything was",adjective,".\nSoon,",noun2,"realized that they could",verb2,"the inhabitants of planet",noun4,",to",verb3,noun1,"back.")
    option=input("do you wish to make your story again: ")
    print(option)
