import crontab
from crontab import CronTab

print(crontab.__file__)

# cron = CronTab(user=True)
# job = cron.new(command='echo "Hello from cron" >> /tmp/cron_output.txt', comment='test job')
# job.minute.every(1)
# cron.write()
# print("Cron job created.")