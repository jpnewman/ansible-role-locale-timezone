"""Timezone Specs."""

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_python_package(host):
    """Test Python is installed."""
    python = host.package('python')
    assert python.is_installed


def test_timezone(host):
    """Test Timezone."""
    timezone = host.command('cat /etc/timezone')
    assert timezone.stdout == 'Etc/UTC'


def test_timedatectl(host):
    """Test timedatectl."""
    timezone = host.command(r'timedatectl | grep -E "Time\s{0,1}zone"')
    assert 'Etc/UTC' in timezone.stdout
