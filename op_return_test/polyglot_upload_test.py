import polyglot

uploader = polyglot.Upload('your private key goes here in WIF format')
# Optional parameters shown for completeness are populated from the file path by default
filepath = "img/bitcoinsv.png"
uploader.upload_b(filepath)