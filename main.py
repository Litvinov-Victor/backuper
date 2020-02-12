import os
import zipfile

helloMessage = 'Программа архивации ваших проектов v 0.1. Введите команду start для начала работы :'
print(helloMessage)
globalSet = input('> ')
if globalSet == 'start':
    pathName = input('Введите путь до папки : ')
    endArhiveName = input('Ведите путь и назание конечного архива : ')
else:
    print('Команда не выбрана > введите команду :')
    globalSet = input('> ')

endtotal = zipfile.ZipFile(endArhiveName, 'w')
for folder, subfolders, files in os.walk(pathName):
    for file in files:
        endtotal.write(os.path.join(folder, file),
                          os.path.relpath(os.path.join(folder, file), pathName),
                          compress_type=zipfile.ZIP_DEFLATED)
endtotal.close()
print('> Архив создан успешно! путь до архива: ' + endArhiveName)