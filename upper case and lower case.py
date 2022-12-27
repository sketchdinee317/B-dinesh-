def string_test(s):
    x={"UPPER_CASE":0, "LOWER_CASE":0}
    for i in s:
        if i.isupper():
           x["UPPER_CASE"]+=1
        elif i.islower():
           x["LOWER_CASE"]+=1
        else:
            pass
    print ("No. of Upper case characters : ", x["UPPER_CASE"])
    print ("No. of Lower case Characters : ", x["LOWER_CASE"])

string_test('The quick Brown Fox')
