"""Package setup"""
from setuptools import setup

from gen_pyi import main as gen_pyi

with open("README.md", "r") as fh:
    long_description = fh.read()

# generate pyi files from pyi.in files
gen_pyi()

setup(
    name="matplotlib-stubs",
    version="0.4.0.dev1",
    url="https://github.com/stdedos/data-science-types",
    project_urls={
        "Bug Tracker": "https://github.com/stdedos/matplotlib-stubs/issues/",
        "Source Code": "https://github.com/stdedos/matplotlib-stubs",
    },
    author="PAL",
    description="Type stubs for Python machine learning libraries",
    license="Apache License 2.0",
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_data={
        "matplotlib-stubs": [
            "__init__.pyi",
            "artist.pyi",
            "axes.pyi",
            "backend_bases.pyi",
            "collections.pyi",
            "color.pyi",
            "cm.pyi",
            "font_manager.pyi",
            "image.pyi",
            "legend.pyi",
            "patheffects.pyi",
            "pyplot.pyi",
            "style.pyi",
            "text.pyi",
            "transforms.pyi",
        ],
    },
    packages=[
        "matplotlib-stubs",
    ],
    python_requires=">=3.6",
    # use `pip install data-science-types[dev]` to install development packages
    extras_require={
        "dev": [
            "black",
            "flake8",
            "flake8-pyi",
            "matplotlib",
            "mypy==0.770",
            "pandas",
            "pytest",
        ]
    },
    classifiers=[  # classifiers can be found here: https://pypi.org/classifiers/
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Typing :: Typed",
    ],
    zip_safe=False,
)
