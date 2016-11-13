from paramiko import SSHClient, AutoAddPolicy
from scp import SCPClient
import sys
import os
import git
from git import Repo
import keepassx

keepassFileName = 'main.kdbx'

################################################################################
################################################################################

def getValidKeepassDir():
    keepassDir = os.environ.get('KEEPASS_GIT_DIR')

    # Validate directory
    if keepassDir == None:
        print "Please define environment variable: KEEPASS_GIT_DIR"
        return None
    elif os.path.isdir(keepassDir) == None:
        print "Invalid path found in environment variable KEEPASS_GIT_DIR"
        return None

    if keepassDir[len(keepassDir)-1] == "/":
        keepassDir = keepassDir[:-1]
    return keepassDir

################################################################################
################################################################################

keepassDir = getValidKeepassDir()
if keepassDir == None:
    keepassDir = "."

# Git-init does not overwrite if the repo already contains content.
r = git.Repo.init(keepassDir)
kpDB = keepassx.db.Database()
# if os.path.isfile(keepassDir + "/" + keepassFileName):
#     r.index.add([keepassFileName])
#
#     # Find how to figure out what changed.
#     r.index.commit("Updated DB Entries")
# for (path, stage), entry in r.index.entries.items():  # @UnusedVariable
    # print path
    # print stage
    # print entry


# assert repo.bare


# rval = g.ls_files()

# todo: Where to instantiate a keepass dir if on does not already exist?


# todo: this will eventually be the desktop server config
# todo: eventually, figure out a way to not hard-code this config.
# androidConfig = {
#     'host': '192.168.0.7',
#     'port': 2222,
#     'user': 'u0_a119'
# }

# client = SSHClient()
# client.load_system_host_keys();
# client.set_missing_host_key_policy(AutoAddPolicy())
# client.connect(androidConfig['host'], androidConfig['port'], androidConfig['user'])

# SCPCLient takes a paramiko transport as its only argument
# scp = SCPClient(client.get_transport())

# scp.put('test.txt', 'test2.txt')

# Check to see the file is there
# stdin, stdout, stderr = client.exec_command('ls -l')
# for line in stdout:
#     print line

# Close down connections
# scp.close()
# client.close()
