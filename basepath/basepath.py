"""
Simple base path function to avoid hardcoding file path
"""


def basepath(base):
    def full_path(tp, *args, **kwargs):
        extb = '/'.join(args)
        if extb:
            tp = '%s/%s' % (extb, tp)
        if kwargs.get('root', False):
            return '%s/%s' % (kwargs['root'], tp)
        return '%s/%s' % (base, tp)
    return full_path
