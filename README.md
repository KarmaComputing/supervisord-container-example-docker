# Supervisord Container Dockerfile Example

## Configure

> `echo_supervisord_conf` exists to generate a sample config :D 
http://supervisord.org/installing.html#creating-a-configuration-file

## Build
```
./build.sh
```

### Run
```
docker run -it --entrypoint=/bin/bash test
```

Type `supervisord --nodaemon`


