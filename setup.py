import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

<<<<<<< HEAD

=======
>>>>>>> f9bed1d (requirements updated)
__version__ = "0.0.0"

REPO_NAME = "Text-Summarizer-Project"
AUTHOR_USER_NAME = "nsrawat"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "rawatnarendra009@gmail.com"

<<<<<<< HEAD


=======
>>>>>>> f9bed1d (requirements updated)
setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP app",
    long_description=long_description,
<<<<<<< HEAD
    long_description_content="text/markdown",
=======
>>>>>>> f9bed1d (requirements updated)
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
<<<<<<< HEAD
)
=======
)
>>>>>>> f9bed1d (requirements updated)
