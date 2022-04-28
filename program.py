import yaml 

with open('settings.yaml','a+',encoding='utf-8') as file:
    readFile = yaml.safe_load(file)

    newDict = {
        'firstKey':"firstObj",
        'secondKey':4,
        'thirdKey': ['one',2,True]
    }


    outputs = yaml.dump(newDict,file)
    print(outputs)

