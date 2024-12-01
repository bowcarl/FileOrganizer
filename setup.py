from setuptools import setup, find_packages

setup(
    name="ACIT4420-FileOrganizer",  # The name of your project
    version="0.1",
    packages=find_packages(),  # Automatically find all packages in your project
    include_package_data=True,  # Include non-Python files specified in MANIFEST.in (if any)
    description="Orgnaizes and sort files based on their extension, and adds new extension folders if needed.",
    author="Carl Petter Mørch-Reiersen",
    author_email="camor2778@oslomet.no",
    entry_points={
        'console_scripts': [
            'FileOrganizer=FileOrganizer.__main__:main',  # Points directly to the main function in main.py
        ],
    },
)
