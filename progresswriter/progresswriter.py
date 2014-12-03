from sys import stdout


class ProgressWriter:
    """
    A utility to show the progress of long processes. A common use case would
    be to initialize, then in the loop, call show_progress() with the index
    of the position in the loop, and then after the loop, call end_progress().
    """

    def __init__(self, prestring, total, should_show):
        """
        :param prestring {string}
        :param total {number}
        :param should_show {boolean}
        """
        self.prestring = prestring
        self.total = total
        self.should_show = should_show
        self.ix = 0

    def increment_progress(self):
        """
        Does nothing if self.should_show is False. Otherwise,
        Shows the progress with self.ix / self.total % complete, then
        increments self.ix by 1.

        Good to call at the begginning of each loop.
        """
        if not self.should_show:
            return
        percent = self.ix / float(self.total) * 100
        stdout.write('\r%s...%.2f%% Complete' % (self.prestring, percent))
        self.ix += 1

    def show_progress(self, count):
        """
        Does nothing if self.should_show is false. Otherwise prints the
        following string:

        {PRESTRING}...{PERCENT}% Complete

        where percent is 100 * count / self.total

        :post Sets self.ix = count
        """
        if not self.should_show:
            return
        self.ix = count
        percent = count / float(self.total) * 100
        stdout.write('\r%s...%.2f%% Complete' % (self.prestring, percent))

    def end_progress(self):
        """
        Does nothing if self.should_show is false. Otherwise prints the
        following string:

        {PRESTRING}...Done
        """
        if not self.should_show:
            return
        stdout.write('\r%s...Done\n' % self.prestring)
