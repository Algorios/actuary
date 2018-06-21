from setuptools import setup

with open('README.md') as f:
    long_description = f.read()
  
setup(
    name='actuary',
    version='0.2',
    packages=['actuary', 'actuary.utils', 'actuary.regression',
              'Chapter_2_Core_Python.Chapter_2_Case_Study.rate_table'],
    url='https://github.com/validatehealth/actuary',
    license='MIT',
    author='Andrew Webster',
    author_email='info@validatehealth.com',
    description='This is an actuarial toolkit as introduced by three Actex webinars on Python for Actuaries',
    long_description=long_description,
    long_description_content_type='text/markdown' # This is important!
)
