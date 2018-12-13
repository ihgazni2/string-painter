from setuptools import setup, find_packages
setup(
      name="spaint",
      version = "0.6",
      description="console,print-colorful-string",
      author="dapeli",
      url="https://github.com/ihgazni2/spaint",
      author_email='terryinzaghi@163.com', 
      license="MIT",
      long_description = "refer to .md files in https://github.com/ihgazni2/spaint",
      classifiers=[
          'Environment :: Console',
          'Environment :: Web Environment',
          'Intended Audience :: End Users/Desktop',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'Programming Language :: Python',
          ],
      packages= find_packages(),
      py_modules=['spaint'], 
      )


# python3 setup.py bdist --formats=tar
# python3 setup.py sdist
# sed -i s/conjugar/spaint/g setup.py
