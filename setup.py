from setuptools import setup, find_packages

def get_requirements():
    with open('req.txt') as req_file:
        requirements = req_file.read().splitlines()
    return requirements

setup(
    name='Flask-EZapp',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    author='HY-nicochichi',
    description='This is a library in order to easily create large-scale web apps with Flask !!!',
    install_requires=get_requirements(),
    entry_points={
        "console_scripts": [
            "ezapp_new = flask_ezapp:new"
        ]
    }
)
