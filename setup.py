from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="TOPSIS-Aryan-101803035",
    version="0.0.2",
    py_modules = ["TOPSIS"],
    description="A Python package in which TOPSIS technique is implemented.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    author="Aryan Yadav",
    author_email="ayadav_be18@thapar.edu",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["TOPSIS-Aryan-101803035"],
    include_package_data=True,
    install_requires=["requests"],
    
)

