from setuptools import setup, find_packages

setup (name="census-income",
      version="0.0.1",
      author="Ashok Bhatta",
      author_email="ashok.bhatta@duke.edu",
      package=find_packages(),
      install_requires=["pandas","numpy","flask"]
      )