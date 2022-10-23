Simple Python Flask to sum of two numbers

Steps to run:-

1. Download Docker on your host
2. Start the docker service
3. Clone the repository on your workspace
```
git clone https://github.com/jayramr/simple-addition.git
```
4. Navigate to the code directory
5. Create the image build
```
docker build -t <name-of-image>  .
```
6. Start the container
```
docker run -p 80:80 <name-of-image>
```
7. Launch browser and hit "localhost"
