# pdf2image
[![TravisCI](https://travis-ci.org/Belval/pdf2image.svg?branch=master)](https://travis-ci.org/Belval/pdf2image) [![PyPI version](https://badge.fury.io/py/pdf2image.svg)](https://badge.fury.io/py/pdf2image) [![codecov](https://codecov.io/gh/Belval/pdf2image/branch/master/graph/badge.svg)](https://codecov.io/gh/Belval/pdf2image) [![Downloads](https://pepy.tech/badge/pdf2image/month)](https://pepy.tech/project/pdf2image) [![mattermost](https://img.shields.io/badge/help-mattermost-blue)](https://mattermost.belval.org/signup_user_complete/?id=3anaj34563rqjg4xm5tdcmu7qa) [![Documentation Status](https://readthedocs.org/projects/pdf2image/badge/?version=latest)](https://pdf2image.readthedocs.io/en/latest/?badge=latest)

A python (3.5+) module that wraps pdftoppm and pdftocairo to convert PDF to a PIL Image object

## How to install

`pip install pdf2image`

### Windows

Windows users will have to install [poppler for Windows](http://blog.alivate.com.au/poppler-windows/), then add the `bin/` folder to [PATH](https://www.architectryan.com/2018/03/17/add-to-the-path-on-windows-10/).

### Mac

Mac users will have to install [poppler for Mac](http://macappstore.org/poppler/).

### Linux

Most distros ship with `pdftoppm` and `pdftocairo`. If they are not installed, refer to your package manager to install `poppler-utils`

### Platform-independant (Using `conda`)

1. Install poppler: `conda install -c conda-forge poppler`
2. Install pdf2image: `pip install pdf2image`

### Table of Contents

1. [Installation of Python Pacakages](#installation)
2. [Read the File ](#File reading )
3. [PDF to Image Conversion](#processing)
4. [Image to Text Conversion](#Text Conversion)
5. [Result](#Output)
6. [Licensing, Authors, and Acknowledgements](#licensing)

## Installation <a name="installation"></a>

There should be no necessary libraries to run the code here beyond the Anaconda distribution of Python. The code should run with no issues using Python versions 3.*.

## Project Intention <a name="Intention"></a>

This is python script would help you to understand how Image to text would give the accurate results.

Before running this script there are two main steps has to be process 
1. Installation of ** Tesseract Software ** from [Tesseract](https://digi.bib.uni-mannheim.de/tesseract/)
2. After Installing the software set the ** Enviornment Variable path ** by "(C:\Program Files (x86))"


## Results<a name="results"></a>

The main findings of the code can be found at as the PDF files can be read as the Image and post that Image can converted as Raw Text format. 


## Licensing, Authors, Acknowledgements<a name="licensing"></a>

Must give credit to Tesseract Owner [here](https://github.com/tesseract-ocr/tesseract) by providing such innovative idea and working on the python library.

