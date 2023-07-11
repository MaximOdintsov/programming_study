txt = 'files.txt'
json = 'departments.json'

with open(txt, 'r') as f:
    files = f.read().split('\n')    

    with open(json, 'a') as d:
        d.write('{\n')

    file_ln = len(files)
    for file in files:
        file = file.strip()

        if file:
            file_ln -= 1

            file = file.replace('"', r'\"')

            with open(json, 'a') as d:
                d.write(f'    "{file}": ')
                d.write('"itb"') if 'ИТБ' in file else d.write('"tkb"')

                if file_ln > 0:
                    d.write(',\n')
    
    with open(json, 'a') as d:
        d.write('\n}')