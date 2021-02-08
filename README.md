# ansible users role
______________________

Ansible driven mass local user creation and management role.

Tested with (Molecule):  
Vagrant:  
- Ubuntu
- Debian
- Centos

Docker:  
- Ubuntu
- Centos


Variables:

`users ` List of dictionaries
`sudoers ` List of users to add sudoers
`rewoke_sudoers ` List of users to remove from sudoers
Example:  
###Add user
```yaml
users:  
  - name: captain
    state: present #optional
    shell: /bin/bash #optional 
    password: "{{ 'password123' | password_hash('sha512') }}"  #optional
    group: captain #optional
    groups:   #optional with auto append
      - sudo
      - admin
    pubkeys: "ssh-rsa xxxxxxxxxxxxxxx capt@host
      ssh-ed25519 xcvbn12345 capt@host2"

sudoers:
  - captain

rewoke_sudoers: []

```
###Remove user:
```yaml
users:  
  - name: captain
    state: absent
    remove_homedir: yes

sudoers: []

rewoke_sudoers: 
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




