from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requires = f.read().splitlines()

setuptools.setup(
    name="{{cookiecutter.package_name}}", # Replace with your own username
    version="0.0.1",
    author="{{cookiecutter.author_name}}",
    author_email="{{cookiecutter.author_email}}",
    description="{{cookiecutter.package_description}}",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "pandas >= 0.25.3"
    ],
    python_requires='{{cookiecutter.python_version}}',
) 
