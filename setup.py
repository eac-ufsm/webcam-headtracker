from setuptools import setup, find_namespace_packages

setup(
    name="EACheadtracker",
    description=" webcam headtracker",
    author="Davi Carvalho",
    url="https://github.com/eac-ufsm/webcam-headtracker",
    author_email="r.davicarvalho@gmail.com",
    version="0.0.1",
    install_requires=[
        "numpy",
        "mediapipe",
        "click",
        "opencv-python"
    ],
    packages=find_namespace_packages(include='EACheadtracker.*'),
    package_data={}, # No data yet.
    # extras_require={
    #     "dev": ["flake8", "flake8-black"],
    #     "test": ["pytest"],
    # },
    entry_points={} # No executable scripts yet
)
