# Simple MPTCP

This repository contains installation scripts and essential documentation for setting up a basic Mininet topology that utilizes MPTCPv**1**, built directly from the source code.

## Topology

![image](https://user-images.githubusercontent.com/32551374/227388394-631b94c1-bd23-4881-8d55-775c8ba6cbee.png)

## Setup Instructions

Follow these steps to set up the Simple MPTCP environment:

1. Clone the repository:
```bash
git clone https://github.com/mrconter1/simple_mptcp/
```

2. Navigate to the `simple_mptcp` directory and run the setup script. You can also follow the script manually if preferred:
```bash
cd simple_mptcp
sudo bash setup.sh
```

3. Reboot your computer after the successful execution of the script.

4. Choose the newly installed kernel, `>= 6.3.0-rc2+`, in the GRUB menu during boot

5. Verify that the new MPTCP kernel has been installed correctly by executing `main.py`:
```bash
sudo python3 main.py
```

After completing these steps, you should have a functional Mininet topology with MPTCPv**1** support.

## Components Overview

### main.py

The main file is in charge of creating and configuring the Mininet network. It executes _server.py_ on the h2-node and subsequently runs _client.py_ on the h1-node.

### server.py

This file sets up a server that attempts to open an MPTCP socket and listens for incoming connections. Once a connection is established with a client, the server sends 100 MB of data as a response.

### client.py

The client script is designed to connect to the server and prepare to receive 100 MB of data. It measures and reports the data transfer characteristics during the process.