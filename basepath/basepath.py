"""
Simple base path function to avoid hardcoding project file paths
"""
from os.path import join

def bpath(base):
    def _bpath(tp='', *args, **kwargs):
        if args:
            tp = join(*args, tp)
        if kwargs.get('root', False):
            return join(kwargs['root'], tp)
        return join(base, tp)
    return _bpath
