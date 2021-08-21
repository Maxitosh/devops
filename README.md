# Web application

Simple web application written in Python with gunicorn that responses current Moscow time.

## Installation

### Source code

```bash
git clone https://github.com/Maxitosh/devops
```

### Docker image

```bash
docker pull maxitosh/devops_web_app
```

## Usage

### Source code

```bash
gunicorn -b 0.0.0.0:80 server:process_http_request  
```

### Docker

```bash
docker run -p "80:80" maxitosh/devops_web_app
```

## Contributing

Pull requests are welcome.

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Author

Kureikin Max BS18-SB
