EL7=build-el7
EL8=build-el8
EL9=build-el9


#---------------------------------------------#
# sync to/from building server
#---------------------------------------------#
push-sv:
	rsync -avc ./ sv:/data/pigsty-rpm/
repo-sv:
	ssh sv 'cd /data/pigsty-rpm && make create'
pull-sv:
	rsync -avc sv:/data/pigsty-rpm/RPMS/ ./RPMS/
update: push-sv repo-sv pull-sv

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
pull: dirs pull7 pull8 pull9 adjust create
purge:
	rm -rf RPMS/*
dirs:
	mkdir -p RPMS/el7.x86_64/debug RPMS/el8.x86_64/debug RPMS/el9.x86_64/debug
pull7:
	rsync -avz build-el7:~/rpmbuild/RPMS/x86_64/ RPMS/el7.x86_64/

pull8:
	rsync -avz build-el8:~/rpmbuild/RPMS/x86_64/ RPMS/el8.x86_64/

pull9:
	rsync -avz build-el9:~/rpmbuild/RPMS/x86_64/ RPMS/el9.x86_64/
adjust:
	chown -R root:root RPMS
	mv -f RPMS/el7.x86_64/*-debug* RPMS/el7.x86_64/debug/
	mv -f RPMS/el8.x86_64/*-debug* RPMS/el8.x86_64/debug/
	mv -f RPMS/el9.x86_64/*-debug* RPMS/el9.x86_64/debug/
create:
	cd RPMS/el7.x86_64/ && createrepo_c .;
	cd RPMS/el7.x86_64/debug && createrepo_c .;
	cd RPMS/el8.x86_64/ && createrepo_c . && repo2module -s stable . modules.yaml && modifyrepo_c --mdtype=modules modules.yaml repodata/;
	cd RPMS/el8.x86_64/debug && createrepo_c . && repo2module -s stable . modules.yaml && modifyrepo_c --mdtype=modules modules.yaml repodata/;
	cd RPMS/el9.x86_64/ && createrepo_c . && repo2module -s stable . modules.yaml && modifyrepo_c --mdtype=modules modules.yaml repodata/;
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

.PHONY: push pull pulld build build-on-sv push9 pull9 build9 build-sv build-on-el9 clean sync pub release