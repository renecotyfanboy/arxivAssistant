import sys
from setuptools import setup, find_packages

__version__ = '0.3'

# READ README.md for long description on PyPi.
try:
    long_description = open("README.md", encoding="utf-8").read()
except Exception as e:
    sys.stderr.write("Failed to read README.md:\n  {}\n".format(e))
    sys.stderr.flush()
    long_description = ""

setup(
    name='arxivAssistant',
    version=__version__,
    python_requires='>=3.9',
    description='Read daily arxiv feed with console',
    author='Simon Dupourqué',
    author_email='sdupourque@irap.omp.eu',
    package_dir={'': "src"},
    packages=find_packages("src"),
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
        },
    long_description=long_description,
    long_description_content_type="text/markdown",
)