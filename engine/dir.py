import os


base_dir = os.path.dirname(__file__)


def use_base(fp: str):
    return os.path.join(base_dir, fp)
