import commands
cmd = "hive -S -e 'SELECT * FROM log4jLogs WHERE t4 = \"[ERROR]\";'"
status, output = commands.getstatusoutput(cmd)
if status == 0:
	print output
else:
	print "error"