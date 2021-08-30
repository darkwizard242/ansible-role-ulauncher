import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


PACKAGE = 'ulauncher'
PACKAGE_BINARY = '/usr/bin/ulauncher'


def test_ulauncher_package_installed(host):
    """
    Tests if ulauncher is installed
    """
    assert host.package(PACKAGE).is_installed


def test_ulauncher_binary_exists(host):
    """
    Tests if ulauncher binary exists.
    """
    assert host.file(PACKAGE_BINARY).exists


def test_ulauncher_binary_file(host):
    """
    Tests if ulauncher binary is file type.
    """
    assert host.file(PACKAGE_BINARY).is_file


def test_ulauncher_binary_which(host):
    """
    Tests the output to confirm ulauncher's binary location.
    """
    assert host.check_output('which ulauncher') == PACKAGE_BINARY
