# tasks/task5.py

def solve():
# Ниже пишите решение задачи

    n = int(input().strip())
    n %= 86400  
    h = n // 3600
    m = (n % 3600) // 60
    s = n % 60
    
    print(h,':',m//10,m%10,':',s//10,s%10,sep='')
   
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()