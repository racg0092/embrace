from channels.embrace import embrace
from channels.scaffold import scaffold


def get():
    CHANNELS = {
        '@embrace': embrace,
        '@scaffold': scaffold
    }
    return CHANNELS

