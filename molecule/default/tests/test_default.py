# coding: utf-8
from __future__ import annotations, unicode_literals

import os

import pytest
import testinfra.utils.ansible_runner
from helper.molecule import get_vars, infra_hosts, local_facts

testinfra_hosts = infra_hosts(host_name="instance")

# --- tests -----------------------------------------------------------------


def test_files(host, get_vars):
    """
    """
    files = [
        get_vars.get("chrony_config_file"),
        get_vars.get("chrony_system_config", {}).get("file")
    ]

    for file in files:
        f = host.file(file)
        assert f.exists
        assert f.is_file


def test_user(host, get_vars):
    """
    """
    user = get_vars.get("chrony_user")
    group = get_vars.get("chrony_group")

    assert host.group(group).exists
    assert host.user(user).exists
    assert group in host.user(user).groups


def test_service(host, get_vars):
    """
    """
    print(get_vars.get("chrony_defaults_service", {}))
    print(get_vars.get("chrony_defaults_service", {}).get("name"))
    service = host.service(
        get_vars.get("chrony_defaults_service", {}).get("name")
    )
    assert service.is_enabled
    assert service.is_running


def test_open_port(host, get_vars):
    """
    """
    # version = local_facts(host).get("major_version")

    for i in host.socket.get_listening_sockets():
        print(i)

    service = host.socket("udp://{0}:{1}".format("127.0.0.1", "323"))
    assert service.is_listening

    # if int(version) > 3:
    #     service = host.socket("udp://{0}:{1}".format("0.0.0.0", "123"))
    #     assert service.is_listening
