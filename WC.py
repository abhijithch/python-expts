    # -*- coding: utf-8 -*-
    """
    Created on Wed Apr 23 08:45:45 2014
    
    @author: abhijith
    """
    import string
    
    flText = open("diamond.txt",'r')
    
    strText = flText.read()
    
    iNC = len(strText)
    
    iNL = len(strText.splitlines())
    
    strWords = string.split(strText)
    
    iWC = len(strWords)
    
    print iNL, iWC, iNC
    
    
    
    
    
