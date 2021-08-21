# Best practices for Docker

## Linters

* [**hadolint**](https://github.com/hadolint/hadolint) - linter is parsing the Dockerfile into an AST and performs rules
  on top of the AST.
* [Dockerlint](https://github.com/RedCoolBeans/dockerlint) - linting tool for Dockerfiles based on recommendations from
  Dockerfile Reference and Best practices for writing Dockerfiles.
* [dockerfilelint](https://www.npmjs.com/package/dockerfilelint) - is an node module that analyzes a Dockerfile and
  looks for common traps, mistakes and helps enforce best practices.

## Practices

* Multi-stage builds - allow to drastically reduce the size of your final image, without struggling to reduce the number
  of intermediate layers and files.
* Exclude with .dockerignore - exclude files not relevant to the build, like .gitignore.
* Don’t install unnecessary packages - to reduce complexity, dependencies, file sizes, and build times, avoid installing
  extra or unnecessary packages.
* Minimize the number of layers
* Keep images small - choose an appropriate base image.
