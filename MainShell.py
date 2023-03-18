import sys


def is_venv():
    return (hasattr(sys, 'real_prefix') or
            (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix))


if is_venv:
    print('inside a venv')
else: 
    print('not inside a virtual env')