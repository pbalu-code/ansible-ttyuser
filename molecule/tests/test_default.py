
def test_passwd_file(host):
    passwd = host.file("/etc/passwd")
    assert passwd.contains("captain")
    assert passwd.user == "root"
    assert passwd.group == "root"
    assert passwd.mode == 0o644

def test_sudoers_file(host):
    sudoers = host.file("/etc/sudoers")
    assert sudoers.contains("captain")
#    assert passwd.mode == 0o644

def test_user(host):
    user = host.user("captain")
    assert user.exists
    assert user.name == "captain"
    #assert user.uid == 1001
    #assert user.gid == 65534
    assert user.group == "captain"
    #assert user.gids == [65534]
    assert user.groups == ["captain"]
    assert user.shell == "/bin/bash"
    assert user.home == "/home/captain"
    assert user.password != "!"

def test_accessconf_file(host):
    access = host.file("/etc/security/access.conf")
    assert access.contains("captain")
#    assert passwd.mode == 0o644

def test_ssh_installed(host):
    assert not host.package('zsh').is_installed
    if host.system_info.distribution in ("alpine", "archlinux"):
        name = "openssh"
    else:
        name = "openssh-server"
    ssh = host.package(name)
    assert ssh.is_installed

def test_ssh_running(host):
    if host.system_info.distribution in ("centos", "fedora"):
        name = "sshd"
    else:
        name = "ssh"
    service = host.service(name)
    assert service.is_running
    assert service.is_enabled

def test_ssh_listening(host):
    ssh = host.socket('tcp://0.0.0.0:22')
    assert ssh.is_listening