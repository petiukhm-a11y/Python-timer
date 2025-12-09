import time
seconds = int(input("Введіть кількість секунд: ")) 
while seconds > 0:
    print(seconds)
    time.sleep(1)    
    seconds = seconds - 1

print("Поїхали!")