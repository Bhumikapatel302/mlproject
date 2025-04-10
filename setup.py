from setuptools import find_packages,setup
from typing import List


def get_req(file_path:str)->List[str]:
    '''
    This function will return the list of requireemnts
    '''
    req=[]

    with open(file_path) as file_obj:
        req=file_obj.readlines()
        req=[req.replace('\n',"") for req in req ]


    return req





setup(
name='mlproject1',
version='0.0.1',
author='Bhumika',
author_email='bhoomzpatel6@gmail.com',
packages=find_packages(),
install_requires=get_req('req.txt')


)