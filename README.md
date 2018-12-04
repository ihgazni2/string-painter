<!--[TOC]-->

# _spaint_
>__print colorful string in console__

# INSTALL
>__pip3 install spaint__

# USAGE
-----------------------------------------------------------------------

    import spaint.spaint as spaint

## spanpaint    
    #spaint.spanpaint(string,(start1,end1),color1,(start2,end2),color2,...)
    
    spaint.spanpaint("0123456789x",(2,3),'blue',(5,7),'yellow',(9,10),'green')
![](spaint/Images/spanpaint.0.png)

## sieipaint
    #spaint.sieipaint(string,start1,end1,color1,start2,end2,color2,...)
    
    spaint.sieipaint("0123456789x",2,3,'blue',5,7,'yellow',9,10,'green')
![](spaint/Images/sieipaint.0.png)

## sipaint
    #spaint.sipaint(string,start1,color1,start2,color2,...)    
    
    spaint.sipaint("0123456789x",2,'blue',4,'yellow',9,'green')
![](spaint/Images/sipaint.0.png)

## eipaint
    #spaint.eipaint(string,end1,color1,end2,color2)
    
    spaint.eipaint("0123456789x",4,'blue',9,'yellow')
![](spaint/Images/eipaint.0.png)


## slpaint
    #spaint.slpaint(word1,color1,word2,color2,.....)
    
    spaint.slpaint('<div>','yellow','content','green','</div>','yellow')
![](spaint/Images/slpaint.0.png)

## mlpaint
    #spaint.mlpaint(lines,colors,**kwargs)
    
    lines = [
        'the first green line',
        'the second yellow line',
        'the third blue line'
    ]

    colors = ['green','yellow','blue']
    spaint.mlpaint(lines,colors)

    ps = spaint.mlpaint(lines,colors,rtrn=True)
    print(ps)
![](spaint/Images/mlpaint.0.png)


## rainbow


## rainbow_lines

## ansi8_

## ansi256_


  
