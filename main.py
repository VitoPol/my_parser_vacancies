import requests
import json
from classes import *


# list_ = HH.get_request(search_text="python")
# for i in list_:
#     print(i, '\n')
# print(len(list_))


data = Superjob.get_request(search_text="python")
for i in data:
    print(i, '\n')
print(len(data))

