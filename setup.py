from setuptools import setup, find_packages

setup(
    name="DummyData",
    version="0.0.1",
    author="B. Linowski",
    author_email="bernd.linowski@bayer.com",
    # url="https://bit.ly/edeediong-resume",
    description="Provides access to dummy data",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    install_requires=[
      # "click", "pytz"
    ]
    #,
    #entry_points={"console_scripts": ["timechecker = src.main:main"]},
)
