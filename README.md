## xsh 

A simple ssh wrapper to make ssh tunneling easier.

## Why and examples ?

```bash
ssh remotehost -o ProxyCommand="ssh jumpbox nc %h %p"
```

can be simplfied as

```bash
xsh remotehost -j jumpbox
```

And by default, it will retry 50 times unless you add `--failfast` flag, which stop it after first try.

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

And if you happend want to access a box with user named `tom`, simply do `xsh tom@tomsbox` would always bypass `XSH_USER` environment variable.

## Installation

Too simple, just wget it to your anywhere in your [PATH](https://en.wikipedia.org/wiki/PATH_(variable)), and don't forget [chmod](https://en.wikipedia.org/wiki/Chmod) it.
