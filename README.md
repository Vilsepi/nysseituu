
# [Nysseituu](https://twitter.com/nysseituu) [![Build Status](https://travis-ci.org/Vilsepi/nysseituu.svg?branch=master)](https://travis-ci.org/Vilsepi/nysseituu)

A serverless Twitter bot that checks if the [Lissu Traffic Monitor](http://lissu.tampere.fi/?lang=en) service of [Tampere Regional Transport](http://joukkoliikenne.tampere.fi/en/home.html) has crashed again. Because as you know, it is down a lot.

You can send feedback regarding the Lissu Traffic Monitor to Tampere Regional Transport [here](http://joukkoliikenne.tampere.fi/en/info/customer-service/feedback/feedback-online-services.html). Who knows, they might even fix their service some day.

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

Install dev dependencies in the `src/` directory:

    pip3 install -U -r requirements-dev.txt

Install runtime dependencies in the `src/` directory:

    pip3 install -U -t vendored -r requirements.txt

Install Serverless plugins

    npm install --save-dev serverless-plugin-tracing

## Deploying

    sls deploy -v
    sls deploy function -f nysseituu
    sls invoke -f nysseituu -l
    sls logs -f nysseituu -t
    sls deploy function -f nysseituu && sls invoke -f nysseituu -l

## Disclaimer

This hobby project is not affiliated with Tampere Regional Transport or any other organization.
