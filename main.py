import pathlib

def meta_data():
    currentDirectory = pathlib.Path('.\\files_dir')
    files = {}
    for currentFile in currentDirectory.iterdir():
        with open(currentFile, 'r', encoding="utf-8") as f:
            file = f.readlines()
        files[currentFile] = len(file)
    list_files = list(files.items())
    list_files.sort(key=lambda i: i[1])
    with open(str(currentDirectory)+'\\result.txt', 'w', encoding="utf-8") as file_result:
        for file in list_files:
            with open(file[0], 'r', encoding="utf-8") as f:
                file_name = str(file[0])
                file_name = file_name[file_name.find('\\') + 1:len(file_name)]
                file_result.write(file_name + '\n')
                file_result.write(str(file[1]) + '\n')
                for line in f:
                    if line.find('\n') > 0:
                        file_result.write(line)
                    else:
                        file_result.write(line + '\n')

meta_data()