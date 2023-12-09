from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    """
    this function returns the list of requirements
    """
    requirements = []

    with open(file_path, 'r') as file_obj:
        requirements = file_obj.readlines()
        requirements = [line.replace('\n', '') for line in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name = 'EndToEndML',
    version = '0.0.1',
    author = 'Hrithik Sharma',
    author_email = 'hrithik.sharma.stats@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)