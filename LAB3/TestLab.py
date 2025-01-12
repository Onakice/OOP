def update_records(record, id, property, value):
  if id not in record:
    return record

  if property != 'tracks' and value != '':
    record[id].update({property: value})
  elif property == 'tracks' and 'tracks' not in record[id]:
    record[id].update({property: [value]})
  elif property == 'tracks' and value != '':
    record[id][property].append(value)
  elif value == '':
    record[id].pop(property)
  return record