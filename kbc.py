questions =[

 ["which language is used to create fb?", "python","java","C++","php", "None",4
],


["which language is used to create fb?", "python","java","C++","php", "None",4
],


["which language is used to create fb?", "python","java","C++","php", "None",4
],


["which language is used to create fb?", "python","java","C++","php", "None",4
 ],
]

levels =[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000]
 
money = 0
for i in range(len(questions)):
    question = questions[i]
    print(f"question for RS.{levels[i]}")
    print(f"a.{question[1]}     b.{question[2]}")
    print(f"c.{question[3]}    d.{question[4]}")
    reply = int(input("enter your answer (1-4)"))
    if(reply == question[6]):
        print(f"congratulation you won RS.{levels[i]}")
        if(i == 4):
            money = 10000
        elif(i == 9):
            money = 320000
        elif(i == 14):
            money = 10000000
    
    else:
        print("soory worng answer")
        break 