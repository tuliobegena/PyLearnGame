print('''Hey! This is Jorge!\n_____________________________
|                  _        |
|                 /"\       |
|                /o o\      |
|           _\/  \   / \/_  |
|            \\._/  /_.//    |
|            `--,  ,----'   |
|              /   /        |
|    ^        /    \        |
|   /|       (      )       |
|  / |     ,__\    /__,     |
|  \ \   _//---,  ,--\\_     |
|   \ \   /\  /  /   /\     |
|    \ \.___,/  /           |
|     \.______,/            |
|                           |
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~''')
print("Jorge is hungry, buy you can help him!"
      "\nIt's simple: each answer you get right, Jorge wins a delicious fly."
      "\nPrepare yourself, answer each question with a, b, c or d and don't let Jorge starve!"
      "\nSince Jorge wants to fit in with his Pythons cousins, the five questions are about Python.")
first = input("___________________________________________________________________"
              "\n|  1. What will be the value of the following Python expression?  |"
              "\n|  4 + 3 % 5                                                      |"
              "\n|  a) 7                                                           |"
              "\n|  b) 2                                                           |"
              "\n|  c) 4                                                           |"
              "\n|  d) 1                                                           |"
              "\n|_________________________________________________________________|"
              ""
              "\nYour answer:")
score = 0
if first == "a":
    score += 1
    print(f"The answer is a. Congratulations! You are {score}/5 AND Jorge won a fly!")
else:
    print("The correct answer is a: The order of precedence is: %, +."
          "\nHence the expression above, on simplification results in 4 + 3 = 7."
          "\nHence the result is 7. ")
    print(f"You are {score}/5. Jorge needs food.")

second = input("___________________________________________________"
              "\n|  2. What is the order of precedence in python?  |"
              "\n|  a) **, (), *, /, +, -                          |"
              "\n|  b) **, (), /, *, +, -                          |"
              "\n|  c) (), **, *, /, -, +                          |"
              "\n|  d) (), **, *, /, +, -                          |"
              "\n|_________________________________________________|"
              ""
              "\nYour answer:")
if second == "d":
    score += 1
    print(f"The answer is d. Congratulations! You are {score}/5 AND Jorge won a fly!")
else:
    print("The correct answer is d: gor order of precedence,"
          "\njust remember this PEMDAS (similar to BODMAS).")
    print(f"You are {score}/5. Jorge needs food.")

third = input("_________________________________________________________________"
              "\n|  3. What are the values of the following Python expressions?  |"
              "\n|  a) 512, 64, 512                                              |"
              "\n|  b) 512, 512, 512                                             |"
              "\n|  c) 64, 512, 64                                               |"
              "\n|  d) 64, 64, 64                                                |"
              "\n|_______________________________________________________________|"
              ""
              "\nYour answer:")
if third == "a":
    score += 1
    print(f"The answer is a. Congratulations! You are {score}/5 AND Jorge won a fly!")
else:
    print("The correct answer is a: Expression 1 is evaluated as: 2**9, which is equal to 512."
          "\nExpression 2 is evaluated as 8**2, which is equal to 64. The last expression is"
          "\nevaluated as 2**(3**2). This is because the associativity of ** operator is from"
          "\nright to left. Hence the result of the third expression is 512.")
    print(f"You are {score}/5. Jorge needs food.")

fourth = input("__________________________________________________________________"
              "\n|  4. What will be the output of the following Python function?  |"
              "\n|  a) -4                                                         |"
              "\n|  b) -3                                                         |"
              "\n|  c) 2                                                          |"
              "\n|  d) False                                                      |"
              "\n|________________________________________________________________|"
              ""
              "\nYour answer:")
if fourth == "d":
    score += 1
    print(f"The answer is d. Congratulations! You are {score}/5 AND Jorge won a fly!")
else:
    print("The correct answer is d: the function max() is being used to find the"
          "\nmaximum value from among -3, -4 and false. Since false amounts to the value zero,"
          "\nhence we are left with min(0, 2, 7) Hence the output is 0 (false).")
    print(f"You are {score}/5. Jorge needs food.")

fifth = input("__________________________________ ___________________________"
               "\n|  5. What will be the output of the following Python code?  |"
               "\n|  a) 1                                                      |"
               "\n|  b) 1 2                                                    |"
               "\n|  c) 1 3 5 7 9 11 ...                                       |"
               "\n|  d) 1 2 3 4 5 6 ...                                        |"
               "\n|____________________________________________________________|"
               ""
               "\nYour answer:")
if fifth == "c":
    score += 1
    print(f"The answer is c. Congratulations! You are {score}/5 AND Jorge won a fly!")
else:
    print("The correct answer is c: the loop does not terminate since i is never an even number.")
    print(f"You are {score}/5. Jorge needs food.")

if score == 5:
    print("___________________________________________________________________"
          "\n5 outta 5!! Congratulations! You fed Jorge very well! Right, Jorge?")
    print('''                    .-._   _ _ _ _ _ _ _ _
             .-''-.__.-'00  '-' ' ' ' ' ' ' ' '-.
             '.___ '    .   .--_'-' '-' '-' _'-' '._
              V: V 'vv-'   '_   '.       .'  _..' '.'.
                '=.____.=_.--'   :_.__.__:_   '.   : :
                        (((____.-'        '-.  /   : :
     HMMMMM... Riiiiight!                 (((-'\ .' /
                                        _____..'  .'
                                       '-._____.-')''')
elif score == 3 or score == 4:
    print(f"_____________________________________________________________________________________"
          f"\nVery nice! You fed Jorge a little {score}/5. At least he won't die due some mistakes.")
    print('''_____________________________
|                  _        |
| TY, human.      /"\       |
|                /o o\      |
|           _\/  \   / \/_  |
|            \\._/  /_.//    |
|            `--,  ,----'   |
|              /   /        |
|    ^        /    \        |
|   /|       (      )       |
|  / |     ,__\    /__,     |
|  \ \   _//---,  ,--\\_     |
|   \ \   /\  /  /   /\     |
|    \ \.___,/  /           |
|     \.______,/            |
|                           |
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~''')
else:
    print(f"_______________________________________________________________"
          f"\nOh no! You got {score}/5. Jorge still needs food, Right, Jorge?"
          f"\n..."
          f"\nJorge? Jorge?!")
    print('''_____________________________
|                  _        |
|                 /"\       |
|                /x x\      |
|  ...      _\/  \   / \/_  |             %%% %%%%%%%            |#|
|            \\._/  /_.//    |          %%%% %%%%%%%%%%%        |#|####
|            `--,  ,----'   |         %%%%% %         %%%       |#|=#####
|              /   /        |        %%%%% %   @    @   %%      | | ==####
|    ^        /    \        |       %%%%%% % (_  ()  )  %%     | |    ===##
|   /|       (      )       |       %%  %%% %  \_    | %%      | |       =##
|  / |     ,__\    /__,     |       %    %%%% %  u^uuu %%     | |         ==#
|  \ \   _//---,  ,--\\_     |            %%%% %%%%%%%%%      | |           V
|   \ \   /\  /  /   /\     |
|    \ \.___,/  /           |           MUAHAHAHAHAHAHAHAHA!
|     \.______,/            |
|                           |
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~''')

input("Did you have fun playing?")
print("\nYou can find me searching for Túlio Begena on GitHub or LinkedIn")
print("\nThe questions, answers and explanations are from https://www.sanfoundry.com."
      "\nMake sure to reach it if you want to really practice with multiple choice questions & answers"
      "\nabout a lot of subjects, including programming, science, and school subjects.")