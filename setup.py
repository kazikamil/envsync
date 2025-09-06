from setuptools import setup, find_packages

setup(
    name="envsync",
    version="0.1.0",
    description="A CLI tool to manage and synchronize .env files.",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/envsync",  # optional
    packages=find_packages(),
    install_requires=[
        "typer>=0.9.0",
    ],
    entry_points={
        "console_scripts": [
            "envsync=main:app",  # (module:function)
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # or your choice
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
