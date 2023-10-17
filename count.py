import json
import datetime

infile = 'result.json'
with open(infile, 'r', encoding='utf-8') as f:
    chat = json.load(f)

users = []
users_count = {}
user = ''

start_date = input('Start date as dd.mm.yyyy HH:MM:SS: ')
end_date = input('End date as dd.mm.yyyy HH:MM:SS: ')

begin = datetime.datetime.strptime(start_date,"%d.%m.%Y %H:%M:%S")
end = datetime.datetime.strptime(end_date,"%d.%m.%Y %H:%M:%S")

def count_users(user_list, user_dict):
    for i in user_list:
        if i in user_dict:
            user_dict[i] += 1
        else:
            user_dict[i] = 1


for message in chat['messages']:
    if begin <= datetime.datetime.fromtimestamp(int(message['date_unixtime'])) <= end:
        if 'from_id' in message:
            user = message['from_id'] + ',' + str(message['from'])
            users.append(user)

count_users(users, users_count)
result = dict(sorted(users_count.items(),
                     key=lambda x: x[1],
                     reverse=True))

outfile = 'sorted.csv'
with open(outfile, 'w', encoding='utf8') as file:
    for key, value in result.items():
        file.write(f'{key},{value},\n')
