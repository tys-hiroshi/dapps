https://pypi.org/project/eciespy/

python3 -m venv .venv
source .venv/bin/activate
pip3 install eciespy
pip3 freeze | grep -v "pkg-resources" > requirements.txt

https://qiita.com/unhurried/items/dc4734b8cc6b9c7493da

代表的なアルゴリズム
鍵共有
Elliptic Curve Diffie-Hellman Key Agreement (ECDH)
署名
Elliptic Curve Digital Signature Algorithm (ECDSA)
暗号化
Elliptic Curve Integrated Encryption Scheme (ECIES)


