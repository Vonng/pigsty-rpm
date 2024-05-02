#---------------------------------------------#
# EL
#---------------------------------------------#
default:
	echo "make make basic"

#---------------------------------------------#
# scws
#---------------------------------------------#
scws:
	rm -rf ~/rpmbuild/RPMS/x86_64/scws*.rpm /tmp/pigsty-rpm/RPMS/scws*.rpm
	QA_RPATHS=2 rpmbuild -ba ~/rpmbuild/SPECS/scws.spec

# scws is required when building zhparser
scws-install:
	sudo yum remove -y scws || /bin/true
	sudo rpm -ivh ~/rpmbuild/RPMS/x86_64/scws-1.2.3-1PIGSTY.el*.x86_64.rpm

# pure-C or pure-SQL extensions
basic:
	make zhparser pg_roaringbitmap pg_tle pgsql-http pgjwt vault hydra pg_filedump pg_net pointcloud # age

#---------------------------------------------#
# zhparser
#---------------------------------------------#
zhparser:
	rm -rf ~/rpmbuild/RPMS/x86_64/zhparser*.rpm;
	QA_RPATHS=2 rpmbuild --define "pgmajorversion 12" -ba ~/rpmbuild/SPECS/zhparser.spec
	QA_RPATHS=2 rpmbuild --define "pgmajorversion 13" -ba ~/rpmbuild/SPECS/zhparser.spec
	QA_RPATHS=2 rpmbuild --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/zhparser.spec
	QA_RPATHS=2 rpmbuild --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/zhparser.spec
	QA_RPATHS=2 rpmbuild --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/zhparser.spec   # not available on el7


#---------------------------------------------#
# pg_roaringbitmap
#---------------------------------------------#
pg_roaringbitmap:
	rm -rf ~/rpmbuild/RPMS/x86_64/pg_roaringbitmap*.rpm;
	rpmbuild --define "pgmajorversion 12" -ba ~/rpmbuild/SPECS/pg_roaringbitmap.spec
	rpmbuild --define "pgmajorversion 13" -ba ~/rpmbuild/SPECS/pg_roaringbitmap.spec
	rpmbuild --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/pg_roaringbitmap.spec
	rpmbuild --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/pg_roaringbitmap.spec
	rpmbuild --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/pg_roaringbitmap.spec   # not available on el7

#---------------------------------------------#
# pg_tle (deps: krb5-devel) rename to v1.2.0 (no el7)
#---------------------------------------------#
pg_tle:
	rm -rf ~/rpmbuild/RPMS/x86_64/pg_tle*.rpm;
	rpmbuild --define "pgmajorversion 12" -ba ~/rpmbuild/SPECS/pg_tle.spec
	rpmbuild --define "pgmajorversion 13" -ba ~/rpmbuild/SPECS/pg_tle.spec
	rpmbuild --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/pg_tle.spec
	rpmbuild --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/pg_tle.spec
	rpmbuild --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/pg_tle.spec   # not available on el7

#---------------------------------------------#
# pgsql-http (libcurl-devel)
#---------------------------------------------#
pgsql-http:
	rm -rf ~/rpmbuild/RPMS/x86_64/pgsql-http*.rpm;
	rpmbuild --define "pgmajorversion 12" -ba ~/rpmbuild/SPECS/pgsql-http.spec
	rpmbuild --define "pgmajorversion 13" -ba ~/rpmbuild/SPECS/pgsql-http.spec
	rpmbuild --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/pgsql-http.spec
	rpmbuild --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/pgsql-http.spec
	rpmbuild --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/pgsql-http.spec

#---------------------------------------------#
# pgsql-gzip
#---------------------------------------------#
pgsql-gzip:
	rm -rf ~/rpmbuild/RPMS/x86_64/pgsql-gzip*.rpm;
	rpmbuild --define "pgmajorversion 12" -ba ~/rpmbuild/SPECS/pgsql-gzip.spec
	rpmbuild --define "pgmajorversion 13" -ba ~/rpmbuild/SPECS/pgsql-gzip.spec
	rpmbuild --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/pgsql-gzip.spec
	rpmbuild --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/pgsql-gzip.spec
	rpmbuild --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/pgsql-gzip.spec

#---------------------------------------------#
# pgjwt
#---------------------------------------------#
pgjwt:
	rm -rf ~/rpmbuild/RPMS/x86_64/pgjwt*.rpm;
	rpmbuild --without debuginfo --define "pgmajorversion 12" -ba ~/rpmbuild/SPECS/pgjwt.spec
	rpmbuild --without debuginfo --define "pgmajorversion 13" -ba ~/rpmbuild/SPECS/pgjwt.spec
	rpmbuild --without debuginfo --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/pgjwt.spec
	rpmbuild --without debuginfo --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/pgjwt.spec
	rpmbuild --without debuginfo --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/pgjwt.spec

#---------------------------------------------#
# vault
#---------------------------------------------#
vault:
	rm -rf ~/rpmbuild/RPMS/x86_64/vault*.rpm;
	rpmbuild --without debuginfo --define "pgmajorversion 12" -ba ~/rpmbuild/SPECS/vault.spec
	rpmbuild --without debuginfo --define "pgmajorversion 13" -ba ~/rpmbuild/SPECS/vault.spec
	rpmbuild --without debuginfo --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/vault.spec
	rpmbuild --without debuginfo --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/vault.spec
	rpmbuild --without debuginfo --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/vault.spec

#---------------------------------------------#
# pointcloud
#---------------------------------------------#
pointcloud:
	rm -rf ~/rpmbuild/RPMS/x86_64/pointcloud*.rpm;
	rpmbuild --without debuginfo --define "pgmajorversion 12" -ba ~/rpmbuild/SPECS/pointcloud.spec
	rpmbuild --without debuginfo --define "pgmajorversion 13" -ba ~/rpmbuild/SPECS/pointcloud.spec
	rpmbuild --without debuginfo --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/pointcloud.spec
	rpmbuild --without debuginfo --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/pointcloud.spec
	rpmbuild --without debuginfo --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/pointcloud.spec

#---------------------------------------------#
# imgsmlr (12-15)
#---------------------------------------------#
imgsmlr:
	rm -rf ~/rpmbuild/RPMS/x86_64/imgsmlr*.rpm;
	rpmbuild --without debuginfo --define "pgmajorversion 12" -ba ~/rpmbuild/SPECS/imgsmlr.spec
	rpmbuild --without debuginfo --define "pgmajorversion 13" -ba ~/rpmbuild/SPECS/imgsmlr.spec
	rpmbuild --without debuginfo --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/imgsmlr.spec
	rpmbuild --without debuginfo --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/imgsmlr.spec

#---------------------------------------------#
# pg_similarity (12-15)
#---------------------------------------------#
pg_similarity:
	rm -rf ~/rpmbuild/RPMS/x86_64/pg_similarity*.rpm;
	rpmbuild --without debuginfo --define "pgmajorversion 12" -ba ~/rpmbuild/SPECS/pg_similarity.spec
	rpmbuild --without debuginfo --define "pgmajorversion 13" -ba ~/rpmbuild/SPECS/pg_similarity.spec
	rpmbuild --without debuginfo --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/pg_similarity.spec
	rpmbuild --without debuginfo --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/pg_similarity.spec

#---------------------------------------------#
# pg_bigm (12-15)
#---------------------------------------------#
pg_bigm:
	rm -rf ~/rpmbuild/RPMS/x86_64/pg_bigm*.rpm;
	rpmbuild --without debuginfo --define "pgmajorversion 12" -ba ~/rpmbuild/SPECS/pg_bigm.spec
	rpmbuild --without debuginfo --define "pgmajorversion 13" -ba ~/rpmbuild/SPECS/pg_bigm.spec
	rpmbuild --without debuginfo --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/pg_bigm.spec
	rpmbuild --without debuginfo --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/pg_bigm.spec

#---------------------------------------------#
# hydra (lz4-devel libzstd-devel)
#---------------------------------------------#
hydra:
	rm -rf ~/rpmbuild/RPMS/x86_64/hydra*.rpm;
	PATH=/usr/pgsql-13/bin:/usr/bin/:$PATH rpmbuild --define "pgmajorversion 13" -ba ~/rpmbuild/SPECS/hydra.spec
	PATH=/usr/pgsql-14/bin:/usr/bin/:$PATH rpmbuild --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/hydra.spec
	PATH=/usr/pgsql-15/bin:/usr/bin/:$PATH rpmbuild --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/hydra.spec
	PATH=/usr/pgsql-16/bin:/usr/bin/:$PATH rpmbuild --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/hydra.spec

#---------------------------------------------#
# pg_net (el7 not available)
#---------------------------------------------#
pg_net:
	rm -rf ~/rpmbuild/RPMS/x86_64/pg_net*.rpm;
	rpmbuild --define "pgmajorversion 12" -ba ~/rpmbuild/SPECS/pg_net.spec
	rpmbuild --define "pgmajorversion 13" -ba ~/rpmbuild/SPECS/pg_net.spec
	rpmbuild --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/pg_net.spec
	rpmbuild --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/pg_net.spec
	rpmbuild --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/pg_net.spec


#---------------------------------------------#
# pg_filedump (lz4-devel libzstd-devel)
#---------------------------------------------#
pg_filedump:
	rm -rf ~/rpmbuild/RPMS/x86_64/pg_filedump*.rpm;
	rpmbuild --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/pg_filedump.spec

#---------------------------------------------#
# apache-age  (dnf install perl perl-FindBin)
# yum install gcc glibc glib-common readline readline-devel zlib zlib-devel flex bison
#---------------------------------------------#
age:
	rm -rf ~/rpmbuild/RPMS/x86_64/age*.rpm;
	rpmbuild --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/age16.spec

age15:
	rm -rf ~/rpmbuild/RPMS/x86_64/age*.rpm;
	rpmbuild --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/age15.spec

#---------------------------------------------#
# EL7
#---------------------------------------------#
el7:
	QA_RPATHS=2 rpmbuild --define "pgmajorversion 12" -ba ~/rpmbuild/SPECS/zhparser.spec
	QA_RPATHS=2 rpmbuild --define "pgmajorversion 13" -ba ~/rpmbuild/SPECS/zhparser.spec
	QA_RPATHS=2 rpmbuild --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/zhparser.spec
	QA_RPATHS=2 rpmbuild --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/zhparser.spec

	rpmbuild --define "pgmajorversion 12" -ba ~/rpmbuild/SPECS/pg_roaringbitmap.spec
	rpmbuild --define "pgmajorversion 13" -ba ~/rpmbuild/SPECS/pg_roaringbitmap.spec
	rpmbuild --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/pg_roaringbitmap.spec
	rpmbuild --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/pg_roaringbitmap.spec

	rpmbuild --define "pgmajorversion 12" -ba ~/rpmbuild/SPECS/pg_tle.spec
	rpmbuild --define "pgmajorversion 13" -ba ~/rpmbuild/SPECS/pg_tle.spec
	rpmbuild --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/pg_tle.spec
	rpmbuild --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/pg_tle.spec

	rpmbuild --define "pgmajorversion 12" -ba ~/rpmbuild/SPECS/pgsql-http.spec
	rpmbuild --define "pgmajorversion 13" -ba ~/rpmbuild/SPECS/pgsql-http.spec
	rpmbuild --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/pgsql-http.spec
	rpmbuild --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/pgsql-http.spec

	rpmbuild --without debuginfo --define "pgmajorversion 12" -ba ~/rpmbuild/SPECS/pgjwt.spec
	rpmbuild --without debuginfo --define "pgmajorversion 13" -ba ~/rpmbuild/SPECS/pgjwt.spec
	rpmbuild --without debuginfo --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/pgjwt.spec
	rpmbuild --without debuginfo --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/pgjwt.spec

	rpmbuild --without debuginfo --define "pgmajorversion 12" -ba ~/rpmbuild/SPECS/vault.spec
	rpmbuild --without debuginfo --define "pgmajorversion 13" -ba ~/rpmbuild/SPECS/vault.spec
	rpmbuild --without debuginfo --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/vault.spec
	rpmbuild --without debuginfo --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/vault.spec

	rpmbuild --without debuginfo --define "pgmajorversion 12" -ba ~/rpmbuild/SPECS/pointcloud.spec
	rpmbuild --without debuginfo --define "pgmajorversion 13" -ba ~/rpmbuild/SPECS/pointcloud.spec
	rpmbuild --without debuginfo --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/pointcloud.spec
	rpmbuild --without debuginfo --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/pointcloud.spec

	rpmbuild --without debuginfo --define "pgmajorversion 12" -ba ~/rpmbuild/SPECS/imgsmlr.spec
	rpmbuild --without debuginfo --define "pgmajorversion 13" -ba ~/rpmbuild/SPECS/imgsmlr.spec
	rpmbuild --without debuginfo --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/imgsmlr.spec
	rpmbuild --without debuginfo --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/imgsmlr.spec

	rpmbuild --without debuginfo --define "pgmajorversion 12" -ba ~/rpmbuild/SPECS/pg_similarity.spec
	rpmbuild --without debuginfo --define "pgmajorversion 13" -ba ~/rpmbuild/SPECS/pg_similarity.spec
	rpmbuild --without debuginfo --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/pg_similarity.spec
	rpmbuild --without debuginfo --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/pg_similarity.spec

	rpmbuild --without debuginfo --define "pgmajorversion 12" -ba ~/rpmbuild/SPECS/pg_bigm.spec
	rpmbuild --without debuginfo --define "pgmajorversion 13" -ba ~/rpmbuild/SPECS/pg_bigm.spec
	rpmbuild --without debuginfo --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/pg_bigm.spec
	rpmbuild --without debuginfo --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/pg_bigm.spec

	PATH=/usr/pgsql-13/bin:/usr/bin/:$PATH rpmbuild --define "pgmajorversion 13" -ba ~/rpmbuild/SPECS/hydra.spec
	PATH=/usr/pgsql-14/bin:/usr/bin/:$PATH rpmbuild --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/hydra.spec
	PATH=/usr/pgsql-15/bin:/usr/bin/:$PATH rpmbuild --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/hydra.spec

	rpmbuild --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/pg_filedump.spec
	rpmbuild --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/age15.spec

el89: zhparser pg_roaringbitmap pg_tle pgsql-http pgjwt vault pointcloud imgsmlr pg_similarity pg_bigm hydra pg_net pg_filedump age


#---------------------------------------------#
# pg_graphql [RUST]
#---------------------------------------------#
pg_graphql:
	rm -rf ~/rpmbuild/RPMS/x86_64/pg_graphql*.rpm;
	rpmbuild --without debuginfo --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/pg_graphql.spec
	rpmbuild --without debuginfo --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/pg_graphql.spec
	rpmbuild --without debuginfo --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/pg_graphql.spec

#---------------------------------------------#
# pgml [RUST]
#---------------------------------------------#
pgml:
	rm -rf ~/rpmbuild/RPMS/x86_64/pgml*.rpm;
	rpmbuild --without debuginfo --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/pgml.spec
	rpmbuild --without debuginfo --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/pgml.spec
	rpmbuild --without debuginfo --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/pgml.spec

#---------------------------------------------#
# pg_bm25 [RUST]
#---------------------------------------------#
pg_search:
	rm -rf ~/rpmbuild/RPMS/x86_64/pg_bm25*.rpm;
	rpmbuild --without debuginfo --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/pg_bm25.spec
	rpmbuild --without debuginfo --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/pg_bm25.spec

#---------------------------------------------#
# pg_analytics [RUST]
#---------------------------------------------#
pg_analytics:
	rm -rf ~/rpmbuild/RPMS/x86_64/pg_analytics*.rpm;
	rpmbuild --without debuginfo --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/pg_analytics.spec
	rpmbuild --without debuginfo --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/pg_analytics.spec

#---------------------------------------------#
# pg_sparse
#---------------------------------------------#
pg_sparse:
	rm -rf ~/rpmbuild/RPMS/x86_64/pg_sparse*.rpm;
	rpmbuild --define "pgmajorversion 12" -ba ~/rpmbuild/SPECS/pg_sparse.spec
	rpmbuild --define "pgmajorversion 13" -ba ~/rpmbuild/SPECS/pg_sparse.spec
	rpmbuild --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/pg_sparse.spec
	rpmbuild --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/pg_sparse.spec
	rpmbuild --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/pg_sparse.spec

#---------------------------------------------#
# duckdb & duckdb_fdw
#---------------------------------------------#
libduckdb:
	rm -rf ~/rpmbuild/RPMS/x86_64/libduckdb*.rpm;
	rpmbuild -ba ~/rpmbuild/SPECS/libduckdb.spec

duckdb_fdw:
	rpmbuild --define "pgmajorversion 12" -ba ~/rpmbuild/SPECS/duckdb_fdw.spec
	rpmbuild --define "pgmajorversion 13" -ba ~/rpmbuild/SPECS/duckdb_fdw.spec
	rpmbuild --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/duckdb_fdw.spec
	rpmbuild --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/duckdb_fdw.spec
	rpmbuild --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/duckdb_fdw.spec


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
	ls -alh  ~/rpmbuild/SRPMS/
ls-rpm:
	ls -alh  ~/rpmbuild/RPMS/x86_64/
rm-srpm:
	rm -rf  ~/rpmbuild/SRPMS/*
rm-rpm:
	rm -rf  ~/rpmbuild/RPMS/*

#---------------------------------------------#
# repo build
#---------------------------------------------#
repo7:
	rm -rf /tmp/el7.x86_64; mkdir -p /tmp/el7.x86_64/debug
	cp -r ~/rpmbuild/RPMS/x86_64/* /tmp/el7.x86_64/
	cd /tmp/el7.x86_64/ && mv *debug*.rpm debug/
	cd /tmp/el7.x86_64/ && createrepo_c .
	cd /tmp/el7.x86_64/debug && createrepo_c .
	chmod -R a+r /tmp/el7.x86_64/

repo8:
	rm -rf /tmp/el8.x86_64; mkdir -p /tmp/el8.x86_64/debug
	cp -r ~/rpmbuild/RPMS/x86_64/* /tmp/el8.x86_64/
	cd /tmp/el8.x86_64/ && mv *debug*.rpm debug/
	cd /tmp/el8.x86_64/ && createrepo_c . && repo2module -s stable . modules.yaml && modifyrepo_c --mdtype=modules modules.yaml repodata/
	cd /tmp/el8.x86_64/debug && createrepo_c . && repo2module -s stable . modules.yaml && modifyrepo_c --mdtype=modules modules.yaml repodata/
	chmod -R a+r /tmp/el8.x86_64/

repo9:
	rm -rf /tmp/el9.x86_64; mkdir -p /tmp/el9.x86_64/debug
	cp -r ~/rpmbuild/RPMS/x86_64/* /tmp/el9.x86_64/
	cd /tmp/el9.x86_64/ && mv *debug*.rpm debug/
	cd /tmp/el9.x86_64/ && 	createrepo_c . && repo2module -s stable . modules.yaml && modifyrepo_c --mdtype=modules modules.yaml repodata/
	cd /tmp/el9.x86_64/debug && createrepo_c . && repo2module -s stable . modules.yaml && modifyrepo_c --mdtype=modules modules.yaml repodata/
	chmod -R a+r /tmp/el9.x86_64/


#---------------------------------------------#
# phony
#---------------------------------------------#
.PHONY: zhparser zhparser-srpm zhparser-rpm \
		pg_embedding pg_embedding-srpm pg_embedding-rpm \


