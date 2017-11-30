
# [Nysseituu](https://twitter.com/nysseituu)

[![Build Status](https://travis-ci.org/Vilsepi/nysseituu.svg?branch=master)](https://travis-ci.org/Vilsepi/nysseituu)

## Prerequisites

Serverless framework is required for deploying the app. It is installed with npm:

    sudo npm install -g serverless

Python 3.6 and its `venv` module is required for running the code. Depending on your OS, you may have to install it manually:

    sudo apt install python3-venv

Create a Python 3.6 virtual environment anywhere you'd like, we'll create it as `nyssenv` in the project home directory:

    python3.6 -m venv nyssenv

## Dependencies

Activate virtual environment:

    source nyssenv/bin/activate

Install dependencies in the `src/` directory:

    cd src/
    pip3 install -U -t vendored -r requirements.txt

## Deploying

    sls deploy -v
    sls deploy function -f nysseituu
    sls invoke -f nysseituu -l
    sls logs -f nysseituu -t
    sls deploy function -f nysseituu && sls invoke -f nysseituu -l
