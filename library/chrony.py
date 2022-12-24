#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# (c) 2020-2022, Bodo Schulz <bodo@boone-schulz.de>
# BSD 2-clause (see LICENSE or https://opensource.org/licenses/BSD-2-Clause)

from __future__ import absolute_import, print_function

import re

from ansible.module_utils.basic import AnsibleModule


class ChronyCmd(object):
    module = None

    def __init__(self, module):
        """
          Initialize all needed Variables
        """
        self.module = module

        self.command    = module.params.get("command")
        self.parameters = module.params.get("parameters")

        self._syslog_ng_bin = module.get_bin_path(self.command, True)

    def run(self):
        ''' ... '''
        result = dict(
            failed=True,
            ansible_module_results='failed'
        )

        parameter_list = self._flatten_parameter()

        if not self._syslog_ng_bin:
            return dict(
                rc = 1,
                failed = True,
                msg = "no installed chrony found"
            )

        args = []
        args.append(self._syslog_ng_bin)

        if len(parameter_list) > 0:
            for arg in parameter_list:
                args.append(arg)

        self.module.log(msg=f" - args {args}")

        rc, out, err = self._exec(args)

        if '--version' in parameter_list:
            """
              get version"
            """
            pattern = re.compile(r'^chronyd.*version (?P<version>\d+(\.\d+){0,2}(\.\*)?) .*', re.MULTILINE)
            version = re.search(pattern, out)
            version = version.group('version')

            major_version = version.split('.')[0]

            # self.module.log(msg=f"   version: '{version}'")
            # self.module.log(msg=f"   major_version: '{major_version}'")

            if (rc == 0):
                return dict(
                    rc = 0,
                    failed = False,
                    args = args,
                    version = version,
                    major_version = major_version
                )

        return result

    def _exec(self, args):
        """
        """
        rc, out, err = self.module.run_command(args, check_rc=True)
        # self.module.log(msg="  rc : '{}'".format(rc))
        # self.module.log(msg="  out: '{}' ({})".format(out, type(out)))
        # self.module.log(msg="  err: '{}'".format(err))
        return rc, out, err

    def _flatten_parameter(self):
        """
          split and flatten parameter list

          input:  ['--validate', '--log-level debug']
          output: ['--validate', '--log-level', 'debug']
        """
        parameters = []

        for _parameter in self.parameters:
            if ' ' in _parameter:
                _list = _parameter.split(' ')
                for _element in _list:
                    parameters.append(_element)
            else:
                parameters.append(_parameter)

        return parameters

# ===========================================
# Module execution.
#


def main():

    module = AnsibleModule(
        argument_spec=dict(
            command=dict(
                required=True,
                type='str'
            ),
            parameters=dict(
                required=True,
                type='list'
            ),
        ),
        supports_check_mode=True,
    )

    c = ChronyCmd(module)
    result = c.run()

    module.exit_json(**result)


# import module snippets
if __name__ == '__main__':
    main()
