EL7=el7
EL8=el8
EL9=el9


#---------------------------------------------#
# sync to/from building server
#---------------------------------------------#
push-sv:
	rsync -avc ./ sv:/data/pigsty-rpm/
pushd-sv:
	rsync -avc --delete ./ sv:/data/pigsty-rpm/
repo-sv:
	ssh sv 'cd /data/pigsty-rpm && make create'
push-rpm:
	rsync -avc  ./RPMS/ sv:/data/pigsty-rpm/RPMS/
pushd-rpm:
	rsync -avc --delete ./RPMS/ sv:/data/pigsty-rpm/RPMS/
pull-sv:
	rsync -avc sv:/data/pigsty-rpm/RPMS/ ./RPMS/
pulld-sv:
	rsync --delete -avc sv:/data/pigsty-rpm/RPMS/ ./RPMS/
update: push-sv repo-sv pull-sv
updated: pushd-sv repo-sv pulld-sv
pushss: push-sv
	ssh sv 'cd /data/pigsty-rpm && make push'

#---------------------------------------------#
# push to building machines
#---------------------------------------------#
push: spec srcd
spec:
	#rsync -avc --delete ./SPECS/   el7:~/rpmbuild/SPECS/
	rsync -avc --delete ./SPECS/   el8:~/rpmbuild/SPECS/
	rsync -avc --delete ./SPECS/   el9:~/rpmbuild/SPECS/
src:
	#rsync -avc ./SOURCES/ el7:~/rpmbuild/SOURCES/
	rsync -avc ./SOURCES/ el8:~/rpmbuild/SOURCES/
	rsync -avc ./SOURCES/ el9:~/rpmbuild/SOURCES/
srcd:
	#rsync -avc --delete ./SOURCES/ el7:~/rpmbuild/SOURCES/
	rsync -avc --delete ./SOURCES/ el8:~/rpmbuild/SOURCES/
	rsync -avc --delete ./SOURCES/ el9:~/rpmbuild/SOURCES/
push7:
	ssh el7 'mkdir -p ~/rpmbuild/SOURCES ~/rpmbuild/SPECS'
	rsync -avc --delete ./SOURCES/ el7:~/rpmbuild/SOURCES/
	rsync -avc --delete ./SPECS/   el7:~/rpmbuild/SPECS/
push8:
	ssh el8 'mkdir -p ~/rpmbuild/SOURCES ~/rpmbuild/SPECS'
	rsync -avc --delete ./SOURCES/ el8:~/rpmbuild/SOURCES/
	rsync -avc --delete ./SPECS/   el8:~/rpmbuild/SPECS/
push9:
	ssh el9 'mkdir -p ~/rpmbuild/SOURCES ~/rpmbuild/SPECS'
	rsync -avc --delete ./SOURCES/ el9:~/rpmbuild/SOURCES/
	rsync -avc --delete ./SPECS/   el9:~/rpmbuild/SPECS/

#---------------------------------------------#
# pull rpm from building machines
#---------------------------------------------#
pull: dirs pull8 pull9 adjust create
purge:
	rm -rf RPMS/*
dirs:
	mkdir -p RPMS/el7.x86_64/debug RPMS/el8.x86_64/debug RPMS/el9.x86_64/debug
pull7:
	rsync -avz el7:~/rpmbuild/RPMS/x86_64/ RPMS/el7.x86_64/
pull8:
	rsync -avz el8:~/rpmbuild/RPMS/x86_64/ RPMS/el8.x86_64/
pull9:
	rsync -avz el9:~/rpmbuild/RPMS/x86_64/ RPMS/el9.x86_64/
adjust:
	chown -R root:root RPMS
	#mv -f RPMS/el7.x86_64/*-debug* RPMS/el7.x86_64/debug/
	mv -f RPMS/el8.x86_64/*-debug* RPMS/el8.x86_64/debug/
	mv -f RPMS/el9.x86_64/*-debug* RPMS/el9.x86_64/debug/
create:
	cd RPMS/el7.x86_64/ && createrepo_c .;
	cd RPMS/el8.x86_64/ && createrepo_c . && repo2module -s stable . modules.yaml && modifyrepo_c --mdtype=modules modules.yaml repodata/;
	cd RPMS/el9.x86_64/ && createrepo_c . && repo2module -s stable . modules.yaml && modifyrepo_c --mdtype=modules modules.yaml repodata/;
	cd RPMS/el7.x86_64/debug && createrepo_c .;
	cd RPMS/el8.x86_64/debug && createrepo_c . && repo2module -s stable . modules.yaml && modifyrepo_c --mdtype=modules modules.yaml repodata/;
	cd RPMS/el9.x86_64/debug && createrepo_c . && repo2module -s stable . modules.yaml && modifyrepo_c --mdtype=modules modules.yaml repodata/;
rmds:
	find . -type f -name .DS_Store -delete

#---------------------------------------------#
# publish
#---------------------------------------------#
sync: release
pub: release
release: clean
	coscmd upload --recursive -s -f -y --delete --ignore .idea . yum

.PHONY: push pull pulld build on-sv push9 pull9 build9 sv on-el9 clean sync pub release