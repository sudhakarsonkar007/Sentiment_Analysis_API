from typing import OrderedDict

def formatoutput(total,pos,neg,neu):
    output = OrderedDict({
            "total review":total,
            "positive review":pos,
            "negative review":neg,
            "neutral review":neu,
            })
    return output