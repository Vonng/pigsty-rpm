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

	rpmbuild --define "pgmajorversion 12" -ba ~/rpmbuild/SPECS/pgsql_http.spec
	rpmbuild --define "pgmajorversion 13" -ba ~/rpmbuild/SPECS/pgsql_http.spec
	rpmbuild --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/pgsql_http.spec
	rpmbuild --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/pgsql_http.spec

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

	rpmbuild --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/age15.spec

	#rpmbuild --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/pg_filedump.spec