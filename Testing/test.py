import psutil

# cpu = psutil.cpu_percent(interval=1, percpu=True)
#
print(psutil.cpu_count())

all_users = psutil.users()
for user in all_users:
    print user
