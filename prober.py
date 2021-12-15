#!/usr/bin/python
import sys,time
import easysnmp
import math
from easysnmp import Session
from easysnmp import snmp_get,snmp_walk
Argument=sys.argv[1]
COMMAND=Argument.split(':')
IP_ADDRESS=COMMAND[0]
PORT=COMMAND[1]
Network=COMMAND[2]
FREQUENCY_OF_SAMPLE=float(sys.argv[2])
INTERVALS=int(sys.argv[3])
INTERVALS_TIME=1/FREQUENCY_OF_SAMPLE 
OBJECT_IDENTIFIERS=[]
OLD_OBJECT_IDENTIFIER=[]
NEW_OBJECT_IDENTIFIER=[]
for NUMBER_OBJECT_IDENTIFIER in range(4,len(sys.argv)):
	OBJECT_IDENTIFIERS.append(sys.argv[NUMBER_OBJECT_IDENTIFIER])
OBJECT_IDENTIFIERS.insert(0,'1.3.6.1.2.1.1.3.0')
def easysnmp_prober():
	global OLD_OBJECT_IDENTIFIER, CURR_TIME
	session=Session(hostname=IP_ADDRESS,remote_port=PORT,community='public',version=2,timeout=1,retries=1)
	retaliation=session.get(OBJECT_IDENTIFIERS)
	NEW_OBJECT_IDENTIFIER=[]
	for getter in range(1,len(retaliation)):
		if retaliation[getter].value!='NOSUCHOBJECT' and retaliation[getter].value!='NOSUCHINSTANCE':
			NEW_OBJECT_IDENTIFIER.append(int(retaliation[getter].value))
			
			if count!=0 and len(OLD_OBJECT_IDENTIFIER)>0:
				different_object_identifier=int(NEW_OBJECT_IDENTIFIER[getter-1]) - int(OLD_OBJECT_IDENTIFIER[getter-1])
				different_time=round(PREVIOUS_SAMPLES-CURR_TIME,1)
				SAMPLE_INTERVAL_RATE = int(different_object_identifier / different_time)
				if SAMPLE_INTERVAL_RATE < 0 :
					if retaliation[getter].snmp_type == 'COUNTER32': 
						different_object_identifier = different_object_identifier + 2**32
						print(str(PREVIOUS_SAMPLES) +"|"+ str(different_object_identifier / different_time) +"|")
					elif retaliation[getter].snmp_type == 'COUNTER64':
						different_object_identifier = different_object_identifier + 2**64
						print(str(PREVIOUS_SAMPLES) +"|"+ str(different_object_identifier / different_time) +"|")
				else:
					print(str(PREVIOUS_SAMPLES) +"|"+ str(SAMPLE_INTERVAL_RATE) +"|")

	OLD_OBJECT_IDENTIFIER=NEW_OBJECT_IDENTIFIER
	CURR_TIME=PREVIOUS_SAMPLES
if INTERVALS==-1:
	count=0
	OLD_OBJECT_IDENTIFIER=[]
	while True:
		PREVIOUS_SAMPLES=(time.time())
		easysnmp_prober()
		response_time=(time.time())
		count = count+1
		time.sleep(abs(INTERVALS_TIME - response_time + PREVIOUS_SAMPLES))
else:
	OLD_OBJECT_IDENTIFIER=[]
	for count in range(0,INTERVALS+1):
		PREVIOUS_SAMPLES=(time.time())
		easysnmp_prober()
		response_time=(time.time())
		time.sleep(abs(INTERVALS_TIME - response_time + PREVIOUS_SAMPLES))
		