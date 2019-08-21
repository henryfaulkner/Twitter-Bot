from setuptools import setup

projectName = 'TwitterBot'

setup(
    name = projectName,
    version = '1.0'
    packages = [projectName],
    entry_points = {
        'console_scripts': [
            projectName + " = " + projectName + ".__main__:main"
            ]
        },
    install_requires = [
        'tweepy',
        'textblob'
        ]
    )
