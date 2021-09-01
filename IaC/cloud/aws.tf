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
resource "aws_instance" "vm" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"

  tags = {
    Name = "lab-3-vm"
  }
}
