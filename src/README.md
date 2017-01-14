
[AWS Blog: Simplified serverless application deployment](https://aws.amazon.com/blogs/compute/introducing-simplified-serverless-application-deplyoment-and-management/)

## Bummer

- Package does not support ignoring of files (includes all files in the current directory)
- Package does not support requirements.txt (you have to download deps yourself)
- Slow deployment (via cloudformation change set)
- No local development
- No easy access to cloudwatch logs?

Serverless framework is going to [wait it out](https://github.com/serverless/serverless/issues/2867)

## Deployment

    ./tool.sh deps
    ./tool.sh package
    ./tool.sh deploy
