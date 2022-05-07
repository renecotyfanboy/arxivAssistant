from setuptools import setup, find_packages

__version__ = 0.3

setup(
    name='arxivAssistant',
    version=str(__version__),
    python_requires='>=3.10.4',
    description='Read daily arxiv feed with console',
    author='Simon Dupourqué',
    author_email='sdupourque@irap.omp.eu',
    packages=find_packages(exclude=["examples"]),
    install_requires=[
        'feedparser',
        'rich',
        'textual'
    ],
    url='https://github.com/renecotyfanboy/arxivAssistant',
    license='MIT',
    zip_safe=False,
    entry_points={
            'console_scripts': [
                'arxiv-today=arxivAssistant.scripts.today:main'
            ],
        }
)