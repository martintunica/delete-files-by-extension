import os

dir_name = r'C:\rout\to\files'
test = os.listdir(dir_name)
for i in test:
    print('one item found')

for item in test:
    if item.endswith(".txt"): #.txt . json etc. extensions you want to delete
        os.remove(os.path.join(dir_name, item))

print('done!')
