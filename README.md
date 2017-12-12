## Instructions

Use the provided `ansible.cfg` to add some holiday cheer to your ansible
playbooks.  For more advanced use of callback plugins, refer to [the
documentation](https://docs.ansible.com/ansible/devel/plugins/callback.html#enabling-callback-plugins).

## Example

```
$ ansible-playbook -i some.example.org, -c local hello_world.py

PLAY [Hello World Sample] ****************************************************

TASK [Gathering Facts] *******************************************************
ok: [some.example.org]

TASK [Hello Message] *********************************************************
ok: [some.example.org] => {
    "msg": "Hello World!"
}

PLAY RECAP *******************************************************************
some.example.org           : ok=2    changed=0    unreachable=0    failed=0

Happy Holidays from team Ansible!


*           *
                                *
    \/ \/  \/ \/
 *    \/    \/      *
      (A)  (A)
       \ ^^ / 			 *
       (o)(o)--)---------\.
       |    |          A  \
        \__/             ,|  *
 *        ||-||\.____./|| |
          || ||     || || A      *
   *      <> <>     <> <>

```

