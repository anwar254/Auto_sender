from sender import auto_scheduler

ctnts_list = auto_scheduler.get_contacts()
for list in ctnts_list:

	print(list[0])