from datetime import datetime, timedelta

yesterday = datetime.now() - timedelta(days=1)
today = datetime.now()
tomorrow = datetime.now() + timedelta(days=1)
print(yesterday.date(), 'Yesterday')
print(today.date(), 'Today')
print(tomorrow.date(), 'Tomorrow')