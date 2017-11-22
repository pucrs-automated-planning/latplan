# latplan
LatPlan : A domain-independent, image-based classical planner

This fork changed the root dir, so it is possible to use without further modifications.

To install and run latplan you have the following options:
- Create a virtualenv with Python 3.5.x and install the necessary packages
- Use Leonardo's virtualenv on LSA

## Standard installation
- First create a virtualenv using at least python 3.5.x.
- Install Keras and Tensorflow
- Run **latplan/install.sh**
- Follow further instructions in the original readme inside the #latplan# folder
## LSA Leonardo's virtual env
```
source /home/leonardo/latplan/latplan/bin/activate
```
## Running latplan
Currently **test_all.sh** does not seem to be working due to path issues, trying to fix that. Additionally **do-everything.sh** can be only executed as root.
To train the networks use:
```
./train_all.sh
```
or
```
./train_all_fast.sh
```
Output is going to "samples/<problem_name>". Encoder and decoder weights are being saved there.
