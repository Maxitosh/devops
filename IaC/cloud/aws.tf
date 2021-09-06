provider "aws" {
  region     = "us-east-2"
  access_key = var.aws_access_key_id
  secret_key = var.aws_secret_access_key
}

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "3.56.0"
    }
  }
}

resource "aws_key_pair" "pubkey" {
  key_name   = "devops-ssh-key"
  public_key = file(var.pubkey)
}

resource "aws_security_group" "app_security_group" {
  name        = "Application security group"
  description = "Allow ssh and app ports"

  ingress {
    description      = "ssh"
    from_port        = 22
    to_port          = 22
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  ingress {
    description      = "python_app"
    from_port        = 8000
    to_port          = 8000
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }


  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }
}

resource "aws_instance" "vm" {
  ami                         = "ami-0c55b159cbfafe1f0"
  instance_type               = "t2.micro"
  key_name                    = aws_key_pair.pubkey.key_name
  vpc_security_group_ids      = [aws_security_group.app_security_group.id]
  associate_public_ip_address = true

  tags = {
    Name = "lab-3-vm"
  }
}
