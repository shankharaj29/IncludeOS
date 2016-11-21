#!/usr/bin/python

import sys
import os

includeos_src = os.environ.get('INCLUDEOS_SRC',
                               os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))).split('/test')[0])
print 'includeos_src: {0}'.format(includeos_src)
sys.path.insert(0,includeos_src + "/test")
from subprocess import call

# Setup disk
call(["./make_disk.sh"], shell=True)

import vmrunner
vm = vmrunner.vms[0]
vm.make()

num_outputs = 0

def cleanup():
  vm.make(["clean"])

def increment(line):
  global num_outputs
  num_outputs += 1
  print "num_outputs after increment: ", num_outputs

def check_num_outputs(line):
  assert(num_outputs == 17)
  vmrunner.vms[0].exit(0, "SUCCESS")

vm.on_output("stat\(\) with nullptr buffer fails with EFAULT", increment)
vm.on_output("stat\(\) of folder that exists is ok", increment)
vm.on_output("chdir\(nullptr\) should fail", increment)
vm.on_output("chdir\(\"\"\) should fail", increment)
vm.on_output("chdir\(\) to a file should fail", increment)
vm.on_output("chdir to folder that exists is ok", increment)
vm.on_output("chdir\(\".\"\) is ok", increment)
vm.on_output("chdir to subfolder of cwd is ok", increment)
vm.on_output("getcwd\(\) with 0-size buffer should fail", increment)
vm.on_output("getcwd\(\) with nullptr buffer should fail", increment)
vm.on_output("getcwd\(\) with too small buffer should fail", increment)
vm.on_output("getcwd\(\) with adequate buffer is ok", increment)
vm.on_output("chmod\(\) should fail on read-only memdisk", increment)
vm.on_output("fchmod\(\) on non-open FD should fail", increment)
vm.on_output("nftw\(\) visits a directory before the directory's files", increment)
vm.on_output("nftw\(\) visits the directory's files before the directory when FTW_DEPTH is specified", increment)
vm.on_output("fstatat\(\) of file that exists is ok", increment)

vm.on_output("All done!", check_num_outputs)

vm.on_exit(cleanup)

# Boot the VM, taking a timeout as parameter
vm.boot(20)
