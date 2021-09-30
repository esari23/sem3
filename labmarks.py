#1. Weekly Continuous Assessment marks are given to each student based on the student's lab performance. Maximum CA marks = 10, minimum CA Marks to clear the exam= 5
#2. Maximum Internal Lab mark = 30, Minimum Internal lab mark to clear the exam= 10
#3. Maximum External Lab Mark = 50, Minimum External Lab Mark to clear the exam.= 25
#4. Maximum Marks allocated for viva-voce = 10. Even student gets zero, in this category, it will not have any effect on the overall result.
#Students must get 40 marks  minimum to clear the lab exam overall. 
mi = int(input())
me = int(input())
vv = int(input())

if (mi<10) or (me<25):
    print("fail")
elif ((mi+me+vv)<40):
    print("FAIL")
else:
    print(mi+me+vv)
    