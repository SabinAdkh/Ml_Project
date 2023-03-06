from setuptools import find_packages,setup
from typing import List


HYPEN_E_DOT = '-e.'

def get_requirements(filePath:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requrements = []
    with open(filePath) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements


setup(
    name='Ml_Project',
    version='0.0.1',
    author='Sabin',
    author_email="adhikarisabin258@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),

)