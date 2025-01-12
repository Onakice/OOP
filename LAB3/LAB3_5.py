# def update_records(record, id, property, value):
#   if id not in record:
#     return record

#   if property != 'tracks' and value != '':
#     record[id].update({property: value})
#   elif property == 'tracks' and 'tracks' not in record[id]:
#     record[id].update({property: [value]})
#   elif property == 'tracks' and value != '':
#     record[id][property].append(value)
#   elif value == '':
#     record[id].pop(property)
#   return record

record_collection = {
  2548: {
      'albumTitle': 'Slippery When Wet',
      'artist': 'Bon Jovi',
      'tracks': ['Let It Rock', 'You Give Love a Bad Name']
  },
  2468: {
      'albumTitle': '1999',
      'artist': 'Prince',
      'tracks': ['1999', 'Little Red Corvette']
  },
  1245: {
      'artist': 'Robert Palmer',
      'tracks': []
  },
  5439: {
      'albumTitle': 'ABBA Gold'
  }
}

def update_records(record, id, property, value):
  if id not in record:
    del record[id][property]

  if property != 'tracks' and value != '':
    record[id].update({property: value})
  elif property == 'tracks' and 'tracks' not in record[id]:
    record[id].update({property: [value]})
  elif property == 'tracks' and value != '':
    record[id][property].append(value)
  elif value == '':
    record[id].pop(property)
  return record

print(update_records(record_collection, 1245, 'tracks', '99999'))
# print(update_records(record_collection, 2468, "tracks", "International Lover"))