from setuptools import setup, find_packages

setup(
    name="dataset_image",
    version="0.1",
    description="Custom Image downloader to create amazing datasets for your models",
    url="https://github.com/kurianbenoy/dataset_image",
    author="Kurian Benoy",
    author_email="kurian.bkk@gmail.com",
    packages=find_packages(),
    install_requires=['google_images_download'],
    zip_safe=False
)
