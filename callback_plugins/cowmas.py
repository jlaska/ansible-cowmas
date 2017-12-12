from ansible.plugins.callback.default import CallbackModule
from ansible.utils.color import stringc
from ansible import constants as C

all_colors = [C.COLOR_CHANGED, C.COLOR_DEBUG, C.COLOR_DEPRECATE, C.COLOR_DIFF_ADD, C.COLOR_DIFF_LINES,
              C.COLOR_DIFF_REMOVE, C.COLOR_ERROR, C.COLOR_HIGHLIGHT, C.COLOR_OK, C.COLOR_SKIP, C.COLOR_UNREACHABLE,
              C.COLOR_VERBOSE, C.COLOR_WARN]


def colorize(txt, color=None):
    output = ''
    if color is None:
        for (idx, char) in enumerate(txt):
            output += stringc(char, all_colors[idx % len(all_colors)])
    else:
        output += stringc(txt, color)
    return output


class CallbackModule(CallbackModule):

    CALLBACK_VERSION = 2.0
    CALLBACK_TYPE = 'stdout'
    CALLBACK_NAME = 'cowmas'
    CALLBACK_NEEDS_WHITELIST = True

    def v2_playbook_on_stats(self, stats):
        super(CallbackModule, self).v2_playbook_on_stats(stats)
        print colorize("Happy Holidays from team Ansible!\n")

        if len(stats.failures):
            force_color = C.COLOR_ERROR
        elif len(stats.dark):
            force_color = C.COLOR_UNREACHABLE
        else:
            force_color = None

        print colorize('''
*           *
                                *
    \/ \/  \/ \/
 *    \/    \/      *
      (A)  (A)
       \ ^^ / 			 *
       (o)(o)--)---------\.
       |    |          A  \\
        \__/             ,|  *
 *        ||-||\.____./|| |
          || ||     || || A      *
   *      <> <>     <> <>
                   ''', force_color)
