from setuptools import setup, find_packages

setup(
    name='bashguard',
    version='0.1.2',
    description='Analysis tool of the history of the Bash/ZSH teams',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Insany',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'bashguard=bashguard.cli:main'
        ]
    },
    install_requires=[
        'colorama>=0.4.6'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)