import spaint.spaint as spaint
from xdict.jprint import pdir,pobj
import elist.elist as elel
from spaint.spaint import *



#1.
spaint.spanpaint("0123456789x",(2,3),'blue',(5,7),'yellow',(9,10),'green')

#2.
spaint.sieipaint("0123456789x",2,3,'blue',5,7,'yellow',9,10,'green')


#3. (2,4) (4,9) (9,lngth)
spaint.sipaint("0123456789x",2,'blue',4,'yellow',9,'green')

#4. (0,4),(4,9),(9,lngth)
spaint.eipaint("0123456789x",4,'blue',9,'yellow')



#5. 
spaint.slpaint('<div>','yellow','content','green','</div>','yellow')

ps = spaint.slpaint('<div>','yellow','content','green','</div>','yellow',rtrn=True)
print(ps)

#6.

lines = [
    'the first green line',
    'the second yellow line',
    'the third blue line'
]

colors = ['green','yellow','blue']
spaint.mlpaint(lines,colors)

ps = spaint.mlpaint(lines,colors,rtrn=True)
print(ps)




#7.
rainbow(s*256,10)



#8.

lines = [
    'the first line',
    'the second line',
    'the third line',
    'the fourth line',
    'the fifth line'
]

rainbow_lines(lines)

#9.
spaint.ansi8_help()

#10.
spaint.ansi8_test(95)
spaint.ansi8_test('brightmagenta')


#11.
spaint.ansi256_help()

#12.
spaint.ansi256_test(2)
spaint.ansi256_test('green')



















#

