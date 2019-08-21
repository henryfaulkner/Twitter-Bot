from setuptools import setup

projectName = 'TwitterBot'

setup(
    name = projectName,
    version = '0.1dev',
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
