
# Testing

### VirtualBox

> Mac OS X

~~~
brew cask install virtualbox
brew cask install virtualbox-extension-pack
~~~

### Vagrant

> Mac OS X

~~~
brew cask install vagrant
~~~

### Vagrant-Manager

> Mac OS X

~~~
brew cask install vagrant-manager
~~~

## Running Tests

### All Platforms

~~~
molecule test --platform=all
~~~

### Specific Platform

~~~
molecule test --platform=trusty64
molecule test --platform=xenial64
molecule test --platform=jessie64
molecule test --platform=stretch64
~~~

### Login

~~~
molecule login --host ansible-role-locale-timezone-trusty64
molecule login --host ansible-role-locale-timezone-xenial64
molecule login --host ansible-role-locale-timezone-jessie64
molecule login --host ansible-role-locale-timezone-stretch64
~~~

## Destroy, All Platforms

~~~
molecule destroy --platform=all
~~~
