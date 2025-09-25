# Product Service

The Product Service is a simple web service built using Rust and the Warp web framework. It is responsible for serving the product catalog, which includes a list of products that can be fetched via a RESTful API.

## Requirements

- Python
- pip

## Setup Instructions
1. Update your package list:
   ```bash
   sudo apt update
2. Install python

   ```bash
   sudo apt-get install python3.6
3. Install package installer for python
   ```bash
   sudo apt install python3-pip
5. Navigate to the `product-service` directory:
   ```bash
   cd product-service
6. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
- The service will be running on `http://localhost:3030` if installed locally or on `http://<your-vm-public-ip>:3030` if installed on Azure VM
- When you connect to the VM with VS Code Remote - SSH, VS Code sets up an SSH tunnel. By default it auto-forwards ports that your remote process opens (setting: remote.autoForwardPorts: true). So when your Rust service on the VM listens on 127.0.0.1:3030 (the VM’s loopback), VS Code forwards that remote port to your local machine as localhost:3030.
   - In other words:
      ```
      [Your laptop] http://localhost:3030  <--tunnel-->  [Azure VM] 127.0.0.1:3030
      ```
   - Only your machine can reach it this way; it’s not public on the internet.

## Testing
1. Install the `REST Client` extension in VS Code to use `.http` files.
2. Use the provided `test-product-service.http` file to test the service.

