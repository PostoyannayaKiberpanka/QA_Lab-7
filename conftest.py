import paramiko
import subprocess
import pytest

server_ip = '192.168.4.122'
port = '22'
username = 'igor'
password = '123'


@pytest.fixture(scope='function')
def server():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=server_ip, port=port, username=username, password=password)
    stdin, stdout, stderr = ssh.exec_command('iperf3 -s -1')
    print(f"Created iperf3 server on {server_ip}")
    ssh.close()

    return ssh


@pytest.fixture(scope='function')
def client(server):
    result = subprocess.run(f'iperf3 -c {server_ip}', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                            text=True)

    return result.stdout, result.stderr
