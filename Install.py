import os

print("Установка библиотек")
os.system("pip3 install --upgrade pip")
bib = ["tk", "colorama", "bs4", "termcolor", "Label", "colored", "requests"]
for i in range(len(bib)):
    print("Установка "+bib[i]+"...\033[0m")
    os.system("pip3 install "+bib[i])
os.system('clear')
print("Установка завершена!")
