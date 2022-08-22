buoy_id = '135'
index_template = [1, 6, 7, 16, 17, 26]
index = []
for i in range(len(buoy_id)) :
    index.append(index_template[int(buoy_id[i])-1])
print(index)