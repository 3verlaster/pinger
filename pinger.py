import os
from time import sleep

print("IP Pinger v1.2")
print("Author: 3verlaster")


ipping = input("Введите айпи, который хотите пингануть: ")
packets = input("Введите какое количество пакетов вы хотите отправить: ")
args = input("Введите аргументы (Можете оставить поле пустым): ")

if args == "-t":
	print("Внимание! Сейчас пакеты будут отправлятся до нажатия CTRL+C. Потому что аргумент -t не совместим с -n")

os.system('ping -n' + ' '+ packets + ' ' + ipping + ' ' + args)

os.system("PAUSE")