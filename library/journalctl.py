#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# (c) 2022, Bodo Schulz <bodo@boone-schulz.de>
# BSD 2-clause (see LICENSE or https://opensource.org/licenses/BSD-2-Clause)

from __future__ import absolute_import, division, print_function

from ansible.module_utils.basic import AnsibleModule


class JournalCtl(object):
    """
      Main Class
    """
    module = None

    def __init__(self, module):
        """
          Initialize all needed Variables
        """
        self.module = module

        self._journalctl = module.get_bin_path('journalctl', True)

        self.unit = module.params.get("unit")
        self.identifier = module.params.get("identifier")
        self.lines = module.params.get("lines")
        self.reverse = module.params.get("reverse")
        self.arguments = module.params.get("arguments")

        module.log(msg="----------------------------")
        module.log(msg=f" journalctl   : {self._journalctl}")
        module.log(msg=f" unit         : {self.unit}")
        module.log(msg=f" identifier   : {self.identifier}")
        module.log(msg=f" lines        : {self.lines}")
        module.log(msg=f" reverse      : {self.reverse}")
        module.log(msg=f" arguments    : {self.arguments}")
        module.log(msg="----------------------------")

    def run(self):
        """
          runner
        """
        result = dict(
            rc=1,
            failed=True,
            changed=False,
        )

        result = self.journalctl_lines()

        return result

    def journalctl_lines(self):
        """
            journalctl --help
            journalctl [OPTIONS...] [MATCHES...]

            Query the journal.

        """
        args = []
        args.append(self._journalctl)

        if self.unit:
            args.append("--unit")
            args.append(self.unit)

        if self.identifier:
            args.append("--identifier")
            args.append(self.identifier)

        if self.lines:
            args.append("--lines")
            args.append(str(self.lines))

        if self.reverse:
            args.append("--reverse")

        if len(self.arguments) > 0:
            for arg in self.arguments:
                args.append(arg)

        self.module.log(msg=f" - args {args}")

        rc, out, err = self._exec(args)

        return dict(
            rc=rc,
            cmd=" ".join(args),
            stdout=out,
            stderr=err,
        )

    def _exec(self, args):
        """
        """
        rc, out, err = self.module.run_command(args, check_rc=False)

        self.module.log(msg="  rc : '{}'".format(rc))
        self.module.log(msg="  out: '{}' ({})".format(out, type(out)))
        self.module.log(msg="  err: '{}'".format(err))
        return rc, out, err


# ===========================================
# Module execution.
#


def main():

    module = AnsibleModule(
        argument_spec=dict(
            identifier=dict(
                required=False,
                type="str"
            ),
            unit=dict(
                required=False,
                type="str"
            ),
            lines=dict(
                required=False,
                type='int'
            ),
            reverse=dict(
                required=False,
                default=False,
                type='bool'
            ),
            arguments=dict(
                required=False,
                default=[],
                type=list
            )
        ),
        supports_check_mode=True,
    )

    k = JournalCtl(module)
    result = k.run()

    module.log(msg="= result: {}".format(result))

    module.exit_json(**result)


# import module snippets
if __name__ == '__main__':
    main()
