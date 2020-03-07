#!/usr/bin/env python
#
#  Copyright (c) 2011-2013 Corey Goldberg (http://goldb.org)
#
#  This file is part of linux-metrics
#
#  License :: OSI Approved :: MIT License:
#      http://www.opensource.org/licenses/mit-license
#
#      Permission is hereby granted, free of charge, to any person obtaining a copy
#      of this software and associated documentation files (the "Software"), to deal
#      in the Software without restriction, including without limitation the rights
#      to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#      copies of the Software, and to permit persons to whom the Software is
#      furnished to do so, subject to the following conditions:
#
#      The above copyright notice and this permission notice shall be included in
#      all copies or substantial portions of the Software.
#


""" example usage of linux-metrics """


import linux_metrics as lm
import sys




def main(metric='cpu'):
    if metric == 'cpu':
        print ("CPU")
        # cpu
        print('procs running: %d' % lm.cpu_stat.procs_running())
        cpu_pcts = lm.cpu_stat.cpu_percents(sample_duration=1)
        print('system cpu.idle: %.2f%%' % (100 - cpu_pcts['idle']))
        print('system cpu.user: %.2f%%' % (100 - cpu_pcts['user']))
        print('system.cpu.iowait: %.2f%%' % (100 - cpu_pcts['iowait']))
        print('system cpu.system: %.2f%%' % (100 - cpu_pcts['system']))
        #print('system cpu.guest: %.2f%%' % (100 - cpu_pcts['guest']))
        #print('system cpu.stolen: %.2f%%' % (100 - cpu_pcts['stolen']))

    elif metric == 'mem':
        print ("MEM")
        # memory
        used, total, free, _, _, _ = lm.mem_stat.mem_stats()
        print('mem used: %s' % used)
        print('mem total: %s' % total)
        print('mem free: %s' %  free)
        print('swap total: %s' % total)
        print('swap free: %s' % free)


if __name__ == '__main__':
    try:
        main(str(sys.argv[1]))
    except:
        print("Pls provide arg cpu/mem")
