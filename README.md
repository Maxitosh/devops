# Web application

Simple web application written in Python with gunicorn that responses current Moscow time.

## Requirements

### Local

* Python3 [3.9.6]
* pip [21.1.3]

### Docker

* Docker [20.10.8]

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

#### Build [Optional]

```bash
git clone https://github.com/Maxitosh/devops
cd devops/app_python
docker build --tag maxitosh/devops_web_app .  
```

## Usage

### Source code

#### 1. Create and activate virtual environment

```bash
cd devops/app_python
python3 -m virtualenv venv 
source venv/bin/activate
```

#### 2. Install requirements

```bash
pip install -r requirements.txt
```

#### 3. Run application

```bash
gunicorn -b 0.0.0.0:80 server:process_http_request  
```

### Docker

#### Run application

```bash
docker run -p "80:80" --name devops_web_app maxitosh/devops_web_app
```

## Test

Application will be available at [127.0.0.1](http://127.0.0.1:80)

## Contributing

Pull requests are welcome.

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Author

Kureikin Max BS18-SB  
Telegram: @Maxitosh
