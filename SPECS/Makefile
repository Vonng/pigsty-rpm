#---------------------------------------------#
# EL
#---------------------------------------------#
all: zhparser pg_embedding pg_roaringbitmap pg_tle pgsql-http age

# el7 does not have pg 16 & pg_tle & pg_embedding
el7:

	QA_RPATHS=2 rpmbuild --define "pgmajorversion 12" -ba /root/rpmbuild/SPECS/zhparser.spec
	QA_RPATHS=2 rpmbuild --define "pgmajorversion 13" -ba /root/rpmbuild/SPECS/zhparser.spec
	QA_RPATHS=2 rpmbuild --define "pgmajorversion 14" -ba /root/rpmbuild/SPECS/zhparser.spec
	QA_RPATHS=2 rpmbuild --define "pgmajorversion 15" -ba /root/rpmbuild/SPECS/zhparser.spec

	rpmbuild --define "pgmajorversion 12" -ba /root/rpmbuild/SPECS/pg_roaringbitmap.spec
	rpmbuild --define "pgmajorversion 13" -ba /root/rpmbuild/SPECS/pg_roaringbitmap.spec
	rpmbuild --define "pgmajorversion 14" -ba /root/rpmbuild/SPECS/pg_roaringbitmap.spec
	rpmbuild --define "pgmajorversion 15" -ba /root/rpmbuild/SPECS/pg_roaringbitmap.spec

	rpmbuild --define "pgmajorversion 12" -ba /root/rpmbuild/SPECS/pgsql-http.spec
	rpmbuild --define "pgmajorversion 13" -ba /root/rpmbuild/SPECS/pgsql-http.spec
	rpmbuild --define "pgmajorversion 14" -ba /root/rpmbuild/SPECS/pgsql-http.spec
	rpmbuild --define "pgmajorversion 15" -ba /root/rpmbuild/SPECS/pgsql-http.spec

	rpmbuild --define "pgmajorversion 15" -ba /root/rpmbuild/SPECS/age.spec

#---------------------------------------------#
# scws
#---------------------------------------------#
scws:
	rm -rf /root/rpmbuild/RPMS/x86_64/scws*.rpm /tmp/pigsty-rpm/RPMS/scws*.rpm
	QA_RPATHS=2 rpmbuild -ba /root/rpmbuild/SPECS/scws.spec

# scws is required when building zhparser
scws-install:
	rpm -ivh /root/rpmbuild/RPMS/x86_64/scws-1.2.3-PIGSTY1.el*.x86_64.rpm

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
# pg_embedding (no el7)
#---------------------------------------------#
pg_embedding:
	rm -rf /root/rpmbuild/RPMS/x86_64/pg_embedding*.rpm;
	rpmbuild --define "pgmajorversion 12" -ba /root/rpmbuild/SPECS/pg_embedding.spec
	rpmbuild --define "pgmajorversion 13" -ba /root/rpmbuild/SPECS/pg_embedding.spec
	rpmbuild --define "pgmajorversion 14" -ba /root/rpmbuild/SPECS/pg_embedding.spec
	rpmbuild --define "pgmajorversion 15" -ba /root/rpmbuild/SPECS/pg_embedding.spec
	rpmbuild --define "pgmajorversion 16" -ba /root/rpmbuild/SPECS/pg_embedding.spec

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
# apache-age  (dnf install perl perl-FindBin)
# yum install gcc glibc glib-common readline readline-devel zlib zlib-devel flex bison
#---------------------------------------------#
age:
	rm -rf /root/rpmbuild/RPMS/x86_64/age*.rpm;
	rpmbuild --define "pgmajorversion 15" -ba /root/rpmbuild/SPECS/age.spec

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
# phony
#---------------------------------------------#
.PHONY: zhparser zhparser-srpm zhparser-rpm \
		pg_embedding pg_embedding-srpm pg_embedding-rpm \

