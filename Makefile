EL7=build-el7
EL8=build-el8
EL9=build-el9

#---------------------------------------------#
# push to building machines
#---------------------------------------------#
push: spec src
spec:
	rsync -avc --delete ./SPECS/   build-el7:~/rpmbuild/SPECS/
	rsync -avc --delete ./SPECS/   build-el8:~/rpmbuild/SPECS/
	rsync -avc --delete ./SPECS/   build-el9:~/rpmbuild/SPECS/
src:
	rsync -avc --delete ./SOURCES/ build-el7:~/rpmbuild/SOURCES/
	rsync -avc --delete ./SOURCES/ build-el8:~/rpmbuild/SOURCES/
	rsync -avc --delete ./SOURCES/ build-el9:~/rpmbuild/SOURCES/
push7:
	ssh build-el7 'mkdir -p ~/rpmbuild/SOURCES ~/rpmbuild/SPECS'
	rsync -avc --delete ./SOURCES/ build-el7:~/rpmbuild/SOURCES/
	rsync -avc --delete ./SPECS/   build-el7:~/rpmbuild/SPECS/
push8:
	ssh build-el8 'mkdir -p ~/rpmbuild/SOURCES ~/rpmbuild/SPECS'
	rsync -avc --delete ./SOURCES/ build-el8:~/rpmbuild/SOURCES/
	rsync -avc --delete ./SPECS/   build-el8:~/rpmbuild/SPECS/
push9:
	ssh build-el9 'mkdir -p ~/rpmbuild/SOURCES ~/rpmbuild/SPECS'
	rsync -avc --delete ./SOURCES/ build-el9:~/rpmbuild/SOURCES/
	rsync -avc --delete ./SPECS/   build-el9:~/rpmbuild/SPECS/

#---------------------------------------------#
# pull rpm from building machines
#---------------------------------------------#

save-rpm:
	ssh -t build-el7 'sudo rm -rf /tmp/rpms/; mkdir /tmp/rpms; sudo cp -r /root/rpmbuild/RPMS/x86_64 /tmp/rpms'
	ssh -t build-el8 'sudo rm -rf /tmp/rpms/; mkdir /tmp/rpms; sudo cp -r /root/rpmbuild/RPMS/x86_64 /tmp/rpms'
	ssh -t build-el9 'sudo rm -rf /tmp/rpms/; mkdir /tmp/rpms; sudo cp -r /root/rpmbuild/RPMS/x86_64 /tmp/rpms'
pigsty-rpm:
	#ssh -t build-el7 'sudo mv -f /tmp/pigsty-rpm/RPMS/* /www/pigsty/'
	ssh -t build-el8 'sudo mv -f /tmp/pigsty-rpm/RPMS/* /www/pigsty/'
	ssh -t build-el9 'sudo mv -f /tmp/pigsty-rpm/RPMS/* /www/pigsty/'
pull-rpm:
	#rsync -avc build-el7:/tmp/pigsty-rpm/RPMS/  /data/pigsty-rpm/RPMS/el7.x86_64/
	rsync --delete -avc build-el8:/tmp/rpms/  /data/pigsty-rpm/RPMS/el8.x86_64/
	rsync --delete -avc build-el9:/tmp/rpms/  /data/pigsty-rpm/RPMS/el9.x86_64/
pull-srpm:
	ssh build-el8 'sudo cp -r /root/rpmbuild/SRPMS/* /tmp/pigsty-rpm/SRPMS/'
	rsync -avc build-el8:/tmp/pigsty-rpm/SRPMS/ /data/pigsty-rpm/SRPMS/
clean:
	find . -type f -name .DS_Store -delete

pull:
	ssh sv 'cd /data/pigsty-rpm; make pull-sv'
	rsync -avc --delete sv:/data/pigsty-rpm/RPMS/ ./RPMS/

pull-sv:
	cd /data/pigsty-rpm/RPMS;
	mkdir -p el8.x86_64 el9.x86_64;
	rsync -avc --delete build-el7:/tmp/el7.x86_64/ ./RPMS/el7.x86_64/
	rsync -avc --delete build-el8:/tmp/el8.x86_64/ ./RPMS/el8.x86_64/
	rsync -avc --delete build-el9:/tmp/el9.x86_64/ ./RPMS/el9.x86_64/

#---------------------------------------------#
# publish
#---------------------------------------------#
sync: release
pub: release
release: clean
	coscmd upload --recursive -s -f -y --delete --ignore .idea . yum

.PHONY: push pull pulld build build-on-sv push9 pull9 build9 build-sv build-on-el9 clean sync pub release