# Clean up the old resources
rm -f design.py
rm -f design.pyc
rm -f design_resources.py
rm -f design_resources.pyc

pyrcc4 -py3 designer/design_resources.qrc -o design_resources.py
pyuic4 designer/design.ui -o design_temp.py
# Can't figure out how to force pyuic to correctly link design_resources 
sed 's/design_resources_rc/design_resources/' design_temp.py > design.py
rm -f design_temp.py
