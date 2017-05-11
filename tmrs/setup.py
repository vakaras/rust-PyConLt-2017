from setuptools import setup
from setuptools_rust import RustExtension

setup(name='tmrs',
      version='1.0',
      rust_extensions=[RustExtension('tmrs._tmrs', 'extensions/Cargo.toml')],
      packages=['tmrs'],
      zip_safe=False
)
