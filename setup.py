from setuptools import setup, find_packages
 
with open("Readme.md", "r") as f:
    long_description = f.read()

setup(
    name="src",
    version="0.0.0",
    author= "Prakhyath Bhandar",
    author_email= "prakhyathb07@gmail.com",
    description= " dvc for tensorflow demo",
    long_description= long_description,
    long_description_content_type = "text/markdown",
    packages=["src"],
    python_requires = ">=3.7",
    install_requires = [
        'dvc',
        'tensorflow',
        'numpy',
        'pandas',
        'tqdm',
        'pyYAML',
        'boto3'
    ]


)
