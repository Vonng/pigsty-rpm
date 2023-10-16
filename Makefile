# SSH ALIAS
EL7=el7
EL8=el8
EL9=el9
U22=ubuntu22

#---------------------------------------------#
# push to building machines
#---------------------------------------------#
pt: pt8 pt9
pt7:
	rsync -avc --delete ./SOURCES/ $(EL7):/root/rpmbuild/SOURCES/
	rsync -avc --delete ./SPECS/   $(EL7):/root/rpmbuild/SPECS/
pt8:
	rsync -avc --delete ./SOURCES/ $(EL8):/root/rpmbuild/SOURCES/
	rsync -avc --delete ./SPECS/   $(EL8):/root/rpmbuild/SPECS/
pt9:
	rsync -avc --delete ./SOURCES/ $(EL9):/root/rpmbuild/SOURCES/
	rsync -avc --delete ./SPECS/   $(EL9):/root/rpmbuild/SPECS/
pl: pl8 pl9
pl7:
	rsync -avc $(EL7):/root/rpmbuild/RPMS/x86_64/ RPMS/el7.x86_64/
pl8:
	rsync -avc $(EL8):/root/rpmbuild/RPMS/x86_64/ RPMS/el8.x86_64
pl9:
	rsync -avc $(EL9):/root/rpmbuild/RPMS/x86_64/ RPMS/el9.x86_64


#---------------------------------------------#
# push/pull changes on local host
#---------------------------------------------#
push: clean
	rsync -avc --delete ./SOURCES/ sv:/data/pigsty-rpm/SOURCES/
	rsync -avc --delete ./SPECS/   sv:/data/pigsty-rpm/SPECS/
	scp Makefile sv:/data/pigsty-rpm/Makefile
p7: push
	ssh sv "cd /data/pigsty-rpm; make push7"
p8: push
	ssh sv "cd /data/pigsty-rpm; make push8"
p9: push
	ssh sv "cd /data/pigsty-rpm; make push9"
pp: push
	ssh sv "cd /data/pigsty-rpm; make push7"
	ssh sv "cd /data/pigsty-rpm; make push8"
	ssh sv "cd /data/pigsty-rpm; make push9"


#---------------------------------------------#
# push to building machines
#---------------------------------------------#
push7:
	ssh build-el7 'mkdir -p /tmp/pigsty-rpm/SOURCES /tmp/pigsty-rpm/SPECS'
	rsync -avc --delete /data/pigsty-rpm/SOURCES/ build-el7:/tmp/pigsty-rpm/SOURCES/
	rsync -avc --delete /data/pigsty-rpm/SPECS/   build-el7:/tmp/pigsty-rpm/SPECS/
	ssh build-el7 'sudo rm -rf /root/rpmbuild/SOURCES/* /root/rpmbuild/SPECS/*; sudo cp -r /tmp/pigsty-rpm/SOURCES/* /root/rpmbuild/SOURCES/; sudo cp -r /tmp/pigsty-rpm/SPECS/* /root/rpmbuild/SPECS/'
push8:
	ssh build-el8 'mkdir -p /tmp/pigsty-rpm/SOURCES /tmp/pigsty-rpm/SPECS'
	rsync -avc --delete /data/pigsty-rpm/SOURCES/ build-el8:/tmp/pigsty-rpm/SOURCES/
	rsync -avc --delete /data/pigsty-rpm/SPECS/   build-el8:/tmp/pigsty-rpm/SPECS/
	ssh build-el8 'sudo rm -rf /root/rpmbuild/SOURCES/* /root/rpmbuild/SPECS/*; sudo cp -r /tmp/pigsty-rpm/SOURCES/* /root/rpmbuild/SOURCES/; sudo cp -r /tmp/pigsty-rpm/SPECS/* /root/rpmbuild/SPECS/'
push9:
	ssh build-el9 'mkdir -p /tmp/pigsty-rpm/SOURCES /tmp/pigsty-rpm/SPECS'
	rsync -avc --delete /data/pigsty-rpm/SOURCES/ build-el9:/tmp/pigsty-rpm/SOURCES/
	rsync -avc --delete /data/pigsty-rpm/SPECS/   build-el9:/tmp/pigsty-rpm/SPECS/
	ssh build-el9 'sudo rm -rf /root/rpmbuild/SOURCES/* /root/rpmbuild/SPECS/*; sudo cp -r /tmp/pigsty-rpm/SOURCES/* /root/rpmbuild/SOURCES/; sudo cp -r /tmp/pigsty-rpm/SPECS/* /root/rpmbuild/SPECS/'
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