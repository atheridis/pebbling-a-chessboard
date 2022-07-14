from setuptools import setup, find_packages

setup(
    name="pebbling_a_chessboard",
    version="0.0.1",
    author="Georgios Atheridis",
    author_email="atheridis@tutamail.com",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "pebble-chessboard=pebbling_a_chessboard.main:main",
        ],
    },
    install_requires=[
        "pygame",
    ],
)
