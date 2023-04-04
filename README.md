
# Ansible Role:  `chrony`

Ansible role to install and configure chrony on various linux systems.

[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/bodsch/ansible-chrony/main.yml?branch=main)][ci]
[![GitHub issues](https://img.shields.io/github/issues/bodsch/ansible-chrony)][issues]
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/bodsch/ansible-chrony)][releases]
[![Ansible Quality Score](https://img.shields.io/ansible/quality/50067?label=role%20quality)][quality]

[ci]: https://github.com/bodsch/ansible-chrony/actions
[issues]: https://github.com/bodsch/ansible-chrony/issues?q=is%3Aopen+is%3Aissue
[releases]: https://github.com/bodsch/ansible-chrony/releases
[quality]: https://galaxy.ansible.com/bodsch/chrony

## Requirements & Dependencies

Ansible Collections

- [bodsch.core](https://github.com/bodsch/ansible-collection-core)

```bash
ansible-galaxy collection install bodsch.core
```
or
```bash
ansible-galaxy collection install --requirements-file collections.yml
```

### Operating systems

Tested on

* Arch Linux
* Debian based
    - Debian 10 / 11
    - Ubuntu 20.10
* RedHat based
    - Alma Linux 8
    - Rocky Linux 8
    - Oracle Linux 8

## Configuration

```yaml
chrony_service: {}

chrony_config: {}

chrony_daemon_args: {}
```

#### defaults

```yaml
chrony_service:
  name: chrony
  executable: /usr/sbin/chronyd
  state: started
  enable: true

chrony_config:
  conf_directory: /etc/chrony/conf.d
  log:
    types: []
    #  - tracking
    #  - measurements
    #  - statistics
    directory: /var/log/chrony
  drift_file: /var/lib/chrony/chrony.drift
  key_file: /etc/chrony/chrony.keys
  nts_dump_directory: /var/lib/chrony
  source_directories: []
  #  - /run/chrony-dhcp
  #  - /etc/chrony/sources.d
  ntp_servers: []
  ntp_pools:
    - pool.ntp.org iburst maxpoll 10
  ntp_peers: []
  makestep:
    threshold: 1
    limit: 10
  rtc:
    sync: true
    on_utc: true
  leap_sec_tz: right/UTC
  bind_cmd_addresses:
    - 127.0.0.1
    - ::1
  allow: []
  deny: []

chrony_daemon_args:
  # -4
  use_ipv4_only: ""  # | true / false
  # -6
  use_ipv6_only: ""  # | true / false
  # -n
  run_as_daemon: ""  # | true / false
  # -d
  run_as_daemon_and_log_to_stderr: ""  # | true / false
  # -L level
  # 0 (informational), 1 (warning), 2 (non-fatal error), and 3 (fatal error)
  logging_threshold: 0  # | 0
  # -r
  reload_dump_files: true
  # -F level
  # Three levels are defined: 0, 1, 2.
  seccomp_filter_level: 2
  # -P priority
  process_priority: 0
  # -m
  lock_memory: ""  # | true / false
  # -x
  control_clock: ""  # | true / false
  # -u USER       Specify user (_chrony)
  run_as_user: "{{ chrony_user }}"
  # -U
  dont_check_for_root: ""  # | true / false
```


[example](molecule/default/group_vars/all/vars.yml)

    
## Contribution

Please read [Contribution](CONTRIBUTING.md)

## Development,  Branches (Git Tags)

The `master` Branch is my *Working Horse* includes the "latest, hot shit" and can be complete broken!

If you want to use something stable, please use a [Tagged Version](https://github.com/bodsch/ansible-chrony/tags)!


## Author

- Bodo Schulz

## License

[Apache](LICENSE)

`FREE SOFTWARE, HELL YEAH!`
    
