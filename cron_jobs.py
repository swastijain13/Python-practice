from crontab import CronTab

cron = CronTab(user=True)

job = cron.new(command='python /read_json.py')

job.setall('0 3 * * *') #run everyday at 3 a.m

cron.write()