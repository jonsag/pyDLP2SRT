#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Encoding: UTF-8

import xml.etree.ElementTree as ET

from misc import onError, printInfo1

def readFile(inFile, verbose):
    with open(inFile, 'r') as myFile:
        DLPFile=myFile.read()
    
    if verbose:
        print DLPFile
    
    readXML(DLPFile, verbose)
    
def readXML(xmlCode, verbose):
    print
    
    try:
        xmlRoot = ET.fromstring(xmlCode)
    except:
        onError(6, "Not a valid XML")
    else:
        printInfo1("XML is valid")
    
    handleXML(xmlRoot, verbose)
            
def handleXML(xmlRoot, verbose):
    
    for xmlChild in xmlRoot:
        
        if verbose:
            print "%s: %s" % (xmlChild.tag, xmlChild.text)
        
        if 'language' in xmlChild.tag.lower():
            language = xmlChild.text
            printInfo1("\nLanguage: %s" % language)
            
        if 'font' in xmlChild.tag.lower():
            print "Here comes the subs"
            
            print xmlChild
            for line in xmlChild:
                
                if 'subtitle' in line.tag.lower():
                    print line.attrib['SpotNumber']
                    print "%s --> %s" % (line.attrib['TimeIn'], line.attrib['TimeOut'])
                    
                    for text in line:
                        if 'text' in text.tag.lower():
                            print text.text
                    
                    print
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
    
    