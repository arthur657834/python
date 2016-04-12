import json
 
obj = [[1,2,3],123,123.123,'abc',{'key1':(1,2,3),'key2':(4,5,6)}]
encodedjson = json.dumps(obj)
print json.dumps(obj,sort_keys=True,indent=4,separators=(',',':'))

print repr(obj)
print encodedjson

decodejson = json.loads(encodedjson)
print type(decodejson)
print "---------------"
print decodejson[0][0]
print decodejson[1]
print decodejson[4]['key1']
print decodejson

obj1={'key1':(1,2,3),'key2':(4,5,6)}
decodejson1 = json.loads(json.dumps(obj1))
print "---------------------"
print decodejson1
print decodejson1['key1']
