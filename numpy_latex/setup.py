from setuptools import setup, find_packages


def do_setup():
    setup(name='numpy_latex',
          version="0.0",
          author='chebee7i',
          platforms=['Windows', 'Linux', 'Mac OS-X', 'Unix'],
          packages=find_packages())

if __name__ == "__main__":
    do_setup()