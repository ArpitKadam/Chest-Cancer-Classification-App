from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    requirements = []
    with open('requirements.txt') as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        
        if '-e .' in requirements:
            requirements.remove('-e .')

    return requirements

setup(
    name = "Chest-Cancer-Classification-App",
    version = "0.0.0",
    author = "ArpitKadam",
    author_email="arpitkadam922@gmail.com",
    description="Package for Chest-Cancer-Classification-App",
    url="https://github.com/ArpitKadam/Chest-Cancer-Classification-App",
    packages=find_packages(),
    install_requires = get_requirements(),
)