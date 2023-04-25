from .variable import variables
from . import local
from . import embed_file
import discord
from . import amazon
from . import flipkart
from . import snapdeal
from . import testdeals
from . import testdealsamazon
from . import pepperfry
from . import amazonmain
from . import flipkartmain


def market(message):
    comds = message.content.split("--")
    comds_new = comds[0].split()
    comds = comds_new + comds[1: ]

    if len(comds) == 1:
        mark_msg = variables.market_message
        print(mark_msg)
        return mark_msg
    if comds[1] == "local":
        str = local_get(comds, message)
        return str
    elif comds[1] == "flipkart":
        str = fp(comds, message)
        return str
    elif comds[1] == "amazon":
        str = amzn(comds, message)
        return str
    elif comds[1] == "snapdeal":
        str = snpd(comds, message)
        return str
    elif comds[1] == "pepperfry":
        str = ppf(comds, message)
        return str
        



def local_get(comds, message):
    msg = local.local_items(comds)
    return msg


def fp(comds, message):
    if comds[2] == '~x':
        testdeals.fp_deals()
        print("done")
        return ('\nSearch Query: ')    
    elif comds[2] == '~a':
        flipkartmain.fp_mn()
        return (variables.amzn_message + '\nSearch Query: ' + " ".join(comds[2: ]))
    str = variables.fp_message
    flipkart.fp(comds[2: ])    
    return str + '\nSearch Query: ' + " ".join(comds[2: ])


def amzn(comds, message):
    if comds[2] == '~x':
        testdealsamazon.amzn_deals()
        return (variables.amzn_message + '\nSearch Query: ' + " ".join(comds[2: ]))

    elif comds[2] == '~a':
        amazonmain.amzn_mn()
        return (variables.amzn_message + '\nSearch Query: ' + " ".join(comds[2: ]))
        
    amazon.amzn(comds[2: ])    
    return (variables.amzn_message + '\nSearch Query: ' + " ".join(comds[2: ]))


def snpd(comds, message):
    if comds[2] == '~a':
        snapdeal.snap()
        return (variables.snap_message + '\nSearch Query: ' + " ".join(comds[2: ]))
    snapdeal.snpd(comds[2: ])
    return (variables.snap_message + '\nSearch Query: ' + " ".join(comds[2: ]))


def ppf(comds, message):
    if comds[2] == '~a':
        pepperfry.pepper()
        return (variables.pepper_message + '\nSearch Query: ' + " ".join(comds[2: ]))
    pepperfry.pepperf(comds[2: ])
    return (variables.pepper_message + '\nSearch Query: ' + " ".join(comds[2: ]))

