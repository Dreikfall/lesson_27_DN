import csv
import json

CSV_ADS = 'datasets/ads.csv'
CSV_CATEGORIES = 'datasets/categories.csv'
json_filename = ('datasets/ads.json', 'datasets/categories.json')


def csv_to_json(csv_name, json_name, model_name):
    mydata = []

    with open(csv_name, encoding='utf-8') as csvfile:
        csv_read = csv.DictReader(csvfile)

        for rows in csv_read:
            if 'Id' in rows:
                pk = int(rows['Id'])
                del rows['Id']
            if 'id' in rows:
                pk = int(rows['id'])
                del rows['id']
            if 'is_published' in rows:
                rows['is_published'] = True if rows['is_published'] == 'TRUE' else False
            if 'price' in rows:
                rows['price'] = int(rows['price'])
            rows = {
                'model': model_name,
                'pk': pk,
                'fields': {**rows},
            }
            mydata.append(rows)

    with open(json_name, 'w', encoding='utf-8') as jsonfile:
        jsonfile.write(json.dumps(mydata, indent=2, ensure_ascii=False))


csv_to_json(CSV_ADS, json_filename[0], 'ads.ad')
csv_to_json(CSV_CATEGORIES, json_filename[1], 'ads.category')
