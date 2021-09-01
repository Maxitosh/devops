## Best practices for Vagrant

* If you want to apply a slightly different configuration to many multi-machine machines, you can use a loop to do this.
* Overwrite host locale in ssh session Usually, host locale environment variables are passed to guest. It may cause
  failures if the guest software do not support host locale.
* Just read the awesome documentation at https://www.vagrantup.com/docs
