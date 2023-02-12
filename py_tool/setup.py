from setuptools import setup

setup(
    name='py_tool',
    version='0.0.2',
    packages=[''],
    url='',
    license='MIT',
    author='yzqdev',
    author_email='',
    description='',
    install_requires=['click'],
    entry_points={
        'console_scripts': [
            'pytool = pytool.hello:cli',
        ]
    }
)
