variable "aws_access_key_id" {
  type        = string
  description = "AWS access key id"
}

variable "aws_secret_access_key" {
  type    = string
  default = "AWS secret key"
}

variable "pubkey" {
  type        = string
  description = "Public ssh key"
  default     = "ssh-rsa "
}
