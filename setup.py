import setuptools
import codecs

with codecs.open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    
setuptools.setup(
    name="dnevniklib",
    version="2.0.1b0",
    author="Ivan Kriventsev",
    author_email="<dirtyhornet277@gmail.com>",
    description="Библиотека для работы с МЭШ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/xD1rty/dnevniklib",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires='>=3.6',
    install_requires=['requests', "pydantic"]
)
