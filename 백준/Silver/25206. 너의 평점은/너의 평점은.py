sum_mul = 0
sum_credit = 0

for _ in range(20) :
    subject, credit, grade = input().split()
    credit = float(credit)
    if grade == 'A+' : sum_mul += credit * 4.5; sum_credit += credit
    elif grade == 'A0' : sum_mul += credit * 4.0; sum_credit += credit 
    elif grade == 'B+' : sum_mul += credit * 3.5; sum_credit += credit
    elif grade == 'B0' : sum_mul += credit * 3.0; sum_credit += credit
    elif grade == 'C+' : sum_mul += credit * 2.5; sum_credit += credit
    elif grade == 'C0' : sum_mul += credit * 2.0; sum_credit += credit
    elif grade == 'D+' : sum_mul += credit * 1.5; sum_credit += credit
    elif grade == 'D0' : sum_mul += credit * 1.0; sum_credit += credit
    elif grade == 'F' : sum_mul += credit * 0.0; sum_credit += credit
    else : pass

print('%.6f' % (sum_mul / sum_credit))