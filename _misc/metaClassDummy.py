from maya import cmds

def motherfucker(parent, child, attr):
    this_dict = {}
    for i, v in attr.items():
        if not i.startswith('__'):
            #get the connections of the selection
            sel = cmds.ls(sl = 1)
            for s in sel:
                attris = cmds.listAttr(s, channelBox = 1)
                this_dict[attris] = v
        else:
            #get the connections of the selection
            sel = cmds.ls(sl = 1)
            for s in sel:
                attris = cmds.listAttr(s, channelBox = 1)
                this_dict[attris] = v
    
    return type(parent, child, this_dict)

__metaclass__ = motherfucker

class haha():
    translateX = 123
    translateY = 12
    translateZ = 434
    
    
    
h = haha()
print h.translateX
#print hasattr(h, 'translateX')