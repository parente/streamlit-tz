from pathlib import Path

import setuptools

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setuptools.setup(
    name="streamlit-tz",
    version="0.1.1",
    author="Peter Parente",
    author_email="parente@gmail.com",
    description="Streamlit component that returns the user browser IANA timezone",
    url="https://github.com/parente/streamlit-tz",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.7",
    install_requires=["streamlit>=1.2", "jinja2"],
)
