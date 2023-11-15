from setuptools import setup, find_packages

setup(
    name='your_project',  # Replace with your project name
    version='0.1',        # Replace with your project version
    packages=find_packages(),  # Automatically discover and include all packages
    install_requires=[
        'setuptools',
        'customtkinter==5.2.1',
    ]
)