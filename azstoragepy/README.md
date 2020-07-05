python3 -m venv .venv
source .venv/bin/activate
pip3 install azure-storage-blob
pip3 install PyYAML

pip3 freeze | grep -v "pkg-resources" > requirements.txt

