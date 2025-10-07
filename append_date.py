from datetime import datetime

today = datetime.now().strftime('%Y-%m-%d')
with open('dates.txt', 'a', encoding='utf-8') as f:
    f.write(today + '\n')

