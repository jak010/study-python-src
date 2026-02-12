from pathlib import Path
from typing import Dict, List

from setuptools import setup, find_packages


def local_scheme(version):
    return ""


STD_PACKAGES = set(('array', 'math', 'os', 'random', 'struct', 'sys', 'ssl', 'time'))

setup(
    name="service_stubs",
    package=find_packages(where="./src"),
    data_files=[('.', ['base_service.pyi'])],
)
