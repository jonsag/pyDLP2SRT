#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Encoding: UTF-8

import ConfigParser, os, sys

from termcolor import colored
from colorama import init, deinit

config = ConfigParser.ConfigParser()
config.read("%s/config.ini" % os.path.dirname(os.path.realpath(__file__)))  # read config file

scores = int(config.get('decoration', 'scores'))
defaultTextColor = config.get('decoration', 'defaultTextColor')
defaultBackgroundColor = config.get('decoration', 'defaultBackgroundColor')
defaultTextStyle = config.get('decoration', 'defaultTextStyle')

def onError(errorCode, extra):
    printError("\nError %s:" % errorCode)
    if errorCode in (1, 2, 3,4 ,5):
        printError(extra)
        usage(errorCode)
    elif errorCode == 6:
        printError(extra)
        sys.exit(errorCode)
    else:
        printError("Unkown")
        sys.exit(errorCode)
        
def usage(exitCode):
    printInfo1("\nUsage:")
    printScores()
    printInfo1("%s -f <infile>" % sys.argv[0])
    printInfo1("        Set <infile> to be converted to .srt")
    printInfo1("\n%s -h" % sys.argv[0])
    printInfo1("    Prints this")
    printInfo1("\nOptions:")
    printScores()
    printInfo1("    -v verboses output")
    print
    sys.exit(exitCode)
    
def printDefault(text):
    textColor = defaultTextColor
    backgroundColor = defaultBackgroundColor
    textStyle = defaultTextStyle
    printMessage(text, textColor, backgroundColor, textStyle)
    
def printInfo1(text):
    textColor = "green"
    backgroundColor = defaultBackgroundColor
    textStyle = defaultTextStyle
    printMessage(text, textColor, backgroundColor, textStyle)
    
def printInfo2(text):
    textColor = "magenta"
    backgroundColor = defaultBackgroundColor
    textStyle = "bold"
    printMessage(text, textColor, backgroundColor, textStyle)
    
def printWarning(text):
    textColor = "yellow"
    backgroundColor = defaultBackgroundColor
    textStyle = "bold"
    printMessage(text, textColor, backgroundColor, textStyle)
    
def printError(text):
    textColor = "red"
    backgroundColor = defaultBackgroundColor
    textStyle = "bold"
    printMessage(text, textColor, backgroundColor, textStyle)
    
def printScores():
    printInfo1("-" * scores)

def printMessage(text, textColor, backgroundColor, textStyle):
    init()
    
    if textColor == "default":        
        if backgroundColor == "default":
            if textStyle == "default":
                print (colored(text))
            else:
                print (colored(text, attrs=[textStyle]))
        else:
            if textStyle == "default":
                print (colored(text, "on_%s" % backgroundColor))
            else:
                print (colored(text, "on_%s" % backgroundColor, attrs=[textStyle]))
    else:
        if backgroundColor == "default":
            if textStyle == "default":
                print (colored(text, textColor.lower()))
            else:
                print (colored(text, textColor.lower(), attrs=[textStyle]))
        else:
            if textStyle == "default":
                print (colored(text, textColor.lower(), "on_%s" % backgroundColor))
            else:
                print (colored(text, textColor.lower(), "on_%s" % backgroundColor, attrs=[textStyle]))
        

    deinit()
    
