from setuptools import setup, find_packages

setup(
    name='BookLoverPackage',
    version='1.0.0',
    url='https://github.com/JuliaBurek/HW14Package',
    author='Julia Burek',
    author_email='jeb5pb@virginia.edu',
    description='book lover package',
    packages=find_packages(),
    install_requires=['numpy >= 1.11.1', 'matplotlib >= 1.5.1'],
)