import os

filepath = 'img'
i = 0
for item in os.listdir(filepath):
    # print(item, type(item))
    # print(item[0:8])
    # print(os.path.join(filepath, item))
    os.rename(os.path.join(filepath, item), os.path.join(filepath, (item[0:8] +'.jpg')))
    i += 1

