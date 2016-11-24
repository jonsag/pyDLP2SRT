#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Encoding: UTF-8

import getopt, sys, os

from misc import onError, usage

##### handle arguments #####
try:
    myopts, args = getopt.getopt(sys.argv[1:], 'i:vh' ,
                                 ['infile=', 
                                  'verbose', 
                                  'help'])

except getopt.GetoptError as e:
    onError(1, str(e))

if len(sys.argv) == 1:  # no options passed
    onError(2, "No options given")
    
inFile = ""
    
for option, argument in myopts:
    if option in ('-i', '--infile'):
        inFile = argument
    if option in ('-v', '--verbose'):
        verbose = True
    elif option in ('-h', '--help'):
        usage(0)
        
if not inFile:
    onError(3, "No infile given")
if not os.path.isfile(inFile):
    onError(4, "%s does not exist" % inFile)
elif os.path.islink(inFile):
    onError(5, "%s is a link" % inFile)
    
