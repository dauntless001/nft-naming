import csv, hashlib, json

'''Output CSV File'''
OUTPUT_FILE = 'output/output-nft-naming.csv'
f = open(OUTPUT_FILE, 'w')
writer = csv.writer(f)
writer.writerow(['S/N', 'Filename','Name','Description','Gender','UUID', 'Output File Name'])

team = ''

with open('csv/hng-teams.csv', 'r') as csv_file:
    csv_readr = csv.reader(csv_file, delimiter=',')
    # Skip First Line that contains Column title
    next(csv_readr)
    data = [a for a in csv_readr]  
    for row in data:
        if row[0].startswith('TEAM'):
            team = row[0]
        ''''''
        if row[1] and row[2]:
            sn = row[0]
            file_name = row[1]
            name = row[2]
            uuid = row[5]
            gender = row[4]
            description = row[3]
            nft = {
                'format' : 'CHIP-0007',
                'id' : uuid,
                'name' : name.replace('-',' ').title(),
                'filename': file_name,
                'description' : description,
                'minting_tool' : f'{team} SuperMinter',
                'sensitive_content' : False,
                'series_number' : sn,
                'series_total' : data[-1][0],
                'gender' : gender,
                'collection' : {
                    'name' : 'Zuri Hng NFT Collection',
                    'id' : '24f5ff82-a2f1-494e-8be5-69f1d5e42d15'
                }
            }
            jsonObj = json.dumps(nft, indent=4)
            with open(f'json/{file_name}.json', 'w') as output:
                output.write(jsonObj)
            output.close()
            hashString = hashlib.sha256(jsonObj.encode()).hexdigest()
            row.append(f'{file_name}.{hashString}.csv')
            writer.writerow(row)

f.close()
        
