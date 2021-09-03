from csv import DictWriter
import json
from pathlib import Path

jsonpath = Path('Data/Southbank-metadata-19-08-2021.json')
csvfile = Path('Data/Southbank-metadata-19-08-2021.csv')
with open(jsonpath, 'r') as inp, open(csvfile, 'w', newline='') as outp:
    # writer = DictWriter(outp, fieldnames=['Id', 'Filename', 'TimeStamp',
    #                                       'FrameNumber', 'DateTime', 'Confidence',
    #                                       'XMax', 'YMax', 'XMin', 'YMin', 'PeopleCount'])
    writer = DictWriter(outp, fieldnames=['ts', 'device_id', 'people_count'])
    writer.writeheader()
    for line in inp:
        row = json.loads(line)
        writer.writerow(row)