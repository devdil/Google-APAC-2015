testcases = int(raw_input());
for y in range(1,testcases+1):
	number_of_stations = int(raw_input());
	stations ={};
	for x in range(number_of_stations*2):
		stations[raw_input()] = raw_input()
	for x in stations.keys():
		if x not in stations.values():
			source = x ;
			break;
	print "Case #%s:"%(y),
	while stations.has_key(source):
		print source+"-"+stations[source],
		source = stations[source]
	print ""
