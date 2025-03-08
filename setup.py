from setuptools import setup, find_packages

setup(
    name="your_project_name",
    version="0.1",
    packages=find_packages(),  # Explicitly define package discovery
    py_modules=["simple", "router", "agent", "main"],  # List your modules explicitly
)
