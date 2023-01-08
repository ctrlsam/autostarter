import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="autostart",
    version="0.0.1",
    author="Sam Redmond",
    author_email="samredmondtech@gmail.com",
    description="A module for adding and removing startup scripts on Windows, Mac, and Linux systems",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ctrlsam/autostart",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)