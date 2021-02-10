#!/usr/bin/env ../tests/libs/bats/bin/bats
load 'libs/bats-support/load'
load 'libs/bats-assert/load'

setup() {
  echo "Test has started"
  echo "IP address: " $SUT_IP
}

teardown() {
echo "Test - End"
}

@test 'Teszt SSH and users' {
assert_equal $(sshpass -p 'passwordTest' ssh captain@${SUT_IP} -C -o ControlMaster=auto -o ControlPersist=60s -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no \
 cat /etc/passwd | grep -E '^captain|^bela' | wc -l ) '2'
}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]
then
  run_main
  if [ $? -gt 0 ]
  then
    exit 1
  fi
fi