import json

if __name__ == '__main__':
    data = [{'a':1,'b':2,'c':3}]
    jsondata = json.dumps(data)
    print jsondata
    pr = json.loads(jsondata)
    print pr

