from setuptools import setup, find_packages

setup(
    name="order_calculator",
    version="0.1",
    packages=find_packages(),
    py_modules=["order_calculator"],

    # Dependencies
    install_requires=[],

    # Metadata
    author="Kaye Manuel",
    author_email="kayeeemanuel@gmail.com",
    description="A simple order calculator for different order types.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/order_calculator",  # Replace with your GitHub URL

    # Entry points for command-line scripts
    entry_points={
        "console_scripts": [
            "order_calculator=order_calculator:main",
        ],
    },

    # License and classifiers
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
