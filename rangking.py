def process_data(data):
    # Variable untuk menyimpan hasil akhir
    allPrediction = {}

    # Iterasi melalui data asli
    for item in data:
        name = item['name']
        if name in allPrediction:
            allPrediction[name]['accuration'] += item['accuration']
            allPrediction[name]['count'] += item['count']
        else:
            allPrediction[name] = {
                'name': name,
                'accuration': item['accuration'],
                'count': item['count']
            }

    # Konversi hasil akhir kembali ke dalam list
    allPrediction_list = list(allPrediction.values())

    # Mencari item dengan count tertinggi dan jika count sama, pilih yang memiliki accuration tertinggi
    best_prediction = max(allPrediction_list, key=lambda x: (x['count'], x['accuration']))

    return best_prediction