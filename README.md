# Metrics Linux Server

## Description
Linux-metrics is a Python package that contains a module for extracting metrics about Linux Server and have packaged into the Docker container. Two main metrics are provided-processor (cpu) and memory (mem).

## Requirements
* installed Docker
* Python version 3

## Build and run Docker container
```bash
$ docker build -t lm .
```
Creat alias to run container
```bash
$ alias metrics="docker run -it --mount type=bind,source=/proc/stat,target=/proc/stat
```
Run alias with parametres "cpu" or "mem"
```bash
$ metrics cpu
CPU
procs running: 2
system cpu.idle: 23.81%
system cpu.user: 78.95%
system.cpu.iowait: 100.00%
system cpu.system: 97.49%

$ metrics mem
MEM
mem used: 6048309248
mem total: 16498290688
mem free: 5536702464
swap total: 16498290688
swap free: 5536702464
```



