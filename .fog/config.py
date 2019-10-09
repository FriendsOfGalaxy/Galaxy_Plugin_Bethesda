# -------- consts ---------

# url of original repository from github
UPSTREAM = 'https://github.com/TouwaStar/Galaxy_Plugin_Bethesda'
# branch to be checked for new updates
RELEASE_BRANCH = 'master'
# integration source directory, where the manifest.json is placed; relative to the repository root
SRC = 'betty'

# --------- jobs -----------

# if pack job is not present, simple zip files will be produced with SRC content
# def pack(output):
#     pass
