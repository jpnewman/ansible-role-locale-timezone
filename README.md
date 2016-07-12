# jpnewman.locale-timezone

[![Ansible Role](https://img.shields.io/ansible/role/9596.svg?maxAge=2592000)](https://galaxy.ansible.com/jpnewman/locale-timezone/)
[![Build Status](https://travis-ci.org/jpnewman/ansible-role-locale-timezone.svg?branch=master)](https://travis-ci.org/jpnewman/ansible-role-locale-timezone)

This is a Ansible role to config local and timezone

## Requirements

Ansible 2.x

## Role Variables

|Variable|Description|Default|
|---|---|---|
|```locale```||en_GB.UTF-8|
|```timezone```||Etc/UTC|

## Dependencies

none

## Example Playbook

    - hosts: servers
      roles:
         - { role: jpnewman.locale-timezone, tags: ["init"] }

## License

MIT / BSD

## Author Information

John Paul Newman
