import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cartoonfight",
    version="1.0.dev16",
    author="Kilian Melcher",
    author_email="kilian.melcher@gmail.com",
    description="2D Fighting game with cartoon characters",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kmmelcher/cartoonfight",
    packages=setuptools.find_packages(),
    install_requires=['pygame>=2.0'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
    ],
    entry_points={
        'console_scripts':['cartoonfight = cartoonfight.__main__:main']
    },
    python_requires='>=3.6',
    include_package_data=True,
)
