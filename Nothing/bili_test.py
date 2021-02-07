import requests
import csv
import re

a = 'https://api.bilibili.com/x/relation/stat?vmid='

# with open('UID_and_FOLLOWER.csv', 'a', newline="") as f:
#     writer = csv.writer(f)
#     writer.writerow(('UID', 'Followers'))
# f.close()

for i in range(2266, 1000000):
    url = a + str(i)
    text = requests.get(url).text
    fol = int(re.search(r'follower":(.*?)}', text).group(1))
    if fol >= 50000:
        with open('UID_and_FOLLOWER.csv', 'a', newline="") as f:
            writer = csv.writer(f)
            writer.writerow((str(i), str(fol)))
        f.close()
        # print(str(i))
    else:
        print(str(i) +"号太菜鸡,抛弃!")
