#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

PROFILE="heap"
STACK_NAME="nysseituu"
ARTIFACTORY_BUCKET="lambda-artifactory"

function deps {
  rm -rf ../build
  mkdir -p ../build
  pip install -r requirements.txt -t ../build/
}

function package {
  cp -rf {tweet,healthcheck} ../build/
  cp -f {*.py,sam.yml} ../build/
  cd ../build
  aws cloudformation package --template-file sam.yml --output-template-file sam.compiled.yml --s3-bucket $ARTIFACTORY_BUCKET --profile $PROFILE
}

function deploy {
  cd ../build
  aws cloudformation deploy --template-file sam.compiled.yml --stack-name $STACK_NAME --capabilities CAPABILITY_IAM --profile $PROFILE
}

function help_and_exit {
  echo "Error: Unknown subcommand, read script source for help."
  exit 1
}

if [ $# -lt 1 ]
then
  help_and_exit
fi
case "$1" in
  deps)
    deps
    ;;
  package)
    package
    ;;
  deploy)
    deploy
    ;;
  *)
    help_and_exit
esac
