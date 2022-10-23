Simple Python Flask to sum of two numbers

Steps to run:-

1. Download Docker on your host
2. Start the docker service
3. Clone the repository on your workspace
4. Create the image build
```
docker build -t <name-of-image>  .
```
5. Start the container
```
docker run -p 80:8080 <name-of-image>
```
6. Launch browser and hit "localhost"
