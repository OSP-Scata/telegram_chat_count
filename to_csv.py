import json
import datetime

infile = 'result.json'
with open(infile, 'r', encoding='utf-8') as f:
    chat = json.load(f)

comments = []

for message in chat['messages']:
        if 'from_id' in message:
            comment = str(message["date"]) + ',' + str(message['from_id']) + ',' \
                      + str(message['from']) + ',' + str(message['text'])
            comments.append(comment)

outfile = 'result.csv'
with open(outfile, 'w', encoding='utf8') as file:
    for comment in comments:
        file.write(f'{comment},\n')
