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
docker run --rm -v $PWD:/app/src -p 5000:5000 --name test test
```

Type `supervisord --nodaemon`


