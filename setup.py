# -*- coding: utf-8 -*-

from setuptools import setup

setup(name='Loggy',
      version='0.0.1',
      description='A log analyser and alert',
      url='https://github.com/wenxer/loggy',
      author='Shown Tien',
      author_email='hightian@gmail.com',
      license='',
      packages=['loggy'],
      zip_safe=False,
      entry_points={
          'console_scripts': [
              'loggy = loggy.system.script:main'],
      })
