import sys
from launcher import start, opt_start
if len(sys.argv) <= 1:
    start()
else:
    bot_type = sys.argv[1]
    ind = sys.argv[2]
    opt_start(bot_type, int(ind))
