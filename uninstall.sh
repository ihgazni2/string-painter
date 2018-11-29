pip3 uninstall spaint
git rm -r dist
git rm -r build
git rm -r spaint.egg-info
rm -r dist
rm -r build
rm -r spaint.egg-info
git add .
git commit -m "remove old build"

#sed -i s/spaint/spaint/g uninstall.py
