def get_values(lod,k):
  list = []
  for aDict in lod:
    q = aDict.get(k,0)
    if q not in list:
      list.append(q)
  return list

def sum_death_matches(lod, tgt, k, v):
  count = 0
  for i in lod:
    if i[k] == v:
      count += int(i[tgt])
  return count

def sum_death_matches_specific(lod, tgt, k, v, k2, v2):
  count = 0
  for i in lod:
    if i.get(k,0) == v and i.get(k2,0) == v2:
      count += i[tgt]
  return count

def dict_from_values(lod, k):
  Dict = {}
  for i in lod:
    q = i.get(k,0)
    if k in i:
      Dict[q]=0
  return Dict