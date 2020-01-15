import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="idm-tools-dtk", # Replace with your own username
    version="0.0.2",
    author="Christian Wiswell",
    author_email="cwiswell@idmod.org",
    description="Tools for building simulation configuration files for EMOD",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CWiswell-IDM/idm-tools-dtk",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6.3',
)