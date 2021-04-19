# sublist3r_dig

A script that combines [sublist3r](https://github.com/aboul3la/Sublist3r.git)  and the [dig](https://github.com/iagox86/dnsutils.git) utility.
Domain name parser. The output is a txt file with all the ip addresses that are associated with this domain

## Installation

```
git clone https://github.com/iizakharov/sublist3r_dig.git
```

## Recommended Python Version:

Sublist3r currently supports **Python 2** and **Python 3**.

* The recommended version for Python 2 is **2.7.x**
* The recommended version for Python 3 is **3.4.x**

## Dependencies:

Sublist3r_dig depends on the `sublister` (`requests`, `dnspython` and `argparse`) python modules.

These dependencies can be installed using the requirements file:

- Installation on Windows:
```
c:\python27\python.exe -m pip install -r requirements.txt
```
- Installation on Linux
```
sudo pip install -r requirements.txt
```


### Examples

* To list all the basic options and switches use -h switch:

```python main.py ```

```>> Enter your domain name: google.com```


After the script is completed, a file with the same name will appear with all the ip addresses


## License

Sublist3r is licensed under the GNU GPL license. take a look at the [LICENSE](https://github.com/aboul3la/Sublist3r/blob/master/LICENSE) for more information.
