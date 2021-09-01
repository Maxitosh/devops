
# CI best practices

## GitHub Actions best practices

* Keep your Actions minimal
* Don’t install dependencies unnecessarily
* Never hardcode secrets
* Limit environment variables to the narrowest possible scope
* Ensure every repository contains a CI/CD workflow
* Store authors in Action metadata to promote code ownership
* Don’t use self-hosted runners in a public repository

## Jenkins best practices

* Keep Jenkins secure all the time
* Always backup the “JENKINS_HOME” directory
* Setup a different Job/Project for each maintenance or development branch created
* Prevent resource collisions in jobs that are running in parallel (race condition)
* Build a scalable Jenkins pipeline
