# Libcalculator
This project was created to try the usage of `.so` or shared object libraries in python.
Mainly used for the purpose of optimising processes and code secrecy when being shared.

## To run this project (considering a linux based OS):
1. Setup the virtual environment.
```
python3 -m venv libc
```

2. Install the required libraries.
```
pip3 install -r requirements.txt
```

3. Run the `setup.py`.
```
python3 setup.py
```

4. After compilation, all `pyx` files in the libcalculator module can be deleted.

5. Run the tests:
```
python3 test.py
```