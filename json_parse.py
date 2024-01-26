import pandas as pd
import json

region_name, sold_count, sale_amount = [], [], []
list_col = ('region_name','sold_count','sale_amount')

#Function to parse json file
def parse_json(json_file,file_name):
    data = json.load(open(json_file))
    for i in data['data']['total_info']:
        region_name.append(i['region_name'])
        sold_count.append(i['sold_count'])
        sale_amount.append(i['sale_amount'])
    
    df = pd.DataFrame(list(zip(region_name,sold_count,sale_amount)),
                      columns = list_col)
    df.to_excel('{}.xlsx'.format(file_name),index=False)


parse_json(input('json file: '), input('file name: '))