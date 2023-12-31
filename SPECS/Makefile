#---------------------------------------------#
# EL
#---------------------------------------------#
default:
	echo "make make basic"

#---------------------------------------------#
# scws
#---------------------------------------------#
scws:
	rm -rf /root/rpmbuild/RPMS/x86_64/scws*.rpm /tmp/pigsty-rpm/RPMS/scws*.rpm
	QA_RPATHS=2 rpmbuild -ba /root/rpmbuild/SPECS/scws.spec

# scws is required when building zhparser
scws-install:
	yum remove -y scws || /bin/true
	rpm -ivh /root/rpmbuild/RPMS/x86_64/scws-1.2.3-1PIGSTY.el*.x86_64.rpm

# pure-C or pure-SQL extensions
basic:
	make zhparser pg_roaringbitmap pg_tle pgsql-http pgjwt vault hydra pg_filedump pg_net pointcloud # age

#---------------------------------------------#
# zhparser
#---------------------------------------------#
zhparser:
	rm -rf /root/rpmbuild/RPMS/x86_64/zhparser*.rpm;
	QA_RPATHS=2 rpmbuild --define "pgmajorversion 12" -ba /root/rpmbuild/SPECS/zhparser.spec
	QA_RPATHS=2 rpmbuild --define "pgmajorversion 13" -ba /root/rpmbuild/SPECS/zhparser.spec
	QA_RPATHS=2 rpmbuild --define "pgmajorversion 14" -ba /root/rpmbuild/SPECS/zhparser.spec
	QA_RPATHS=2 rpmbuild --define "pgmajorversion 15" -ba /root/rpmbuild/SPECS/zhparser.spec
	QA_RPATHS=2 rpmbuild --define "pgmajorversion 16" -ba /root/rpmbuild/SPECS/zhparser.spec


#---------------------------------------------#
# pg_roaringbitmap
#---------------------------------------------#
pg_roaringbitmap:
	rm -rf /root/rpmbuild/RPMS/x86_64/pg_roaringbitmap*.rpm;
	rpmbuild --define "pgmajorversion 12" -ba /root/rpmbuild/SPECS/pg_roaringbitmap.spec
	rpmbuild --define "pgmajorversion 13" -ba /root/rpmbuild/SPECS/pg_roaringbitmap.spec
	rpmbuild --define "pgmajorversion 14" -ba /root/rpmbuild/SPECS/pg_roaringbitmap.spec
	rpmbuild --define "pgmajorversion 15" -ba /root/rpmbuild/SPECS/pg_roaringbitmap.spec
	rpmbuild --define "pgmajorversion 16" -ba /root/rpmbuild/SPECS/pg_roaringbitmap.spec

#---------------------------------------------#
# pg_tle (deps: krb5-devel) rename to v1.2.0 (no el7)
#---------------------------------------------#
pg_tle:
	rm -rf /root/rpmbuild/RPMS/x86_64/pg_tle*.rpm;
	rpmbuild --define "pgmajorversion 12" -ba /root/rpmbuild/SPECS/pg_tle.spec
	rpmbuild --define "pgmajorversion 13" -ba /root/rpmbuild/SPECS/pg_tle.spec
	rpmbuild --define "pgmajorversion 14" -ba /root/rpmbuild/SPECS/pg_tle.spec
	rpmbuild --define "pgmajorversion 15" -ba /root/rpmbuild/SPECS/pg_tle.spec
	rpmbuild --define "pgmajorversion 16" -ba /root/rpmbuild/SPECS/pg_tle.spec

#---------------------------------------------#
# pgsql-http (libcurl-devel) rename to v1.6.0.tar.gz
#---------------------------------------------#
pgsql-http:
	rm -rf /root/rpmbuild/RPMS/x86_64/pgsql-http*.rpm;
	rpmbuild --define "pgmajorversion 12" -ba /root/rpmbuild/SPECS/pgsql-http.spec
	rpmbuild --define "pgmajorversion 13" -ba /root/rpmbuild/SPECS/pgsql-http.spec
	rpmbuild --define "pgmajorversion 14" -ba /root/rpmbuild/SPECS/pgsql-http.spec
	rpmbuild --define "pgmajorversion 15" -ba /root/rpmbuild/SPECS/pgsql-http.spec
	rpmbuild --define "pgmajorversion 16" -ba /root/rpmbuild/SPECS/pgsql-http.spec

#---------------------------------------------#
# pgjwt
#---------------------------------------------#
pgjwt:
	rm -rf /root/rpmbuild/RPMS/x86_64/pgjwt*.rpm;
	rpmbuild --without debuginfo --define "pgmajorversion 12" -ba /root/rpmbuild/SPECS/pgjwt.spec
	rpmbuild --without debuginfo --define "pgmajorversion 13" -ba /root/rpmbuild/SPECS/pgjwt.spec
	rpmbuild --without debuginfo --define "pgmajorversion 14" -ba /root/rpmbuild/SPECS/pgjwt.spec
	rpmbuild --without debuginfo --define "pgmajorversion 15" -ba /root/rpmbuild/SPECS/pgjwt.spec
	rpmbuild --without debuginfo --define "pgmajorversion 16" -ba /root/rpmbuild/SPECS/pgjwt.spec

#---------------------------------------------#
# vault
#---------------------------------------------#
vault:
	rm -rf /root/rpmbuild/RPMS/x86_64/pgjwt*.rpm;
	rpmbuild --without debuginfo --define "pgmajorversion 12" -ba /root/rpmbuild/SPECS/vault.spec
	rpmbuild --without debuginfo --define "pgmajorversion 13" -ba /root/rpmbuild/SPECS/vault.spec
	rpmbuild --without debuginfo --define "pgmajorversion 14" -ba /root/rpmbuild/SPECS/vault.spec
	rpmbuild --without debuginfo --define "pgmajorversion 15" -ba /root/rpmbuild/SPECS/vault.spec
	rpmbuild --without debuginfo --define "pgmajorversion 16" -ba /root/rpmbuild/SPECS/vault.spec


#---------------------------------------------#
# pointcloud
#---------------------------------------------#
pointcloud:
	rm -rf /root/rpmbuild/RPMS/x86_64/pgjwt*.rpm;
	rpmbuild --without debuginfo --define "pgmajorversion 12" -ba /root/rpmbuild/SPECS/pointcloud.spec
	rpmbuild --without debuginfo --define "pgmajorversion 13" -ba /root/rpmbuild/SPECS/pointcloud.spec
	rpmbuild --without debuginfo --define "pgmajorversion 14" -ba /root/rpmbuild/SPECS/pointcloud.spec
	rpmbuild --without debuginfo --define "pgmajorversion 15" -ba /root/rpmbuild/SPECS/pointcloud.spec
	rpmbuild --without debuginfo --define "pgmajorversion 16" -ba /root/rpmbuild/SPECS/pointcloud.spec


#---------------------------------------------#
# imgsmlr
#---------------------------------------------#
imgsmlr:
	rm -rf /root/rpmbuild/RPMS/x86_64/imgsmlr*.rpm;
	rpmbuild --without debuginfo --define "pgmajorversion 12" -ba /root/rpmbuild/SPECS/imgsmlr.spec
	rpmbuild --without debuginfo --define "pgmajorversion 13" -ba /root/rpmbuild/SPECS/imgsmlr.spec
	rpmbuild --without debuginfo --define "pgmajorversion 14" -ba /root/rpmbuild/SPECS/imgsmlr.spec
	rpmbuild --without debuginfo --define "pgmajorversion 15" -ba /root/rpmbuild/SPECS/imgsmlr.spec


#---------------------------------------------#
# pg_similarity
#---------------------------------------------#
pg_similarity:
	rm -rf /root/rpmbuild/RPMS/x86_64/imgsmlr*.rpm;
	rpmbuild --without debuginfo --define "pgmajorversion 12" -ba /root/rpmbuild/SPECS/pg_similarity.spec
	rpmbuild --without debuginfo --define "pgmajorversion 13" -ba /root/rpmbuild/SPECS/pg_similarity.spec
	rpmbuild --without debuginfo --define "pgmajorversion 14" -ba /root/rpmbuild/SPECS/pg_similarity.spec
	rpmbuild --without debuginfo --define "pgmajorversion 15" -ba /root/rpmbuild/SPECS/pg_similarity.spec


#---------------------------------------------#
# pg_bigm
#---------------------------------------------#
pg_bigm:
	rm -rf /root/rpmbuild/RPMS/x86_64/imgsmlr*.rpm;
	rpmbuild --without debuginfo --define "pgmajorversion 12" -ba /root/rpmbuild/SPECS/pg_bigm.spec
	rpmbuild --without debuginfo --define "pgmajorversion 13" -ba /root/rpmbuild/SPECS/pg_bigm.spec
	rpmbuild --without debuginfo --define "pgmajorversion 14" -ba /root/rpmbuild/SPECS/pg_bigm.spec
	rpmbuild --without debuginfo --define "pgmajorversion 15" -ba /root/rpmbuild/SPECS/pg_bigm.spec
	rpmbuild --without debuginfo --define "pgmajorversion 16" -ba /root/rpmbuild/SPECS/pg_bigm.spec

#---------------------------------------------#
# hydra (lz4-devel libzstd-devel)
#---------------------------------------------#
hydra:
	rm -rf /root/rpmbuild/RPMS/x86_64/hydra*.rpm;
	PATH=/usr/pgsql-15/bin:/usr/bin/:$PATH rpmbuild --define "pgmajorversion 15" -ba /root/rpmbuild/SPECS/hydra.spec
	PATH=/usr/pgsql-14/bin:/usr/bin/:$PATH rpmbuild --define "pgmajorversion 14" -ba /root/rpmbuild/SPECS/hydra.spec
	PATH=/usr/pgsql-13/bin:/usr/bin/:$PATH rpmbuild --define "pgmajorversion 13" -ba /root/rpmbuild/SPECS/hydra.spec

#---------------------------------------------#
# pg_filedump (lz4-devel libzstd-devel)
#---------------------------------------------#
pg_filedump:
	rm -rf /root/rpmbuild/RPMS/x86_64/pg_filedump*.rpm;
	rpmbuild --define "pgmajorversion 16" -ba /root/rpmbuild/SPECS/pg_filedump.spec

#---------------------------------------------#
# apache-age  (dnf install perl perl-FindBin)
# yum install gcc glibc glib-common readline readline-devel zlib zlib-devel flex bison
#---------------------------------------------#
age:
	rm -rf /root/rpmbuild/RPMS/x86_64/age*.rpm;
	rpmbuild --define "pgmajorversion 15" -ba /root/rpmbuild/SPECS/age.spec

#---------------------------------------------#
# pg_net
#---------------------------------------------#
pg_net:
	rm -rf /root/rpmbuild/RPMS/x86_64/pg_net*.rpm;
	rpmbuild --define "pgmajorversion 12" -ba /root/rpmbuild/SPECS/pg_net.spec
	rpmbuild --define "pgmajorversion 13" -ba /root/rpmbuild/SPECS/pg_net.spec
	rpmbuild --define "pgmajorversion 14" -ba /root/rpmbuild/SPECS/pg_net.spec
	rpmbuild --define "pgmajorversion 15" -ba /root/rpmbuild/SPECS/pg_net.spec
	rpmbuild --define "pgmajorversion 16" -ba /root/rpmbuild/SPECS/pg_net.spec

#---------------------------------------------#
# pg_graphql RUST
#---------------------------------------------#
pg_graphql:
	rm -rf /root/rpmbuild/SOURCES/pg_graphql-pg16 /root/rpmbuild/SOURCES/pg_graphql-pg15 /root/rpmbuild/SOURCES/pg_graphql-pg14;
	cp -r /root/pg_graphql-1.4.0/target/release/pg_graphql-pg16 /root/rpmbuild/SOURCES/;
	cp -r /root/pg_graphql-1.4.0/target/release/pg_graphql-pg15 /root/rpmbuild/SOURCES/;
	cp -r /root/pg_graphql-1.4.0/target/release/pg_graphql-pg14 /root/rpmbuild/SOURCES/;
	rpmbuild --without debuginfo --define "pgmajorversion 16" -ba /root/rpmbuild/SPECS/pg_graphql.spec
	rpmbuild --without debuginfo --define "pgmajorversion 15" -ba /root/rpmbuild/SPECS/pg_graphql.spec
	rpmbuild --without debuginfo --define "pgmajorversion 14" -ba /root/rpmbuild/SPECS/pg_graphql.spec


#---------------------------------------------#
# pgml RUST
#---------------------------------------------#
pgml:
	rm -rf /root/rpmbuild/SOURCES/pgml-pg1*;
	cp -r /tmp/postgresml/pgml-extension/target/release/pgml-pg1* /root/rpmbuild/SOURCES/
	rpmbuild --without debuginfo --define "pgmajorversion 15" -ba /root/rpmbuild/SPECS/pgml.spec
	rpmbuild --without debuginfo --define "pgmajorversion 14" -ba /root/rpmbuild/SPECS/pgml.spec
	rpmbuild --without debuginfo --define "pgmajorversion 13" -ba /root/rpmbuild/SPECS/pgml.spec
	rpmbuild --without debuginfo --define "pgmajorversion 12" -ba /root/rpmbuild/SPECS/pgml.spec


#---------------------------------------------#
# srpm
#---------------------------------------------#
srpm:
	rpmbuild --define "pgmajorversion 15"  -bs ~/rpmbuild/SPECS/scws.spec
	rpmbuild --define "pgmajorversion 15"  -bs ~/rpmbuild/SPECS/zhparser.spec
	rpmbuild --define "pgmajorversion 15"  -bs ~/rpmbuild/SPECS/pg_embedding.spec
	rpmbuild --define "pgmajorversion 15"  -bs ~/rpmbuild/SPECS/pg_roaringbitmap.spec
	rpmbuild --define "pgmajorversion 15"  -bs ~/rpmbuild/SPECS/pg_tle.spec
	rpmbuild --define "pgmajorversion 15"  -bs ~/rpmbuild/SPECS/pgsql-http.spec
	rpmbuild --define "pgmajorversion 15"  -bs ~/rpmbuild/SPECS/age.spec

ls-srpm:
	ls -alh  /root/rpmbuild/SRPMS/
ls-rpm:
	ls -alh  /root/rpmbuild/RPMS/x86_64/
rm-srpm:
	rm -rf  /root/rpmbuild/SRPMS/*
rm-rpm:
	rm -rf  /root/rpmbuild/RPMS/*



#---------------------------------------------#
# repo build
#---------------------------------------------#
repo7:
	rm -rf /tmp/el7.x86_64; mkdir -p /tmp/el7.x86_64/debug
	cp -r /root/rpmbuild/RPMS/x86_64/* /tmp/el7.x86_64/
	cd /tmp/el7.x86_64/ && mv *debug*.rpm debug/
	cd /tmp/el7.x86_64/ && createrepo_c .
	cd /tmp/el7.x86_64/debug && createrepo_c .
	chmod -R a+r /tmp/el7.x86_64/

repo8:
	rm -rf /tmp/el8.x86_64; mkdir -p /tmp/el8.x86_64/debug
	cp -r /root/rpmbuild/RPMS/x86_64/* /tmp/el8.x86_64/
	cd /tmp/el8.x86_64/ && mv *debug*.rpm debug/
	cd /tmp/el8.x86_64/ && createrepo_c . && repo2module -s stable . modules.yaml && modifyrepo_c --mdtype=modules modules.yaml repodata/
	cd /tmp/el8.x86_64/debug && createrepo_c . && repo2module -s stable . modules.yaml && modifyrepo_c --mdtype=modules modules.yaml repodata/
	chmod -R a+r /tmp/el8.x86_64/

repo9:
	rm -rf /tmp/el9.x86_64; mkdir -p /tmp/el9.x86_64/debug
	cp -r /root/rpmbuild/RPMS/x86_64/* /tmp/el9.x86_64/
	cd /tmp/el9.x86_64/ && mv *debug*.rpm debug/
	cd /tmp/el9.x86_64/ && 	createrepo_c . && repo2module -s stable . modules.yaml && modifyrepo_c --mdtype=modules modules.yaml repodata/
	cd /tmp/el9.x86_64/debug && createrepo_c . && repo2module -s stable . modules.yaml && modifyrepo_c --mdtype=modules modules.yaml repodata/
	chmod -R a+r /tmp/el9.x86_64/


#---------------------------------------------#
# phony
#---------------------------------------------#
.PHONY: zhparser zhparser-srpm zhparser-rpm \
		pg_embedding pg_embedding-srpm pg_embedding-rpm \


