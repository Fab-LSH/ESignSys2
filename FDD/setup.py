from setuptools import setup, find_packages

setup(
    name="fasc-api",
    version="5.1.0",
    author="fdd",
    packages=find_packages(),
    install_requires=["distribute"],
    description="FASC OpenAPI python SDK",
    keywords="FASC OpenAPI, SDK",
    url='https://gitee.com/fadada-cloud',
)
