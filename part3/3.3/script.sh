echo "enter github url:"
read url
git clone $url repo
cd repo
echo "enter image name:"
read  image
docker build -t $image .
docker login
docker push $image
