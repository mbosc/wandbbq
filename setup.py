from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='wandbbq',
    packages=find_packages(),
    version='0.0.1',
    license='MIT',
    description='Wandb Backup and Quit - Unleash the power of wandb without fear of losing your data',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Matteo Boschini',
    author_email='matteoboschini3@gmail.com',
    url='https://github.com/mbosc/wandbbq',
    download_url='https://github.com/mbosc/wandbbq/archive/refs/tags/v0.0.1.zip',
    keywords=['wandb', 'bbq', 'offline', 'python', 'utility'],
    install_requires=["wandb"],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)