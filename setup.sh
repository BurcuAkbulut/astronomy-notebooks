#!/bin/bash

set -e

if ! conda --version >/dev/null 2>&1
then
    echo
    echo 'Error: Cannot find "conda" command'
    echo '       Please install Anaconda'
    echo '       http://continuum.io/downloads'
    echo
    exit 2
fi

cd $(dirname "${BASH_SOURCE[0]}")

# iPython, and the libraries needed for it to run Notebook.
conda install \
    python=2.7 \
    pip \
    ephem \
    ipython-notebook \
    matplotlib \
    mayavi \
    pandas \
    scipy \
    sympy \
    wxpython \


pip install \
    de405 \
    jplephem \
    skyfield \
    sgp4 \


# Get ready to download large data sets.
mkdir -p data
cd data

echo
echo 'Setup successful!'
echo 'Run "download_data.py" to make sure your "data" directory is populated.'
echo
