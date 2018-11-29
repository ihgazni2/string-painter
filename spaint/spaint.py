import os
import sys
import copy
import elist.elist as elel

##platform
def is_win():
    platform = os.sys.platform.lower()
    if('win' in platform):
        return(True)
    else:
        return(False)
########################


##str
def str_rstrip(s,char,count):
    '''
        str_rstrip('asss','s',0)
        str_rstrip('asss','s',1)
        str_rstrip('asss','s',2)
        str_rstrip('asss','s',3)
        str_rstrip('asss','s',4)
    '''
    c = 0
    for i in range(s.__len__()-1,-1,-1):
        if(c==count):
            break
        else:
            if(s[i] == char):
                c = c+1
            else:
                break
    if(c==0):
        return(s)
    else:
        ei = s.__len__() - c
        return(s[:ei])
#########################


def oldStylize(color_sec):
    '''
        for compatible with old code
        old_style_color_sec = {1: (0, 11, 'white'), 2: (12, 19, 'blue'), 3: (20, 21, 'white')}
        new_style_color_sec = [(0, 12, 'white'), (12, 20, 'blue'), (20, 22, 'white')]
        oldStylize(new_style_color_sec)
    '''
    if(isinstance(color_sec,dict)):
        return(copy.deepcopy(color_sec))
    else:
        pass
    new = {}
    for i in range(0,color_sec.__len__()):
        sec = color_sec[i]
        new[i+1] = copy.deepcopy(list(sec))
        new[i+1][1] = sec[1] - 1
        new[i+1] = tuple(new[i+1])
    return(new)



def newStylize(color_sec):
    '''
        for compatible with old code
        old_style_color_sec = {1: (0, 11, 'white'), 2: (12, 19, 'blue'), 3: (20, 21, 'white')}
        new_style_color_sec = [(0, 12, 'white'), (12, 20, 'blue'), (20, 22, 'white')]
        newStylize(old_style_color_sec)
    '''
    if(isinstance(color_sec,list)):
        return(copy.deepcopy(color_sec))
    else:
        pass
    new = []
    for i in range(0,color_sec.__len__()):
        sec = color_sec[i+1]
        sec = copy.deepcopy(list(sec))
        sec[1] = sec[1] + 1
        sec = tuple(sec)
        new.append(sec)
    return(new)




def standlize_color_sec(color_sec,COLORS_MD):
    #now we can accept either new_style_color_sec or old_style_color_sec
    #the internal function use old_style_color_sec
    color_sec = oldStylize(color_sec)
    new = {}
    for seq in color_sec:
        sec = color_sec[seq]
        color = sec[2]
        if(isinstance(color,str)):
            color = color.lower()
            if(is_win()):
                color = color.replace('bright','light')
            else:
                color = color.replace('light','bright')
            color = COLORS_MD[color]
        new[seq] = copy.deepcopy(list(sec))
        new[seq][2] = color
        new[seq] = tuple(new[seq])
    return(new)


if(is_win()):
    from ctypes import *
    from win32con import *
    
    COLORS_MD = {
     'darkgray': 9,
     'lightblue': 10,
     'brightblue':10,
     'magenta': 6,
     'default': 0,
     'lightmagenta': 14,
     'black': 1,
     'cyan': 4,
     'red': 5,
     'lightcyan': 12,
     'brown': 7,
     'lightgreen': 11,
     'lightred': 13,
     'blue': 2,
     'yellow': 15,
     'lightgray': 8,
     'white': 16,
     'green': 3,
      0: 'default',
     1: 'black',
     2: 'blue',
     3: 'green',
     4: 'cyan',
     5: 'red',
     6: 'magenta',
     7: 'brown',
     8: 'lightgray',
     9: 'darkgray',
     10: 'lightblue',
     11: 'lightgreen',
     12: 'lightcyan',
     13: 'lightred',
     14: 'lightmagenta',
     15: 'yellow',
     16: 'white'
    }
    
    
    CloseHandle = windll.kernel32.CloseHandle
    GetStdHandle = windll.kernel32.GetStdHandle
    GetConsoleScreenBufferInfo = windll.kernel32.GetConsoleScreenBufferInfo
    SetConsoleTextAttribute = windll.kernel32.SetConsoleTextAttribute
    
    
    STD_OUTPUT_HANDLE = -11
    
    class COORD(Structure):
        _fields_ = [
            ('X', c_short),
            ('Y', c_short),
        ]
    
    class SMALL_RECT(Structure):
        _fields_ = [
            ('Left', c_short),
            ('Top', c_short),
            ('Right', c_short),
            ('Bottom', c_short),
        ]
    
    class CONSOLE_SCREEN_BUFFER_INFO(Structure):
        _fields_ = [
            ('dwSize', COORD),
            ('dwCursorPosition', COORD),
            ('wAttributes', c_uint),
            ('srWindow', SMALL_RECT),
            ('dwMaximumWindowSize', COORD),
        ]
    
    def _paint_str(text,**kwargs):
        '''for compatible with old code'''
        return(text)    

    def print_str(text,**kwargs):
        hconsole = GetStdHandle(STD_OUTPUT_HANDLE)
        cmd_info = CONSOLE_SCREEN_BUFFER_INFO()
        GetConsoleScreenBufferInfo(hconsole, byref(cmd_info))
        old_color = cmd_info.wAttributes
        if('colors_md' in kwargs):
            colors_md = kwargs['colors_md']
        else:
            colors_md = COLORS_MD
        if("fg" in kwargs):
            fg = kwargs['fg']
        else:
            fg = 16
        if("bg" in kwargs):
            bg = kwargs['bg']
        else:
            bg = 1
        if(isinstance(fg,int)):
            pass
        else:
            fg = colors_md[fg]
        if(isinstance(bg,int)):
            pass
        else:
            bg = colors_md[bg]
        if('single_color' in kwargs):
            single_color = kwargs['single_color']
            if(isinstance(single_color,str)):
                single_color = single_color.lower()
                single_color = single_color.replace('bright','light')
                if(single_color in COLORS_MD):
                    single_color = COLORS_MD[single_color]
                else:
                    print("please input correct color name")
                    pass
            elif(isinstance(single_color,int)):
                pass
            else:
                print("color must be name or int ")
                pass
        else:
            single_color = None
        ####color_sec multicolor for string (si,ei,fg,bg,style), ei is included
        ####"ab" +"bc"
        ####color_sec = {1:(0,1,2),2:(2,3,4)}
        if('color_sec' in kwargs):
            color_sec = kwargs['color_sec']
        else:
            color_sec = None
        if(color_sec):
            color_sec = standlize_color_sec(color_sec,COLORS_MD)
            color_sec_len = color_sec.__len__()
            for i in range(1,color_sec_len + 1):
                ele = color_sec[i]
                si = color_sec[i][0]
                ei = color_sec[i][1]
                tmpfg = color_sec[i][2]
                length = ele.__len__()
                if(length == 3):
                    tmpbg = bg
                elif(length == 4):
                    tmpbg = color_sec[i][3]
                else:
                    tmpbg = color_sec[i][3]
                tmpfg = (tmpfg -1) & 0x0f
                tmpbg = ((tmpbg -1)<<4) & 0xf0
                sec = text[si:ei+1]
                SetConsoleTextAttribute(hconsole, tmpfg + tmpbg)
                #dont use print("xxxx",end=""),important!
                sys.stdout.write(sec)
                sys.stdout.flush()
            SetConsoleTextAttribute(hconsole, old_color)
            print("")
        else:
            fg = single_color
            bg = bg
            fg = (fg -1) & 0x0f
            bg = ((bg -1)<<4) & 0xf0
            SetConsoleTextAttribute(hconsole, fg + bg)
            print(text)
            SetConsoleTextAttribute(hconsole, old_color)
else:
    #for compatible with old code
    def print_str(text,**kwargs):
        print(text)
    def _paint_str(orig_string,**kwargs):
        '''
            currently only support 8 color name,
            if using 256 color need using color number
        '''
        default =  "\033[0m"
        painted_string = default
        #####mode 
        if('mode' in kwargs):
            mode = kwargs['colors']
        else:
            mode = 8
        if(mode == 8):
            color_control = ansi_8color_control
        elif(mode == 256):
            color_control = ansi_256color_control
        else:
            print("mode : " +mode +"not supported!,fallback to 8color ")
            color_control = ansi_8color_control
        ######color name<->number mapping
        if('colors' in kwargs):
            colors = kwargs['colors']
        else:
            colors = COLORS_MD
        ####singlecolor for string
        if("bg" in kwargs):
            bg = kwargs['bg']
        else:
            bg = 30
        if("style" in kwargs):
            style = kwargs['style']
        else:
            style = 1
        if('single_color' in kwargs):
            single_color = kwargs['single_color']
            if(isinstance(single_color,str)):
                single_color = single_color.lower()
                single_color = single_color.replace('light','bright')
                if(single_color in COLORS_MD):
                    single_color = COLORS_MD[single_color]
                else:
                    print("please input correct color name")
                    pass
            elif(isinstance(single_color,int)):
                pass
            else:
                print("color must be name or int ")
                pass
        else:
            single_color = None
        ####color_sec multicolor for string (si,ei,fg,bg,style), ei is included
        ####"ab" +"bc"
        ####color_sec = {1:(0,1,'blue'),2:(2,3,'green')}
        if('color_sec' in kwargs):
            color_sec = kwargs['color_sec']
        else:
            color_sec = None
        if(color_sec):
            color_sec = standlize_color_sec(color_sec,COLORS_MD)
            color_sec_len = color_sec.__len__()
            for i in range(1,color_sec_len + 1):
                ele = color_sec[i]
                si = color_sec[i][0]
                ei = color_sec[i][1]
                fg = color_sec[i][2]
                length = ele.__len__()
                if(length == 3):
                    color = color_control(fg=fg)
                elif(length == 4):
                    bg = color_sec[i][3]
                    color = color_control(fg=fg,bg=bg)
                else:
                    bg = color_sec[i][3]
                    style = color_sec[i][4]
                    color = color_control(fg=fg,bg=bg,style=style)
                sec = ''.join((color,orig_string[si:ei+1]))
                painted_string = ''.join((painted_string,sec))
            painted_string = ''.join((painted_string,default))
        else:
            fg = single_color
            bg = bg
            style = style
            color = color_control(fg=fg,bg=bg,style=style)
            painted_string = ''.join((painted_string,color,orig_string,default))
        return(painted_string)

    COLORS_MD = {
        'black': 30,
        'red': 31,
        'brightwhite': 97,
        'brightyellow': 93,
        97: 'brightwhite',
        'brightblack': 90,
        'brightred': 91,
        'blue': 34,
        'brightcyan': 96,
        'lightcyan': 96,
        'brightmagenta': 95,
        90: 'brightblack',
        91: 'brightred',
        'white': 37,
        93: 'brightyellow',
        30: 'black',
        31: 'red',
        32: 'green',
        33: 'yellow',
        34: 'blue',
        35: 'magenta',
        36: 'cyan',
        37: 'white',
        'cyan': 36,
        92: 'brightgreen',
        95: 'brightmagenta',
        'brightgreen': 92,
        'lightgreen': 92,
        'magenta': 35,
        96: 'brightcyan',
        'green': 32,
        94: 'brightblue',
        'brightblue': 94,
        'lightblue':94,
        'yellow': 33
    }
    
    def ansi_8color_control(**kwargs):
        '''
            The original specification only had 8 colors, and just gave them names. 
            The SGR parameters 30-37 selected the foreground color, 
            while 40-47 selected the background. 
            Quite a few terminals implemented "bold" (SGR code 1) 
            as a brighter color rather than a different font, 
            thus providing 8 additional foreground colors. 
            Usually you could not get these as background colors,
            though sometimes inverse video (SGR code 7) would allow that.
            Examples: to get black letters on white background use ESC[30;47m, to get red use ESC[31m, 
            to get bright red use ESC[1;31m. To reset colors to their defaults, 
            use ESC[39;49m (not supported on some terminals), or reset all attributes with ESC[0m. 
            Later terminals added the ability to directly specify the "bright" colors with 90-97 and 100-107.
        '''
        if("fg" in kwargs):
            fg = kwargs['fg']
        else:
            fg = 37
        if("bg" in kwargs):
            bg = kwargs['bg']
        else:
            bg = 30
        bg = bg + 10
        if("style" in kwargs):
            style = kwargs['style']
        else:
            style = 1
        control = '\033[' + str(style)+ ";" +str(fg) +";"+str(bg) +"m"
        return(control)
    
    def ansi_256color_control(**kwargs):
        '''
            ESC[ … 38;5;<n> … m Select foreground color
            ESC[ … 48;5;<n> … m Select background color
              0-  7:  standard colors (as in ESC [ 30–37 m)
              8- 15:  high intensity colors (as in ESC [ 90–97 m)
             16-231:  6 × 6 × 6 cube (216 colors): 16 + 36 × r + 6 × g + b (0 ≤ r, g, b ≤ 5)
            232-255:  grayscale from black to white in 24 steps
        '''
        if("fg" in kwargs):
            fg = kwargs['fg']
        else:
            fg = 255
        if("bg" in kwargs):
            bg = kwargs['bg']
        else:
            bg = 0
        control = '\033[38;5;' +str(fg) +"m" + '\033[48;5;' +str(bg) +"m"
        return(control)


def fullfill_colors(spans,old_spans,colors,default_color):
    rslt = []
    lngth = spans.__len__()
    for i in range(0,lngth):
        cond = (spans[i] in old_spans)
        if(cond):
            index = old_spans.index(spans[i])
            color = colors[index]
        else:
            color = default_color
        rslt.append(color)
    return(rslt)

###############################################


if(is_win()):
    _paint = print_str
else:
    def _paint(s,**kwargs):
        if('end' in kwargs):
            end = kwargs['end']
        else:
            end = '\n'
        if(rtrn in kwargs):
            rtrn = kwargs[rtrn]
        else:
            rtrn = False
        if(rtrn):
            return(_paint_str(s,**kwargs))
        else:
            print(_paint_str(s,**kwargs),end=end)



def spanpaint(s,*args,**kwargs):
    def map_func(span,color):
        return((span[0],span[1],color))
    if('default_color' in kwargs):
        default_color = kwargs['default_color']
    else:
        default_color = 'white'
    args = list(args)
    old_spans = elel.select_evens(args)
    colors = elel.select_odds(args)
    lngth = s.__len__()
    spans = elel.rangize_fullfill(old_spans,lngth)
    colors = fullfill_colors(spans,old_spans,colors,default_color)
    color_sec = elel.array_map2(spans,colors,map_func=map_func)
    return(_paint(s,color_sec=color_sec))


def sieipaint(s,*args,**kwargs):
    def map_func(span,color):
        return((span[0],span[1],color))
    if('default_color' in kwargs):
        default_color = kwargs['default_color']
    else:
        default_color = 'white'
    args = list(args)
    tmp = elel.deinterleave(args,3)
    sis = tmp[0]
    eis = tmp[1]
    colors = tmp[2]
    old_spans = elel.mapiv(sis,lambda index,ele:((ele,eis[index])),[])
    lngth = s.__len__()
    spans = elel.rangize_fullfill(old_spans,lngth)
    colors = fullfill_colors(spans,old_spans,colors,default_color)
    color_sec = elel.array_map2(spans,colors,map_func=map_func)
    return(_paint(s,color_sec=color_sec))


def get_eis_from_sis(sis,lngth):
    sis.sort()
    eis = []
    for i in range(1,sis.__len__()):
        ei = sis[i]
        if(ei<lngth):
            eis.append(ei)
        else:
            eis.append(lngth)
            break
    eis.append(lngth - 1)
    return(eis)

def sipaint(s,*args,**kwargs):
    def map_func(span,color):
        return((span[0],span[1],color))
    if('default_color' in kwargs):
        default_color = kwargs['default_color']
    else:
        default_color = 'white'
    args = list(args)
    tmp = elel.deinterleave(args,2)
    sis = tmp[0]
    colors = tmp[1]
    eis = get_eis_from_sis(sis,s.__len__())
    old_spans = elel.mapiv(sis,lambda index,ele:((ele,eis[index])),[])
    lngth = s.__len__()
    spans = elel.rangize_fullfill(old_spans,lngth)
    colors = fullfill_colors(spans,old_spans,colors,default_color)
    color_sec = elel.array_map2(spans,colors,map_func=map_func)
    return(_paint(s,color_sec=color_sec))


def get_sis_from_eis(eis,lngth):
    eis.sort()
    if(eis[-1]>lngth):
        eis[-1] = lngth
    else:
        pass
    sis = [0]
    for i in range(0,eis.__len__()):
        si = eis[i] + 1
        if(si<lngth):
            sis.append(si)
        else:
            break
    return(sis)



def eipaint(s,*args,**kwargs):
    def map_func(span,color):
        return((span[0],span[1],color))
    if('default_color' in kwargs):
        default_color = kwargs['default_color']
    else:
        default_color = 'white'
    args = list(args)
    tmp = elel.deinterleave(args,2)
    eis = tmp[0]
    colors = tmp[1]
    sis = get_sis_from_eis(eis,s.__len__())
    old_spans = elel.mapiv(sis,lambda index,ele:((ele,eis[index])),[])
    lngth = s.__len__()
    spans = elel.rangize_fullfill(old_spans,lngth)
    colors = fullfill_colors(spans,old_spans,colors,default_color)
    color_sec = elel.array_map2(spans,colors,map_func=map_func)
    return(_paint(s,color_sec=color_sec))




####



def slpaint(*args,**kwargs):
    '''
        slpaint('<div>','yellow','content','green','</div>','yellow')
    '''
    args = list(args)
    strs = elel.select_evens(args)
    colors = elel.select_odds(args)
    lngth = strs.__len__()
    spans = []
    si = 0
    ei = 0
    for i in range(0,lngth):
        ei = si + strs[i].__len__()
        color = colors[i]
        span = (si,ei,color)
        spans.append(span)
        si = ei
    s = elel.join(strs,'')
    if(rtrn in kwargs):
        rtrn = kwargs[rtrn]
    else:
        rtrn = False
    return(_paint(s,color_sec=spans,rtrn=rtrn))


    

def mlpaint(lines,colors,**kwargs):
    '''
        lines = [
            'the first green line',
            'the second yellow line',
            'the third blue line'
        ]
        
        colors = ['green','yellow','blue']
        mlpaint(lines,colors)
    '''
    if('line_sp' in kwargs):
        line_sp = kwargs[rtrn]
    else:
        line_sp = '\n'
    if(rtrn in kwargs):
        rtrn = kwargs[rtrn]
    else:
        rtrn = False
    s = ''
    length = lines.__len__()
    clen = colors.__len__()
    if(clen < length):
        colors = copy.deepcopy(colors)
        colors.extend(['white'] * (length-clen))
    else:
        pass
    color_sec = {}
    cursor = 0
    for i in range(0,length):
        line = lines[i] + line_sp
        llen = line.__len__()
        color = colors[i]
        color_sec[i+1] = (cursor,cursor+llen-1,color)
        cursor = cursor + llen
        s = s + line
    s = str_rstrip(s,line_sp,1)
    return(_paint(s,color_sec=spans,rtrn=rtrn))



