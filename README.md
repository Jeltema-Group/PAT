# PAT
Pixel Analyzing Tool (PAT) - A tool for computing statistical values for images using CIAO DMSTAT tool.

## Getting Started 
We'll start by installing Anaconda inside your personal directory within INIGO. You'll need to visit the [Anaconda](https://www.anaconda.com/products/individual#linux) page and download the Linux installer. 

Once you have that file downloaed on your local machine, transfer it to your remote directory something like in INIGO:

```
scp filename.extension username@inigo.ucsc.edu:/home/user
```

Now log in to INIGO and run `ls` to make sure the `Anaconda3-20XX.XX-Linux-x86_64.sh` file is your INIGO directory, if so run it using:

```
bash Anaconda3-20XX.XX-Linux-x86_64.sh
```

Follow the prompt instructions. If you've accepted the User License Agreement Terms then the location where Anaconda will be installed is displayed. Ensure path is correct, something like this:

```
Anaconda3 will now be installed into this location:
/home/user/anaconda3

  - Press ENTER to confirm location
```
At the end of the package installation you'll be asked:

```
Do you wish the installer to initialize Anaconda3
by running conda init? [yes|no]
[no] >>>
```
Ensure you enter yes. If the outcome indicates you have chosen to not have conda modify your shell scripts, then run the following:

```
source /home/user/anaconda3/bin/activate
```

```
conda init
``` 

You should now see the `base` env activated. For more details visit the Frequently Asked Questions page under the question [Should I add Anaconda to the macOS or Linux PATH?](https://docs.anaconda.com/anaconda/user-guide/faq/#:~:text=During%20installation%2C%20you%20will%20be,your%20shell%20scripts%20at%20all.)

That concludes the Anaconda installation. 

## Creating CIAO environment in INIGO.

Start by visiting the [Anaconda Cloud](https://anaconda.org/CXC/ciao-4.12-caldb-Linux/files) website and download the CIAO-4.XX `environment.yml` file which we'll need create the CIAO envirornment. 

Transfer the file from your local machine to your remote directory in INIGO:

```
scp filename.extension username@inigo.ucsc.edu:/home/user
```

Log in to INIGO and activate conda if not already active:

```
conda activate base
```

Now lets create the CIAO environment:

```
conda env create -f ciao-4.XX-caldb-Linux-environment.yml
```

Once finished, activate the environment:

```
conda activate ciao-4.XX-caldb
``` 

Done!

## Downloading Dependencies

   * [Astropy](https://anaconda.org/conda-forge/astropy)
   * [Pandas](https://anaconda.org/conda-forge/pandas)
   * [Jupyter lab](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html) 

```
conda install -c conda-forge astropy
conda install -c conda-forge pandas
conda install -c conda-forge jupyterlab
```
## Work Space with Jupyter Lab

To start jupyter lab run 
```
conda jupyter lab
``` 

and a web browser will open with jupyter lab running. In case that a web browser cannot connect to Localhost, then read on.

First we need to forward the remote port XXXX (default=8888) to our local machine's port YYYY (you decide what four numbers) and listen to it so that we can run Jupyter lab on our webpage. Run the following:

```
ssh -Y -N -f -L Localhost:YYYY:Localhost:8888 username@inigo.ucsc.edu
```

Now log in the usual way:

```
ssh -Y username@inigo.ucsc.edu
```
Once inside INIGO, run jupyter lab:

```
conda jupyter lab
```

Open your web browser and type `localhost:YYYY` and the jupyter lab should start. 

Assuming the jupyter lab ran and opened in browser, you'll be prompted to create a password to secure your notebook. Follow the instructions or visit [Jupyter Password Setup](https://jupyter-notebook.readthedocs.io/en/stable/public_server.html)

Done!

## Running `PAT`

`PAT.py` is simple to use. It requires one arguement (a catalog). 

```
python3.X PAT.py fitsfilename.fits
```

I use `python3.X` to use the python version in my CIAO env. You can verify which python you're using by typing in the terminal:

```
which python
```

Done!
