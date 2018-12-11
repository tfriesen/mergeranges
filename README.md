# mergeranges
Python script for merging IP ranges

Ranges (currently) must be expressed as 1.1.1.0-1.1.2.255, for example, and need not be sorted. CIDRs are not currently supported, but adding them would not be hard. Output is in same format.

A couple of different techniques are explored in the script. The uncommented one is generally the fastest and most efficient.


## countips

Python script for counting IPs in a range expressed in the format 1.1.1.0-1.1.2.255.
