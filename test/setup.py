from setuptools import setup

setup(name='test',
      version='1.0',
      packages=['bench'],
      install_requires=['tmpy'],
      entry_points={
        'console_scripts': [
            'test=bench:main',
        ],
      },
)
