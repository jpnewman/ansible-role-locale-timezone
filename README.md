# jpnewman.locale-timezone

This is a Ansible role to config

## Requirements

Ansible 2.x

## Role Variables

|Variable|Description|Default|
|---|---|---|
|```locale```||en_GB.UTF-8|
|```timezone```||Europe/London|

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
