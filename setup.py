from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return a l;ist of all the requirements
    '''
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requiremetns = [req.replace('\n','') for req in requirements]
    
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    
    name='soundEnhancement',
    version='0.1',
    author='Kai',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)