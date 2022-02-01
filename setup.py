import os
from distutils.core import setup
from setuptools import find_packages



README_RST = os.path.join(os.getcwd(), "README.rst")
with open(README_RST, 'r') as rfile:
    LONG_DESCRIPTION = rfile.read()

setup(name='text-to-gif',
      version='0.0.4',
      keywords=("t2g", "text-to-gif", "text2gif", "levin", "leixuewei"),
      description='A small tool to generate text as gif, animation',
      long_description=LONG_DESCRIPTION,
      author='levin',
      author_email='levinmhliu@gmail.com',
      install_requires=["pillow","imageio"],
      license='Apache License 2.0',
      packages=find_packages(),
      platforms=["all"],
      entry_points={
          'console_scripts': [
              't2g = text_to_gif.main:main',
              'ttg = text_to_gif.main:main',
              'text2gif = text_to_gif.main:main',
              'text-to-gif = text_to_gif.main:main',
              'text-to-gif-cli = text_to_gif.main:main'
          ]
      },
      classifiers=[
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Natural Language :: Chinese (Simplified)',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Topic :: Software Development :: Libraries'
      ],
      )