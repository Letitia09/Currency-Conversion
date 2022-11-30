def CurrencyConverter(code,amount):
    code_dict={1:65,2:96,3:67,4:74,5:11}
    if code in code_dict.keys():
        amount=amount*code_dict[code]
    return amount
code=int(input("code:"))
amount=int(input("amount:"))
print(CurrencyConverter(code,amount))  
