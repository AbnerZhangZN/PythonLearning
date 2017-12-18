print('计算客户的相关金额')
exporeSum = input('客户的敞口:')
duebillSum = input('客户的余额:')
bailSum = input('客户的保证金:')
result = exporeSum - duebillSum + bailSum
print('客户的剩余敞口(敞口-余额+保证金):', result)