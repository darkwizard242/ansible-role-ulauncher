[![build-test](https://github.com/darkwizard242/ansible-role-ulauncher/workflows/build-and-test/badge.svg?branch=master)](https://github.com/darkwizard242/ansible-role-ulauncher/actions?query=workflow%3Abuild-and-test) [![release](https://github.com/darkwizard242/ansible-role-ulauncher/workflows/release/badge.svg)](https://github.com/darkwizard242/ansible-role-ulauncher/actions?query=workflow%3Arelease) ![Ansible Role](https://img.shields.io/ansible/role/d/darkwizard242/ulauncher) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-ulauncher&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=ansible-role-ulauncher) [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-ulauncher&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=ansible-role-ulauncher) [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-ulauncher&metric=security_rating)](https://sonarcloud.io/dashboard?id=ansible-role-ulauncher) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-ulauncher?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-ulauncher?color=orange&style=flat-square)

# Ansible Role: ulauncher

Role to install (_by default_) [ulauncher](https://ulauncher.io/) package or uninstall (_if passed as var_) on **Ubuntu** systems..

## Requirements

None.

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

### Variables list:

```yaml
ulauncher_repo: 'ppa:agornostal/ulauncher'
ulauncher_repo_desired_state: present
ulauncher_repo_filename: ulauncher
ulauncher_app: ulauncher
ulauncher_package_desired_state: present
```

### Variables table:

Variable                        | Description
------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------
ulauncher_repo                  | Refers to the ppa repo to add.
ulauncher_repo_desired_state    | Defined to dynamically chose whether to add/keep (i.e. `present`) or remove (i.e. `absent`) the repository file list from `/etc/apt/sources.list.d`.
ulauncher_repo_filename         | Defined to set the repository file name for saving in `/etc/apt/sources.list.d`
ulauncher_app                   | Defines the app to install i.e. **ulauncher**
ulauncher_package_desired_state | Defined to dynamically chose whether to install (i.e. either `present` or `latest`) or uninstall (i.e. `absent`) the package. Default is set to `present`.

## Dependencies

None

## Example Playbook

For default behaviour of role (i.e. installation of **ulauncher** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.ulauncher
```

For customizing behavior of role (i.e. installation of latest **ulauncher** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.ulauncher
  vars:
    ulauncher_package_desired_state: latest
```

For customizing behavior of role (i.e. un-installation of **ulauncher** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.ulauncher
  vars:
    ulauncher_package_desired_state: absent
```

## License

[MIT](https://github.com/darkwizard242/ansible-role-ulauncher/blob/master/LICENSE)

## Author Information

This role was created by [Ali Muhammad](https://www.alimuhammad.dev/).
