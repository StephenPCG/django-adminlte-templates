from setuptools import setup

setup(
    name='django-adminlte-templates',
    version='2.1.2.0', # '2.1.2' is AdminLTE version, '0' is our version
    packages=['AdminLTE'],
    include_package_data=True,
    license='MIT License',
    description='AdminLTE Bootstrap Temolates packaged for Django',
    long_description=open('README.md', 'r').read(),
    url='https://github.com/StephenPCG/django-adminlte-templates',
    author='Stephen Zhang',
    author_email='stephenpcg@gmail.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Utilities',
    ],
    keywords='django bootstrap theme',
    install_requires=[
        'django>=1.4',
    ],
)
