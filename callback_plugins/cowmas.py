import random
from ansible.plugins.callback.default import CallbackModule
from ansible.utils.color import stringc
from ansible import constants as C
from ansible.utils.display import Display


all_colors = [C.COLOR_CHANGED, C.COLOR_DEBUG, C.COLOR_DEPRECATE, C.COLOR_DIFF_ADD, C.COLOR_DIFF_LINES,
              C.COLOR_DIFF_REMOVE, C.COLOR_ERROR, C.COLOR_HIGHLIGHT, C.COLOR_OK, C.COLOR_SKIP, C.COLOR_UNREACHABLE,
              C.COLOR_VERBOSE, C.COLOR_WARN]


def colorize(txt, color=None):
    output = ''
    if color is None:
        # rand_start = random.randint(0, len(all_colors))
        for (idx, char) in enumerate(txt):
            output += stringc(char, random.sample(all_colors, 1)[0])
            # output += stringc(char, all_colors[(rand_start + idx) % len(all_colors)])
    else:
        output += stringc(txt, color)
    return output


def colorize_lights(light_len=3):
    '''Convert white lights to colored lights of the desired length.'''
    # Credit http://www.chris.com/ascii/index.php?art=holiday/christmas/other
    # .:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:.

    # size the lights appropriately
    white_lights = u".:*~*:._" * light_len
    white_lights = white_lights[:light_len - 8]

    # swap out bulbs with some colored bulbs
    colored_lights = ''
    for light in white_lights:
        if light in ['*', '_']:
            colored_lights += colorize(light)
        else:
            colored_lights += light
    return colored_lights

# http://www.chris.com/ascii/index.php?art=holiday/christmas/other
# .:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:.
# -=[ The Twelve Days of Christmas ]=- 12/96
# .:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:.


# http://www.chris.com/ascii/index.php?art=holiday/christmas/other
#          .--._.--.--.__.--.--.__.--.--.__.--.--._.--.
#        _(_      _Y_      _Y_      _Y_      _Y_      _)_
#       [___]    [___]    [___]    [___]    [___]    [___]
#       /:' \    /:' \    /:' \    /:' \    /:' \    /:' \
#      |::   |  |::   |  |::   |  |::   |  |::   |  |::   |
#      \::.  /  \::.  /  \::.  /  \::.  /  \::.  /  \::.  /
#  jgs  \::./    \::./    \::./    \::./    \::./    \::./
#        '='      '='      '='      '='      '='      '='

class LightDisplay(Display):

    def banner(self, msg, color=None, cows=True):
        '''
        Prints a holiday themed header depending on terminal width (3 minimum)
        '''
        if self.b_cowsay and cows:
            try:
                self.banner_cowsay(msg)
                return
            except OSError:
                self.warning("somebody cleverly deleted cowsay or something during the PB run.  heh.")

        msg = msg.strip()
        light_len = max(3, self.columns - len(msg))
        self.display(u"\n%s %s" % (msg, colorize_lights(light_len)))

        # self.display(u"\n")
        # self.display(u"%s" % colorize_lights())
        # self.display(u"-= %s =-" % msg, color=color)
        # self.display(u"%s" % colorize_lights())


class CallbackModule(CallbackModule):

    CALLBACK_VERSION = 2.0
    CALLBACK_TYPE = 'stdout'
    CALLBACK_NAME = 'cowmas'
    CALLBACK_NEEDS_WHITELIST = True

    def __init__(self, display=None, options=None):
        super(CallbackModule, self).__init__()
        self._display = LightDisplay()

    def v2_playbook_on_stats(self, stats):
        super(CallbackModule, self).v2_playbook_on_stats(stats)
        print colorize("HAPPY AUTOMATING TO ALL!\n")

        if len(stats.failures):
            force_color = C.COLOR_ERROR
        elif len(stats.dark):
            force_color = C.COLOR_UNREACHABLE
        elif len(stats.changed):
            force_color = C.COLOR_HIGHLIGHT
        else:
            force_color = None

        print colorize('''
*           *
                                *
    \/ \/  \/ \/
 *    \/    \/      *
      (A)  (A)
       \ ^^ /            *
       (o)(o)--)---------\.
       |    |          A  \\
        \__/             ,|  *
 *        ||-||\.____./|| |
          || ||     || || A      *
   *      <> <>     <> <>
                   ''', force_color)
