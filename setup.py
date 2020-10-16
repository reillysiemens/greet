from setuptools import find_packages, setup

setup(
    name="greet",
    version="1.0.0",
    description="A small example of using GitHub Actions with Python.",
    author="Reilly Tucker Siemens",
    author_email="reilly@tuckersiemens.com",
    python_requires=">= 3.6",
    package_dir={"": "src"},
    packages=find_packages("src"),
)
