def write_file(file_name, file_content):
    with open(f'{file_name}.txt', mode='w') as file_name:
        file_name.write(file_content)

def append_file(file_name, append_content):
    with open(f'{file_name}.txt', mode='a') as file_name:
        file_name.write(append_content)

def read_file(file_name):
    # with open(f'{file_name}.txt',mode='r') as file_name:
    #     file_name.read()
    file_name = open(f'{file_name}.txt')
    return file_name.read()
    file_name.close()


write_file(file_name="logfile", file_content="Log 1: 5 bananas added" )
append_file(file_name="logfile", append_content="Log 2: 3 bananas subtracted")

print(read_file(file_name="logfile"))