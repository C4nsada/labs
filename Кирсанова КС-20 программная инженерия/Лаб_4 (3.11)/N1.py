from sys import exit
file_output = open("N1_output.txt","w")
try: 
    file = open("N1_input.txt","r", encoding="utf-8")
except BaseException:
    file_output.write("входной файл не обнаружен")
    file_output.close()
    exit()
    
student_info = [0]*3

data = file.readline()
i = 0

while data != "":
    data = data.split()
    if (data[2] == "хорошист" or data[2] == "отличник"):
        file_output.write(data[0]+" ")
        i += 1
    data = file.readline()
    
if i: 
    file_output.write("- молодец.\n") if i == 1 else file_output.write(" - молодцы.\n")
else:
    file_output.write("Все дебилы.\n")

file.close()

file = open("input.txt","r", encoding="utf-8")
data = file.readline()

j =0

if i:
    while data != "":
        data = data.split()
        if data[1] == "мужчина" and (data[2] == "хорошист" or data[2] == "отличник"):
            file_output.write(data[0]+" ")
            j += 1
        data = file.readline()    
        
    if j:
        file_output.write("- мужчина молодец.") if j ==1 else file_output.write("- мужчины молодцы.")
        
    else: 
        file_output.write("Мужчин молодцов нет.")
        
file.close()
file_output.close()

