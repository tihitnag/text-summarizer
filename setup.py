import setuptools

with open('readme.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

__version__ = '0.0.0'
REPO_NAME = 'TEXT-SUMMARIZER'
AUTHOR_USER_NAME = 'tihitnag'
SRC_REPO = 'textsummarzer'
AUTHOR_EMAIL = 'tihitna@gmail.com'

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A Python package for text summarization",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    packages=setuptools.find_packages(where="src"),  # Specifies that the packages are located in the 'src' directory
    package_dir={"": "src"},  # Tells setuptools that all your packages are under 'src'
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Specify the minimum Python version requirement
    install_requires=[
        # List any dependencies your package needs
        # Example: 'numpy', 'pandas', etc.
    ],
)
