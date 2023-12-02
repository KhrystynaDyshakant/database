from setuptools import setup, find_packages

requires = [
    'flask',
    'flask-sqlalchemy',
    'psycopg2',
]

setup(
    name='database4',
    version='0.0',
    description='A db 4th lab built with Flask',
    author='<Khrystyna Dyshkant>',
    author_email='<khrystyna.diskant@gmail.com>',
    keywords='web flask',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
)