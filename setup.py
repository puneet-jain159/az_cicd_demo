"""
This file configures the Python package with entrypoints used for future runs on Databricks.

Please follow the `entry_points` documentation for more details on how to configure the entrypoint:
* https://setuptools.pypa.io/en/latest/userguide/entry_point.html
"""

from setuptools import find_packages, setup
from az_cicd_demo import __version__

PACKAGE_REQUIREMENTS = ["PyYAML"]

DEV_REQUIREMENTS = [
    "setuptools",
    "wheel",
    "pyspark",
    "pyyaml",
    "pytest",
    "pytest-cov",
    "dbx",
    "mlflow",
    "delta-spark",
    "scikit-learn",
    "pandas"
]

setup(
    name="az_cicd_demo",
    packages=find_packages(exclude=["tests", "tests.*"]),
    setup_requires=["wheel"],
    install_requires=PACKAGE_REQUIREMENTS,
    extras_require={"dev": DEV_REQUIREMENTS},
    entry_points = {
        "console_scripts": [
            "etl = az_cicd_demo.tasks.sample_etl_task:entrypoint",
            "ml = az_cicd_demo.tasks.sample_ml_task:entrypoint"
    ]},
    version=__version__,
    description="",
    author="",
)
