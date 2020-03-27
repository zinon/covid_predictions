import numpy as np
import os

def name(odir, ofile):
    """
    create a file name with directory
    """
    if not os.path.exists(odir):
        os.mkdir(odir)
        
    return os.path.join( odir, ofile+'.png')

def save(fig = None, fn = None, txt = None):
    """
    store figure
    """
    if fn:
        print("Saving '%s'" % fn)
        if txt:
            fig.text(.1, .8, txt, fontsize=12)
        fig.savefig(fn)


def y_fmt(y, pos):
    """
    transform number to metrix suffix
    """
    decades = [1e9, 1e6, 1e3, 1e0, 1e-3, 1e-6, 1e-9 ]
    suffix  = ["G", "M", "k", "" , "m" , "u", "n"  ]
    if y == 0:
        return str(0)
    for i, d in enumerate(decades):
        if np.abs(y) >=d:
            val = y/float(d)
            signf = len(str(val).split(".")[1])
            if signf == 0:
                return '{val:d} {suffix}'.format(val=int(val), suffix=suffix[i])
            else:
                if signf == 1:
                    if str(val).split(".")[1] == "0":
                        return '{val:d} {suffix}'.format(val=int(round(val)), suffix=suffix[i]) 
                tx = "{"+"val:.{signf}f".format(signf = signf) +"} {suffix}"
                return tx.format(val=val, suffix=suffix[i])
    return y

