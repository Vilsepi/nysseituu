
## Dependencies

    npm install -g serverless
    pip install -t vendored -r requirements.txt

## Deploying

    sls deploy -v
    sls deploy function -f nysseituu
    sls invoke -f nysseituu -l
    sls logs -f nysseituu -t
    sls deploy function -f nysseituu && sls invoke -f nysseituu -l
