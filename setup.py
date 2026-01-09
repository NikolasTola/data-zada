from setuptools import setup, find_packages

setup(
    name='data-zada',
    version='1.0.0',
    description='Data Infrastructure as Code',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click>=8.0.0',
        'pyyaml>=6.0',
        'sqlalchemy>=2.0.0',
        'pydantic>=2.0.0',
        'psycopg2-binary>=2.9.0',
    ],
    entry_points={
        'console_scripts': [
            'zada=src.cli.commands:cli',
        ],
    },
    python_requires='>=3.8',
)