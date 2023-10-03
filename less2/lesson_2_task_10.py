def bank(X, Y):
    account_balance = X
    for _ in range(Y):
        account_balance = account_balance + 0.1 * account_balance
    return account_balance
X = 10000  
Y = 5      
result = bank(X, Y)
print("Сумма на счету спустя {} лет: {}".format(Y, result))