# 攝氏('C')轉換成華氏('F')程式
# 讓使用者輸入 攝氏溫度
# 然後印出 華氏溫度

temp = input('請輸入目前的攝氏溫度: ')
temp = int(temp) #float(temp)
hua_temp = temp * 9 / 5 + 32
print('華氏溫度為', hua_temp)
