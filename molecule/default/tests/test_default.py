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

def test_accessconf_file(host):
    access = host.file("/etc/security/access.conf")
    assert access.contains("captain")
#    assert passwd.mode == 0o644

