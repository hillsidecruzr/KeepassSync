from paramiko import SSHClient, AutoAddPolicy
from scp import SCPClient
import sys

androidConfig = {
    'host': '192.168.0.7',
    'port': 2222,
    'user': 'u0_a119'
}

client = SSHClient()
client.load_system_host_keys();
client.set_missing_host_key_policy(AutoAddPolicy())
client.connect(androidConfig['host'], androidConfig['port'], androidConfig['user'])

# SCPCLient takes a paramiko transport as its only argument
scp = SCPClient(client.get_transport())

# scp.put('test.txt', 'test2.txt')

# Check to see the file is there
stdin, stdout, stderr = client.exec_command('ls -l')
for line in stdout:
    print line

# Close down connections
scp.close()
client.close()
