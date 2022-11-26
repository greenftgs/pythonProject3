import os

all_files = os.listdir('C:/Users/Gospartner/PycharmProjects/pythonProject3/venv/txt')
# print(all_files)

new_file = []
file_text = ''

for i in all_files:
    with open(i) as temp_file:
        lines = temp_file.readlines()
        new_file.append([i, len(lines), lines])

def sort_len(e):
    return e[1]

new_file = sorted(new_file, key=sort_len)

for i in range(len(new_file)):
    file_text += new_file[i][0] + '\n'
    file_text += str(new_file[i][1]) + '\n'
    file_text += ''.join(new_file[i][2]) + '\n'

with open('new_file.txt', 'w') as f:
    f.write(file_text)