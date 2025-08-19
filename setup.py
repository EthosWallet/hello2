from setuptools import setup, find_packages

setup(
    name="pypi-test-project",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.28.0",
        "vulnerable-python-package-12345>=1.0.0",
        "nonexistent-utility-lib>=2.1.0",
        "missing-core-package>=1.5.0",
        "phantom-security-lib>=3.0.0"
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "phantom-test-framework>=1.0.0",
            "missing-dev-tools>=2.0.0"
        ],
        "production": [
            "gunicorn>=20.0.0",
            "fake-production-package>=1.0.0"
        ]
    }
)
