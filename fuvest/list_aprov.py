from zipfile import ZipFile

with ZipFile('aprov2004.zip') as zip:
    with zip.open('aprov2004.txt','rU') as txt:

        for lin in txt:
            lin = lin.strip()
            if not lin: continue
            print lin

