import os
import __main__

base_dir = os.path.dirname(__main__.__file__)


def use_base(fp: str):
    return os.path.join(base_dir, fp)
