# Web application

Simple web application written in Python with gunicorn that responses current Moscow time.

## Installation

### Source code

```bash
git clone https://github.com/Maxitosh/devops
```

### Docker image

#### Pull
```bash
docker pull maxitosh/devops_web_app
```

#### Build
```bash
git clone https://github.com/Maxitosh/devops
cd devops/app_python
docker build --tag maxitosh/devops_web_app .  
```


## Usage

### Source code

```bash
cd devops/app_python
gunicorn -b 0.0.0.0:80 server:process_http_request  
```

### Docker

```bash
docker run -p "80:80" --name devops_web_app maxitosh/devops_web_app
```

## Test

Application will be available at [127.0.0.1]()

## Contributing

Pull requests are welcome.

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Author

Kureikin Max BS18-SB  
Telegram: @Maxitosh
