清理 Docker 无用资源

```
docker system prune
```

修剪镜像、容器和网络，和卷的快捷方式

```
docker system prune --volumes
```

清理none镜像(虚悬镜像,默认情况下，docker image prune 命令只会清理 虚无镜像（没被标记且没被其它任何镜像引用的镜像）)

```
docker image prune 
```

清理无容器使用的镜像

```
docker image prune -a
docker image prune -a --filter "until=24h" # 清理 24 小时前创建的镜像
```

清理停止的容器，无用的所有容器

```
docker container prune
```

清理没有被容器未使用的网络

```
docker network prune
```

清理卷！！！卷可以被一个或多个容器使用，并占用 Docker 主机上的空间。卷永远不会被自动删除，因为这么做会破坏数据。

```
docker volume prune
```

```
docker rm $(docker ps -a | awk '{ print $1}' | tail -n +2)
docker start $(docker ps -a | awk '{ print $1}' | tail -n +2)
docker stop $(docker ps -a | awk '{ print $1}' | tail -n +2)
docker restart $(docker ps -a | awk '{ print $1}' | tail -n +2)
```