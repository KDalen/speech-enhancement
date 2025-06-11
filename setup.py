from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."


def get_requirements(file_path: str) -> List[str]:
    """Return a list of requirements from the given file."""

    requirements: List[str] = []
    with open(file_path) as f:
        requirements = [req.strip() for req in f.readlines()]

    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    
    name='soundEnhancement',
    version='0.1',
    author='Kai',
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)