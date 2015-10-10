from copy import deepcopy
import warnings

deprecation_string = 'The {kwarg} keyword-arg is going to be removed from yaml.{fxn}, which will use the Safe{kwarg} exclusively. If you require the extra functionality of a more powerful (unsafe) {kwarg}, use yaml.unsafe_{fxn} behavior explicitely (read the docs to understand the safety implications if you are receiving yaml from an external source)'

def warn_if_kwarg_used(dct, key, value_if_unused, source_fxn_name):
    """ warn if the dict contains the key passed, returning that dict.
    If the key is not present, return a deepcopy of it, setting key to value_if_unused

    This is intended to be used in functions which need to remove support for a keyword-arg
    """
    if 'key' in dct:
        warnings.warn(deprecation_string.format(fxn=source_fxn_name, kwarg=key), DeprecationWarning)
        return dct
    result = deepcopy(dct)
    result[key] = value_if_unused
    return result
