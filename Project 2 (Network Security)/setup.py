from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    """This function will return list of requirements"""
    requirement_list:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            lines = file.readlines()
            for line in lines:
                requirement=line.strip()
                if requirement and requirement!='-e.':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("Requirement file not found")

    return requirement_list

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Abhijeet Chauhan",
    author_email="abhijeetchauhan025@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)