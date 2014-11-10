testcases = int(raw_input());
for y in range(1,testcases+1):
	number_of_stations = int(raw_input());
	stations ={};
	for x in range(number_of_stations*2):
		if (x%2==0):
			src = raw_input();
		else:
			dest = raw_input();
			stations[src]=dest
	for x in stations.keys():
		if x not in stations.values():
			source = x ;
			break;
	for x in stations.values():
		if x not in stations.keys():
			destination = x
	print "Case #%s:"%(y),
	while stations.has_key(source):
		print source+"-"+stations[source],
		source = stations[source]
	print ""
