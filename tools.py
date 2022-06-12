import json



def get_data(filename: str):
    f = open(filename)
    data = json.load(f)
    f.close
    return data




data = get_data('bumps.json')

print('.')