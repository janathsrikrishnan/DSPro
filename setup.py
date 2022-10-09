from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Data Structures with concurrency support'
LONG_DESCRIPTION = 'Same data structure can be used by multiple threads'

# Setting up
setup(
        name="DSPro", 
        version=VERSION,
        author="Janathsri Krishnan k (JANATH JSK)",
        author_email="janathjsk007@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], 
        license = 'MIT',       
        keywords=['python', 'data structure', 'concurrency', 'algorithms', 'multi processing'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)