import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="vlcHttp-bphermansson",
    packages = ['vlcHttp-bphermansson'],
    version="0.0.1",
    author="Patrik Hermansson",
    author_email="hermansson.patrik@gmail.com",
    description="A package to control VLC via Http",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bphermansson/vlcHttp",
    #packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
