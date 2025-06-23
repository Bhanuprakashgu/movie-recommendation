from setuptools import setup

with open("README.md","r",encoding='utf-8') as fh:
    lond_description =fh.read()
    
AUTHOR_NAME ="BHANU PRAKASH"
SRC_REPO='src'
LIST_OF_REQUIREMENTS =['streamlit']

setup(
    name=SRC_REPO,
    version='0.0.1',
    author=AUTHOR_NAME,
    author_email='bhanuprakashguddeti@gmail.com',
    description='A small package for movies recommendation',
    long_description_content_type='text/markdown',
    package=[SRC_REPO],
    python_requires='>=3.12.4',
    install_requires=LIST_OF_REQUIREMENTS,
    
)