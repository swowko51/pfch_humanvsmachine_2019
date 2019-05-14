import json

with open('test2.json') as json_file:  
    data = json.load(json_file)
    
    for p in data:
    	if p['imageid'] == '63.201.1':
    		print(p['desc'])