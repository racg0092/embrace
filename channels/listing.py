from channels.embrace import embrace
from channels.scaffold import scaffold

_CHANNELS = {
    '@embrace': embrace,
    '@scaffold': scaffold
}


def get():
    return _CHANNELS

