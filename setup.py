from setuptools import setup, find_packages

__version__ = 0.1

setup(
    name='arxivAssistant',
    version=__version__,
    description='Differentiate, compile, and transform Numpy code.',
    author='Simon Dupourqué',
    author_email='sdupourque@irap.omp.eu',
    packages=find_packages(exclude=["examples"]),
    install_requires=[
        'feedparser'
    ],
    url='???',
    license='MIT',
    zip_safe=False,
)