## xsh 

A simple ssh wrapper to make ssh tunneling easier.

## Why and examples ?

When you have a remotehost to connect but you have to go through a jumpbox, you can do

```bash
ssh remotehost -o ProxyCommand="ssh jumpbox nc %h %p"
```
But I always have trouble in memorizing ProxyCommand, so I implement `xsh` and that allows you do simply that as

```bash
xsh remotehost -j jumpbox
```

And by default, it will retry 50 times unless you add `--failfast` flag, which will stop it after first try.

If you are uncertain what it pass to `ssh` command, you can always add a `--dry` flag.

```bash
$> xsh remotehost -j jumpbox --dry
[DRY] Calling: ssh remotehost -o ProxyCommand="ssh jumpbox nc %h %p"
```

If your remotehost doesn't have same username as your computer, and you can do

```#bash
$> xsh user@remotehost
```

If you have a bunch server and they all have a username, let say `ubuntu`.

```#bash
# add this to your ~/.bash_profile
$> export XSH_USER=ubuntu
```

And `xsh remotehost` would be equivalent to `ssh ubuntu@remotehost`

And if you happend want to access a box with user named `tom`. To override `XSH_USER`, just simply do 

```bash
$> xsh tom@tomsbox
```

## Installation

Too simple, just wget it to your anywhere in your [PATH](https://en.wikipedia.org/wiki/PATH_(variable)), and don't forget [chmod](https://en.wikipedia.org/wiki/Chmod) it.

That can be done with following command
```bash
$> wget https://raw.githubusercontent.com/tly1980/xsh/master/src/xsh.py -O /usr/local/bin/xsh
$> chmod a+x /usr/local/bin/xsh
```


