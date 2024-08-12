# Stop and remove all containers
docker rm -f $(docker ps -aq)

# Remove all images
docker rmi -f $(docker images -q)

# Remove all volumes
docker volume rm $(docker volume ls -q)

# Remove all networks (excluding default ones)
docker network rm $(docker network ls | grep -v "bridge\|host\|none" | awk '{if(NR>1)print $1}')

echo "ALL CLEAN"
date