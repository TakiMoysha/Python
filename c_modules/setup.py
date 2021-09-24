from distutils.core import setup, Extension

module_name = 'tm_test_module'
c_files = ['tm_fib_test.c']

extension = Extension(
    module_name,
    c_files
)

setup(
    name=module_name,
    version='0.1',
    description='First C module for Python',
    author='Mikhail Popov',
    author_email='mpwema782@gmail.com',
    url='https://github.com/TakiMoysha',
    ext_modules=[extension]
)
