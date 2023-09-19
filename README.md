# ansible users role
______________________

Version: 1.4.0
Ansible driven mass local user and group creation and management role.

Tested with (Molecule):  
Vagrant:  
- Ubuntu
- Debian
- Centos

Docker:  
- Ubuntu
- Centos

Ansible:
- 2.9
- 2.10
- 3.0

Manually tested on:
OpenSUSE


## Warning - For OpenSUSE the user's primary group must be defined in the `TTYUSER_users ` if it is necessary should be created before by `TTYUSER_groups`
OpenSUSE is not create primary group automatically, it use the 'users' group as default. - Not recommended


Variables:

`TTYUSER_groups ` List of groups to create #1
`TTYUSER_users ` List of dictionaries #2
`TTYUSER_sudoers ` List of users to add sudoers with nopasswd
`TTYUSER_revoke_sudoers ` List of users to remove from sudoers
`TTYUSER_sshkey_size ` Global variable for key size (default 521)
`TTYUSER_sshkey_type`  Global variable for key type (default: ecdsa )
`TTYUSER_usesudopass`  Global variable to force password usage at sudo (>= v1.4.0)

TTYUSER_sshkey_size
Example:  
###Add user
```yaml
TTYUSER_users:  
  - name: captain
    state: present #optional
    shell: /bin/bash #optional 
    password: "{{ 'password123' | password_hash('sha512') }}"  #optional
    keypass: xcvbn123 # Password for the SSH key what is to be created
    group: skipper #optional*
    groups:   #optional with auto append
      - sudo
      - admin
      - private
    pubkeys: "ssh-rsa xxxxxxxxxxxxxxx capt@host
      ssh-ed25519 xcvbn12345 capt@host2"
    update_password: "always" #  default: 'on_create'
    password_lock: 'no' # default: 'no'
    append: "yes/no" # default: 'yes' if you have more groups to add
    home: '/home/bluebread' # optional
    uid: 1003 # optional
    remove: "{{ item.remove_homedir | default('no') }}"
    skip_keygen: false  # Disable key generation default: false
    comment: Demo User  # Optional 
    password_expire_max: 2 # optional - Maximum number of days between password change.
    password_expire_min: 100 # optional - Minimum number of days between password change.
    # hardcoded: force: yes
TTYUSER_sudoers:
  - captain

TTYUSER_groups:
  - name: skipper
    gid: 1003
  - name: private
    system: false  # Set group as system user optional. Default: false

TTYUSER_revoke_sudoers: []

```
###Remove user:
```yaml
TTYUSER_users:  
  - name: captain
    state: absent
    remove_homedir: yes

TTYUSER_sudoers:: []

TTYUSER_revoke_sudoers: 
  - captain

```

#Molecule 

Run test with default vagrant driver/backend  
`molecule test`

Run test with docker driver/backend  
`molecule test -s docker`  

##Molecule command:  

molecule <command> [parameters]

__dependency:__ Pull dependencies from ansible-galaxy if the role requires them.  
__lint:__ Check all the YAML files with yamllint.  
__cleanup:__ Executes the cleanup.yml playbook if exists.  
__destroy:__ If there is a VM with the same name running, destroy it.  
__syntax:__ Check the role with ansible-lint.  
__create:__ Create the VM/docker/ect.. Use the provisioner to start the instances.   
__prepare:__ Executes the prepare.yml playbook, which brings the host to a specific state.  
__converge:__ Executes the converge.yml playbook, which runs the role.  
__idempotence:__ Molecule runs the playbook a second time to check for idempotence.  
__verify:__ Run the tests defined in the tests directory.  
__cleanup:__ Executes the cleanup.yml playbook if exists.  
__destroy:__ Destroy the VM.  
__check:__       Use the provisioner to perform a Dry-Run (destroy, dependency, create, prepare, converge).  
__drivers:__      List drivers.  
__init:__         Initialize a new role or scenario.  
__lint:__         Lint the role (dependency, lint).  
__list:__         List status of instances.  
__login:__        Log in to one instance.  
__matrix:__       List matrix of steps used to test instances.  
__reset:__        Reset molecule temporary folders.  
__side-effect:__  Use the provisioner to perform side-effects to the instances.  
__test:__         Test (dependency, lint, cleanup, destroy, syntax, create, prepare, converge, idempotence, side_effect, verify, cleanup, destroy).  


## Release  note:  
1.4.0 - Option to drive user settings in sudoers with or without password
1.3.1 - Suppress logs when the task manage passwords
      password_expire min/max support

1.3 - Support the most of functionality of the ansible user modul
      Group management (guid, name, system)
      Slurp SSH keys into inventor_dir/files
      

