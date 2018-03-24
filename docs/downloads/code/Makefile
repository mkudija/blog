PY?=python3

help:
	@echo '                                                                          '
	@echo 'Makefile to update websites on MAG GitHub pages                           '
	@echo '                                                                          '
	@echo 'Usage:                                                                    '
	@echo '   make html                                                              '
	@echo '   <verify you like the changes that were made>                           '
	@echo '   make publish                                                           '
	@echo '                                                                          '
	@echo 'Commands:                                                                 '
	@echo '   make data                MILE_file_copy and update_utilization         '
	@echo '   make html                make data, then regenerate the websites       '
	@echo '   make html-only           regenerate the websites (no data update)      '
	@echo '   make publish             publish regenerated websites to GitHub        '
	@echo '                                                                          '

data:
	python ../MILE_Data/MILE_file_copy.py
	cd ../Aircraft-Data/Utilization/Scripts; python update_utilization.py

html: data
	cd ../CommercialData/scripts; python build.py
	cd ../MarketView/scripts; python build.py
	cd ../FleetView/scripts; python build.py

html-only:
	cd ../CommercialData/scripts; python build.py
	cd ../MarketView/scripts; python build.py
	cd ../FleetView/scripts; python build.py

publish:
	@echo ' '
	cd ../CommercialData; git pull origin master
	cd ../CommercialData; git add -A
	cd ../CommercialData; git commit -m "auto-regenerate from make"
	cd ../CommercialData; git push origin master

	@echo ' '
	cd ../MarketView; git pull origin master
	cd ../MarketView; git add -A
	cd ../MarketView; git commit -m "auto-regenerate from make"
	cd ../MarketView; git push origin master

	@echo ' '
	cd ../FleetView; git pull origin master
	cd ../FleetView; git add -A
	cd ../FleetView; git commit -m "auto-regenerate from make"
	cd ../FleetView; git push origin master

	@echo 'Done.'