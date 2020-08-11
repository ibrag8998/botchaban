from setuptools import find_packages, setup

with open("README.md") as f:
    long_description = f.read()

with open("requirements/base.txt") as f:
    base_requirements = f.readlines()

setup(
    name="chaban",
    version="0.1.0",
    packages=find_packages(),
    author="Ibrahim Gadzhimagomedov",
    author_email="ibragdzh@gmail.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ibrag8998/chaban/",
    python_requires=">=3.8",
    install_requires=base_requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
