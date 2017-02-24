from distutils.core import setup


setup(name='pythoncosmicjs',
      version='1.0',
      description='Python Cosmicjs API',
      author='Pavel Uskavan',
      author_email='uskavan@gmail.com',
      url='https://github.com/uskavan/pythoncosmicjs',
      packages=['pythoncosmicjs'],
      package_dir={'pythoncosmicjs': 'pythoncosmicjs'},
      requires=['requests']
      )
