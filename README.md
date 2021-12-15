# SNMP-Agent

Write a script to probe the an SNMP agent and find the rate of change for several counters between successive probes/ samples. The rate calculated for each counter/OID should be displayed on the console, one line for each calculated rate, the output format will be described in detail in 'output format'. Futhermore, as the only requirement on the OIDs is that they are of the type COUNTER, this means that there are both 32 and 64 bit versions of counters. Your solution should handle both counter types, and in the case that a counter wraps (ie goes from a high number to a low number), your solution should address/rectify (if its possible). The solution needs also to handle that an SNMP agent restarts (i.e. the sysUpTime OID becomes less than it was before, ie. it starts counting from zero), and timeouts, i.e. the device does not respond to your request in time. It will be tested that your solution maintains the requested sampling frequency (i.e. the requests from your solution should be sent so that the sampling frequency is maintained, irrespectively if the device has responded or not). 

The script will be invoked as follows:
prober <Agent IP:port:community> <sample frequency> <samples> <OID1> <OID2> …….. <OIDn> where, IP, port and community are agent details, OIDn are the OIDs to be probed (they are absolute, cf. IF-MIB::ifInOctets.2 for interface 2, or 1.3.6.1.2.1.2.2.1.10.2 [1]) Sample frequency  (Fs) is the sampling frequency expressed in Hz, you should handle between 10 and 0.1 Hz. Samples (N) is the number of successful samples the solution should do before terminating, hence the value should be greater or equal to 2. If the value is -1 that means run forever (until CTRL-C is pressed, or the app is terminated in someway). 
  
Output format

The output from the script _MUST_ be as follows:

Sample time | OID1 | OID2 | .... | OIDn

 

Sample time: Timestamp of the last sample, in UNIX time (seconds). 

OID*: Rate of OID* between the last two successful samples

 

As an example:

1504083911  | 2124 | 819 | 0 | 281761 
1504083912  | 2471 | 819 | 110 | 450782 
1504083913  | 1904 | 819 | 2000 | 325448   
  
