#!/usr/bin/python

# This work has been released into the public domain by Pablo Duboue.

import yaml
import sys
from zlib import adler32
import re

template = yaml.load(open(sys.argv[1]))

pattern = re.compile("\\$[A-Za-z0-9]+")

for utt in template['utterances']:
    # find which fillers are involved in the utterance
    m = pattern.search(utt)
    prev = 0
    parsed = list()
    while m is not None:
        if prev < m.start():
            parsed.append( (None, utt[prev:m.start()]) )
        parsed.append( (utt[(m.start()+1):m.end()], None) )
        prev = m.end()
        m = pattern.search(utt, prev)
    if prev != len(utt):
        parsed.append( ( None, utt[prev:len(utt)] ) )
    
    seen = set()
    sys.stderr.write(utt + "\n")

    vars = map(lambda t:t[0], filter(lambda t:t[1] is None, parsed))
    counters = map(lambda v:len(template['fillers'][v]) - 1, vars) # count backwards, easy to check

    while True:
        to_print = ""
        var_idx = 0
        for part in parsed:
            if part[0] is None:
                to_print += part[1]
            else:
                to_print += str(template['fillers'][part[0]][counters[var_idx]])
                var_idx += 1
        print to_print

        # decrease
        var_idx = 0
        while var_idx < len(counters) and counters[var_idx] == 0:
            counters[var_idx] = len(template['fillers'][vars[var_idx]]) - 1
            var_idx += 1
        if var_idx == len(counters):
           break
        counters[var_idx] -= 1




