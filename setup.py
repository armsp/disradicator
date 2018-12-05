from setuptools import setup, find_packages

setup(name='disradicator',
      version='0.1',
      description='Discharge Rate Indicator',
      author='Shantam Raj',
      author_email='shantamdps@gmail.com',
      license='GNU GPL v3',
      packages=find_packages("src"),
      scripts=['bin/disradicator'],
      include_package_data=True,
      zip_safe=False)