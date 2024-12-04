Step 1-
Create Ubuntu VM on Cloud Platform
-------------------------------------------------------------------------------------------------------
Step 2-
Open Command line on that Ubuntu VM

Follow these Command 

Dockers Containerisation in Linux VM

1. Install Docker
   sudo apt update
   sudo apt install docker.io
   sudo systemctl start docker
   sudo systemctl enable docker

2. Clone the repository:
   git clone https://github.com/am-yash/cloud-project
   cd cloud-project

3. Build the Docker image:
   docker build -t flask-app

4. Resolve Docker daemon permission issues:
   sudo usermod -aG docker $USER
   newgrp docker

5. Check running Docker containers:
   docker ps
6. Create flask app build
   docker build -t flask-app .

6. Run the Docker container:
   docker run -d -p 5000:5000 flask-app

7. Check running containers again:
   docker ps
------------------------------------------------------------------------------------------------

Step 3 
1 Go to Network setting 
2 Create port rule -- inbound rule 
3 Destination port ranges to 5000


----------------------------------------------------------------------------------------------
Step 4 
copy the VM IP and write 5000 after that and search it on web it will show you the webpage 
