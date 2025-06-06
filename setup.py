from setuptools import setup, find_packages

setup(
    name="xnat-dcm2bids",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "click",
        "dcm2bids",
        "xnatutils",
        "dcm2niix",
    ],
    entry_points={
        "console_scripts": [
            "xnat-dcm2bids = xnat_dcm2bids.cli:main",
        ],
    },
)
