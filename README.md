
# Ansible Role:  `chrony`

Ansible role to install and configure chrony on various linux systems.

## Requirements & Dependencies


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
```

[example](molecule/default/group_vars/all/vars.yml)
    
    
## Contribution

Please read [Contribution](CONTRIBUTING.md)

## Development,  Branches (Git Tags)

The `master` Branch is my *Working Horse* includes the "latest, hot shit" and can be complete broken!

If you want to use something stable, please use a [Tagged Version](https://gitlab.com/bodsch/ansible-dovecot/-/tags)!


## Author

- Bodo Schulz

## License

[Apache](LICENSE)

`FREE SOFTWARE, HELL YEAH!`
    
