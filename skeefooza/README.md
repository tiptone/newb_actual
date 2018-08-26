
```
cd .. 
virtualenv --system-site-packages -p python3  skeefooza
cd skeefooza
source ./bin/activate
pip install -U tensorflow
python -c "import tensorflow as tf; print(tf.__version__)"
python3 ./hello_world.py
pip install -U Keras
```
