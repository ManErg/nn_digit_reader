import json

def jsonDefault(obj):
    """
    Convert an object into a JSON compatible object.

    Is never called but passed to json method dump as:
    json.dump(arg, default = jsonDefault)
    Credit to https://pythontips.com for function.
    """
    if isinstance(obj, set):    #When applicable, return a list of object members
        return list(obj)        #Otherwise, call the __dict__ magic method, this
    return obj.__dict__         #will return a dict using the member names as keys


def readJsonFile(jsonFile):
    """Return a dict from a JSON file"""
    with open(jsonFile, 'r') as f:
        result = json.loads(f.read() )
    return result
