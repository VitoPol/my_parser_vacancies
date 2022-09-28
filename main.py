import requests
import json
from classes import *


list_ = HH.get_request(HH, search_text="python")
for i in list_:
    print(i, '\n')
print(len(list_))
